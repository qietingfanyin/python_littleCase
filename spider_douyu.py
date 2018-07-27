import requests
import re
#1准备要爬取的url,提交请求，获取页面文本，用正则选择出需要的相关资源链接url2，再次提交请求，将获取的文本保存在本地文件夹
url = "https://www.douyu.com/directory/game/yz"
r = requests.get(url)
print(r.status_code)
str = r.text
# print(str)
pic_url=re.findall(r"(https.+\.jpg)", str)
# print(pic_url)
pic_num = 0
for pic in pic_url:
    image_r = requests.get(pic)
    # print(image_r.status_code)
    path = pic.split("/")[-1]
    with open("douyu_pic/"+path,'wb') as d:
         d.write(image_r.content)
         print("正在保存图片")
         pic_num += 1
print(pic_num)

