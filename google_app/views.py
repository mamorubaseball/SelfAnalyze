from ctypes.wintypes import INT
from email import header
from http.client import UnimplementedFileMode
import re
from urllib import request
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
from google_app.api.serializers import UserSerializer
import requests

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
        requests.post("http://127.0.0.1:8000/api/googleCalender/",data=json.dumps(validate_data),headers=headers)

        # responce = requests.put("http://127.0.0.1:8000/api/googleCalender/1",data=json.dumps(validate_data),headers=headers)
        ans = {'lists':lists}
        return self.render_to_response(ans)
        # return render(request, 'index.html',lists)



