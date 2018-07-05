###encoding: utf-8
import requests
import json
#import urllib.parse

#url = 'https://oapi.dingtalk.com/robot/send?access_token=858e8d74b977e854516410389ef5485d05da4e0564321637012f0c9a3081cec0'
url = 'https://oapi.dingtalk.com/robot/send?access_token=911bbd2cfefc7d2de0cc9f538ecdf0c025cb387be3f321765750c5c4548f2edf'

HEADERS = {
"Content-Type": "application/json ;charset=utf-8 "
}
String_textMsg = {\
"msgtype": "markdown",\
"markdown": {"title":"diaodong_test",\
"text":""" # stock today goes here  > \
\n > ## reported by david """ \
} \
}
String_textMsg = json.dumps(String_textMsg)
res = requests.post(url, data=String_textMsg, headers=HEADERS)
print(res.text)


