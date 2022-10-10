from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import json
import datetime, re
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
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client.json', SCOPES) #保存したjsonファイルを入力する
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
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
    for user in User_ids:
        user_id = user["id"]
        user_name = user["summary"]
        # 直近１ヶ月のイベントを取得する
        event_list = service.events().list(
            calendarId=user_id, timeMin=time_min,timeMax=time_max,singleEvents=True,
            orderBy='startTime').execute()

        sum_time_training = all_time(event_list["items"])
        print("今月の{}時間は{}時間です".format(user_name,sum_time_training))

    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()