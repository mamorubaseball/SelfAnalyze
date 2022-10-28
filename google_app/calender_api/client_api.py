from __future__ import print_function
from dataclasses import dataclass
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import json

import datetime, re
import calendar

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

def get_time(is_registered):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # path_token = "google_app/google_token/{}.json".format(email)
    path = "google_app/google_token/mamorubasebaii5.json"

    # tokenがない場合は発行する
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "google_app/calender_api/client.json", SCOPES) #保存したclient.jsonファイルを入力する
            creds = flow.run_local_server(port=8081) 

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
    month_time_data = {}
        #　2022年の現在月までの各月のデータを取得
    month_lists = []
    this_year = datetime.date.today().year
    this_month = datetime.date.today().month
    if is_registered:
        start = datetime.datetime(this_year,this_month,1,0,0,0)
        start = f"{start.isoformat()}Z"
        end = datetime.datetime.utcnow().isoformat()+"Z"
        for user in User_ids:
            user_id = user["id"]
            user_name = user["summary"]
            event_list = service.events().list(
            calendarId=user_id, timeMin=start,timeMax=end,singleEvents=True,
            orderBy='startTime').execute()
            sum_time_training = all_time(event_list["items"])
            time_data.update({user_name:sum_time_training})
        return time_data
    else:#初登録
        # 月毎のデータを取得
        for m in range(this_month):
            month_start_day = datetime.datetime(this_year, m+1, 1, 0, 0, 0)
            last_day = calendar.monthrange(this_year, m+1)[1]
            month_end_day = datetime.datetime(this_year, m+1, last_day, 0, 0, 0)
            month_lists.append([month_start_day,month_end_day])
        month = 1
        for start,end in month_lists:
            start = f"{start.isoformat()}Z"
            end = f"{end.isoformat()}Z"
            for user in User_ids:
                user_id = user["id"]
                user_name = user["summary"]
                event_list = service.events().list(
                calendarId=user_id, timeMin=start,timeMax=end,singleEvents=True,
                orderBy='startTime').execute()
                sum_time_training = all_time(event_list["items"])
                time_data.update({user_name:sum_time_training})
            month_time_data.update({month:time_data})
            month+=1
        return month_time_data