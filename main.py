#!/usr/bin/python3
import requests
import json
import _thread
from selenium import webdriver
import time
import datetime

headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

opt = webdriver.ChromeOptions()
opt.headless = True
drive = webdriver.Chrome(options=opt)

uri = "https://www.iesdouyin.com/share/user/63169086371"

last_aweme_id = 0

def download_video(link, path):
    page = requests.get(link)
    content_size = int(page.headers['content-length'])
    with open(path, "wb") as f:
        for chunk in page.iter_content(chunk_size=1024):
            f.write(chunk)

while True:
    dy_src = requests.get(uri, headers=headers).text
    tac_start = dy_src.find("tac=")
    tac_end = dy_src.find("</script>", tac_start)
    tac = dy_src[tac_start:tac_end]
    #print("获取到的tac:", tac)
    f = open("./tac.js", "w")
    f.write(tac)
    f.close()
    drive.get("file:///C:/Users/admin/PycharmProjects/tiktok-moniter/get_sign.html")
    sign = drive.find_element_by_xpath("/html/body").text
    #print("抖音服务器签名=", sign)
    for i in range(1,60):
        like_uri = "https://www.iesdouyin.com/web/api/v2/aweme/like/?" \
              "user_id=63169086371&sec_uid=&count=1&max_cursor=0&aid=1128&_signature=" \
              + sign + \
              "&dytk=ec509a9933a542deb54f12d5825b3365"
        drive.get(like_uri)
        json_str = drive.find_element_by_xpath("/html/body").text
        server_json = json.loads(json_str)
        try:
            id = server_json["aweme_list"][0]["aweme_id"]
            if id != last_aweme_id :
                print("甜茶在:", datetime.datetime.now(), "观看了视频:", "id:", "dec",  server_json["aweme_list"][0]["desc"], "link:", server_json["aweme_list"][0]["video"]["play_addr_lowbr"]["url_list"][0])
                _thread.start_new_thread(download_video, ( server_json["aweme_list"][0]["video"]["play_addr_lowbr"]["url_list"][0], "./video/" + id + server_json["aweme_list"][0]["desc"] + ".mp4"))
            last_aweme_id = id
        except:
            continue
        else:
            time.sleep(1)

