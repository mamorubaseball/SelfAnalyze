from ctypes.wintypes import INT
from email import header
from http.client import UnimplementedFileMode
import re
from urllib import request
from wsgiref import validate
from django.shortcuts import render
from django.views.generic import TemplateView

#calender function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import json
import datetime, re

# api
from google_app.api.serializers import AccountsSerializer
import requests

# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import AccountForm, AddAccountForm

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']



#時間の計算
def str_to_time(t):
    return  datetime.datetime.strptime(t,"%Y-%m-%dT%H:%M:%S%z")

def all_time(lists):
    time_sum = 0
    # day_of_week = [0 for i in range(7)]
    for list in lists:
        try:
            start = str_to_time(list["start"]["dateTime"])
            end =  str_to_time(list["end"]["dateTime"])
            t = end - start
            time_str = str(t).split(":")
            hour,minute,second = time_str
            time_sum+=float(hour)+float(float(minute)//60)
        except:
            #終日予定を入れている場合
            pass
    return time_sum

def get_time():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # path_token = "google_app/google_token/{}.json".format(email)
    path = "google_app/google_token/mamorubasebaii5.json"
    # if os.path.exists(path):
        # print('pathは存在する')
        # creds = Credentials.from_authorized_user_file("google_app/google_token/mamorubasebaii5.json", SCOPES)

    # tokenがない場合は発行する
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "google_app/client.json", SCOPES) #保存したclient.jsonファイルを入力する
            creds = flow.run_local_server(port=8081)
        # # Save the credentials for the next run
        # with open(path, 'w') as token:
        #     token.write(creds.to_json())
    # print(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    page_token = None
    User_ids = service.calendarList().list(pageToken=page_token).execute()['items']
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # 現在時刻を世界協定時刻（UTC）のISOフォーマットで取得する
    utc_now_str = datetime.datetime.utcnow().isoformat()
    time_min = datetime.datetime.fromisoformat(utc_now_str) - datetime.timedelta(weeks=4)
    time_min = f"{time_min.isoformat()}Z"
    time_max = utc_now_str + "Z"
    time_data = {}
    for user in User_ids:
        user_id = user["id"]
        user_name = user["summary"]
        # 直近１ヶ月のイベントを取得する
        event_list = service.events().list(
            calendarId=user_id, timeMin=time_min,timeMax=time_max,singleEvents=True,
            orderBy='startTime').execute()

        sum_time_training = all_time(event_list["items"])
        time_data.update({user_name:sum_time_training})
    return time_data

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    #変数を渡す
    def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         context["message"] = "Template Viewの変数"
         print("====get_context_data====")
         return context
    #変数を渡す
    def get(self, request, **kwargs):
        context = {
            'message': 'ありがとう'
        }
        return self.render_to_response(context)

    def post(self,request):
        if request.POST:
            lists = get_time()
            print(type(lists))
            if lists:
                calender_list = [k for k,v in lists.items()]
        print(calender_list)
        #apiに追加する処理
        validate_data = {
            "name":"kazuya",
            "email":"kazuya@gmail.com",
            "old":23,
            "sex":"男",
            "data":lists,
            "datalist":{},
            }
        print(validate_data)
        #apiデータ追加その1
        # user = UserSerializer(data = json.dumps(validate_data))
        # user.save()

        #apiデータ追加その2
        headers = {"Content-Type" : "application/json"}
        #新規追加
        requests.post("http://127.0.0.1:8000/api/usr/",data=json.dumps(validate_data),headers=headers)

        # 編集
        # responce = requests.put("http://127.0.0.1:8000/api/googleCalender/1",data=json.dumps(validate_data),headers=headers)
        ans = {'lists':lists}
        return self.render_to_response(ans)
        # return render(request, 'index.html',lists)


def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        headers = {"Content-Type" : "application/json"}
        user = authenticate(username=ID, password=Pass)
        user_data = requests.get("http://127.0.0.1:8000/api/user/?user={}".format(user.id),headers=headers)
        dict = json.loads(user_data.content.decode('utf-8'))
        print("user_data_content",user_data.content)
        id = dict["results"][0]["id"]
        
        # googleカレンダー情報取得
        lists = get_time()
        validate_data = {
            "old":int(dict["results"][0]["old"]),
            "sex":dict["results"][0]["sex"],
            "data":lists,
            "datalist":{},
            "user":user.id,
        }
        requests.put("http://127.0.0.1:8000/api/user/{}".format(int(id)),data=json.dumps(validate_data),headers=headers)
        
        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('google_app:home',kwargs={'pk':id}))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('google_app:Login'))


#ホーム
@login_required
def home(request,pk):
    params = {"UserID":request.user,}
    print(request.user)
    return render(request, "home.html",context=params)

#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"register.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"register.html",context=self.params)
