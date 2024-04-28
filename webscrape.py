import time

from PIL import Image
import io

import requests
from bs4 import BeautifulSoup

import re

#IMPORTS FOR IMAGE SCRAPING (will be used in V2):
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

#FOR IMAGE SCRAPING (will be used in V2):
# from ESRGAN_master import test
# options = webdriver.ChromeOptions()
# service = Service(ChromeDriverManager().install())
# wd = webdriver.Chrome(service=service, options=options)

import requests

def get_weather_api_info(city, api_key='d651c8cbf6434546aef232841242604'):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()
    weather_condition = data['current']['condition']['text']
    temperature = data['current']['temp_c']
    weather_info = f"{temperature}°C"
    return weather_info


def download_image(download_path, url, file_name):
    img_cont = requests.get(url).content
    img_byte = io.BytesIO(img_cont)
    img = Image.open(img_byte)
    file_path = download_path + file_name
    with open(file_path, "wb") as f:
        img.save(f, 'JPEG')


def crop_img(download_path, file_name):
    img1 = Image.open(download_path + file_name)

    w, h = img1.size
    left = 10
    top = 10
    right = w - 10
    bottom = h - 10

    cropped_image = img1.crop((left, top, right, bottom))
    file_path = download_path + file_name
    with open(file_path, "wb") as f:
        cropped_image.save(f, 'JPEG')

dict = {
    "img_url_AQ_North": "http://ns-webcams.its.sfu.ca/public/images/aqn-current.jpg",
    "img_url_AQ_SouthWest":"http://ns-webcams.its.sfu.ca/public/images/aqsw-current.jpg",
    "img_url_AQ_SouthEast":"http://ns-webcams.its.sfu.ca/public/images/aqse-current.jpg",
    "img_url_Gaglardi_intersection":"http://ns-webcams.its.sfu.ca/public/images/gaglardi-current.jpg",
    "img_url_Tower_Road_North ":"http://ns-webcams.its.sfu.ca/public/images/towern-current.jpg",
    "img_url_Tower_Road_South":"http://ns-webcams.its.sfu.ca/public/images/towers-current.jpg",
    "img_url_University_Drive_North":"http://ns-webcams.its.sfu.ca/public/images/udn-current.jpg"
}

#INCASE WE DO IMAGE SCRAPING TWEETS (will be used in V2):
# img_url_AQ_North = "http://ns-webcams.its.sfu.ca/public/images/aqn-current.jpg"
# img_url_AQ_SouthWest = "http://ns-webcams.its.sfu.ca/public/images/aqsw-current.jpg"
# img_url_AQ_SouthEast = "http://ns-webcams.its.sfu.ca/public/images/aqse-current.jpg"
# img_url_Gaglardi_intersection = "http://ns-webcams.its.sfu.ca/public/images/gaglardi-current.jpg"
# img_url_Tower_Road_North = "http://ns-webcams.its.sfu.ca/public/images/towern-current.jpg"
# img_url_Tower_Road_South = "http://ns-webcams.its.sfu.ca/public/images/towers-current.jpg"
# img_url_University_Drive_North = "http://ns-webcams.its.sfu.ca/public/images/udn-current.jpg"
# path = "C:\\Users\\capta\\OneDrive\\Desktop\\bot\\imgs\\"
# loop = True
# for name in dict:
#     download_image(path,dict[name],name+'.jpg')   
# download_image('', img_url,'test.jpg')
# crop_img('',"test.jpg")


def get_weather_info():      
    url = 'https://www.sfu.ca/security/sfuroadconditions/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div_content = soup.find('section', class_='block')
    formatted_text = re.sub(r'\s+', ' ', div_content.get_text()).strip() # formating the string to make it neat

    tempindexstart = formatted_text.find("currently")+10
    tempindexend = 0
    for i in range(tempindexstart, tempindexstart+10):
        if(formatted_text[i] == " "):
            tempindexend = i
            break
    formatted_text = formatted_text[:tempindexstart] + get_weather_api_info("Burnaby")+ formatted_text[tempindexend:] # change temp using weatherapi to make more real
    index = formatted_text.find("Roads: ")
    weather = get_weather_update(formatted_text)
    index2 = formatted_text.find("Weather Conditions Traffic Notices")
    return formatted_text[index:index+7] + weather.upper() +" \n\n" + formatted_text[index+8+len(weather):index2]

def get_weather_update(formatted_text):
    num = formatted_text.find("Roads: ") + 7

    # extract weather condition keyword
    for i in range(20):
        if(formatted_text[num+i] == ' '):
            weathercondition = formatted_text[num:num+i]
            break


    return weathercondition
