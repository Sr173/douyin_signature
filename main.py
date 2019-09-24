#!/usr/bin/python3
import requests
import json
import execjs

headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

uri = "https://www.iesdouyin.com/share/user/63169086371"

print(requests.get(uri, headers=headers).text)

uri = "https://www.iesdouyin.com/web/api/v2/aweme/like/?" \
      "user_id=63169086371&sec_uid=&count=21&max_cursor=0&aid=1128&_signature=" \
      "WQsRyBAVBINQR2vdKnHXRFkLEd" \
      "&dytk=ec509a9933a542deb54f12d5825b3365"

print(requests.get(uri, headers=headers).text)

