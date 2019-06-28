from win10toast import ToastNotifier
import requests
import datetime
import time
import random

def get(rid,live,upcoming):
    now = datetime.datetime.now()
    url = 'https://clist.by/api/v1/json/contest/?&order_by=-start&username=swiggy123&api_key=a0fc6e7ce627ee61b7fced4c976609b97bb65b76&limit=25'
    params = dict({
        'resource__id' : rid
    })
    resp = requests.get(url=url, params=params)
    x = resp.json()
    t = x['objects']
    n=len(t)
    now=str(now)
    for i in range(n):
         if(t[i]['start'][:10:] == now[:10:]):
              if(t[i]['end'][11::]>=now[11:19] and t[i]['start'][11::]<=now[11:19]):
                   live.append(t[i])
              if(t[i]['start'][11::]>=now[11:19]):
                  upcoming.append(t[i])
              else:
                   upcoming .append(t[i])
upcoming1 , upcoming2 , upcoming3 , live1 , live2 , live3 = [] , [] , [], [] , [], []
get(1,live1,upcoming1)
get(2,live2,upcoming2)
get(73,live3,upcoming3)
name=["CODEFORCES CONTEST DETAILS","CODECHEF CONTEST DETAILS","HACKEREARTH CONTEST DETAILS" ]
live_name=["LIVE CONTEST ON CODEFORCES","LIVE CONTEST ON CODECHEF","LIVE CONTEST ON HACKEREARTH" ]
upcoming=[upcoming1,upcoming2,upcoming3]
live=[live1,live2,live3]
for i in range(len(live)):
    for j in range(len(live[i])):
        toaster = ToastNotifier()
        toaster.show_toast(live_name[i],live[i][j]["event"],icon_path="python.ico",duration=4)
for i in range(len(upcoming)):
    for j in range(len(upcoming[i])):
        toaster = ToastNotifier()
        print(str(int((upcoming[i][j]["start"].split('T')[1]).split(':')[0])))
        hr=int((upcoming[i][j]["start"].split('T')[1]).split(':')[0])+5
        min=int((upcoming[i][j]["start"].split('T')[1]).split(':')[1])+30
        hr=hr+int(min/60)
        min=min%60
        s=str(hr)+":"+str(min)
        var=upcoming[i][j]["event"]+" at "+s
        toaster.show_toast(name[i],var,icon_path="python.ico",duration=4)
