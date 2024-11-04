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
def get_weather_info():      
    url = 'https://www.sfu.ca/security/sfuroadconditions/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div_contents = soup.find_all('div', class_='text parbase section')
    for div in div_contents:
        p_tag = div.find('p')
        if p_tag:
            temp_info = re.sub(r'\s+', ' ', p_tag.get_text()).strip()
            if "It is currently" in temp_info:
                formatted_text = temp_info


    return formatted_text

def get_weather_update(formatted_text):
    num = formatted_text.find("Roads: ") + 7

    # extract weather condition keyword
    for i in range(20):
        if(formatted_text[num+i] == ' '):
            weathercondition = formatted_text[num:num+i]
            break


    return weathercondition

def get_update():
    url = 'https://www.sfu.ca/security/sfuroadconditions/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    current = soup.find('div', class_='block grey')
    lines = current.text.split('\n')
    return lines[1].strip() if len(lines) > 1 else None
