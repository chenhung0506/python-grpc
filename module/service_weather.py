# coding: utf-8
import const
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from flask import Flask, jsonify
import datetime
import log as logpy
import re
import utils
import requests
import dao
import pymysql
import json
import redis 

log = logpy.logging.getLogger(__name__)

class lineService(object):
    def chatList(self, user, message):
        try:
            pool = redis.ConnectionPool(host=const.REDIS_IP, port=const.REDIS_PORT, decode_responses=True)
            r = redis.Redis(host=const.REDIS_IP, port=const.REDIS_PORT, decode_responses=True)  
            log.info("user: {}, message: {}".format(user, message))
            if message:
                log.info(r.get(user))
                if r.get(user)=='null' or r.get(user) == None:
                    result=[message]
                    r.setex(user, timedelta(minutes=10), json.dumps(result))
                else:
                    result=json.loads(r.get(user))
                    result.append(message)
                    r.setex(user, timedelta(minutes=10), json.dumps(result))

            return json.loads(r.get(user))
        except Exception as e:
            log.error(utils.except_raise(e))

    def getSoupbyApiChrome(self, url):
        try:
            browser1 = webdriver.Remote(const.CHROMEDRIVER_PATH, DesiredCapabilities.CHROME)
            browser1.get(url)
            soup = BeautifulSoup(browser1.page_source, features='html.parser')
            return soup
        except Exception as e:
            log.error(utils.except_raise(e))
        finally:
            browser1.quit()
    def getSoupbyLocalChrome(self, url):
        try:
            # chromedriver='/usr/local/bin/chromedriver'
            #container alpine linux path
            chromedriver='/usr/bin/chromedriver' 
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920x1080")
            browser = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
            browser.get(url)
            self.soup = BeautifulSoup(browser.page_source, features='html.parser')
            return self.soup
        except Exception as e:
            log.error(utils.except_raise(e))
        finally:
            browser.quit()

    def tomorrow_weather(self, city_name):
        weather_info = self.get_weather(city_name)
        data = {}
        for element in weather_info:
            element_name = element["elementName"]
            if element_name == 'MinT' or element_name == 'CI':
                continue
            log.info(f"{element_name}:")
            for time_data in element["time"]:
                start_time = time_data["startTime"]
                end_time = time_data["endTime"]
                parameter = time_data["parameter"]
                parameter_name = parameter["parameterName"]
                if "{0} - {1}".format(start_time, end_time) in data:
                    data["{0} - {1}".format(start_time, end_time)][element_name] = parameter_name
                else:
                    data["{0} - {1}".format(start_time, end_time)] = {element_name:parameter_name}
                log.info(f"  {start_time} - {end_time}: {parameter_name}")

        log.info(data)
        result = ''
        for k, v in data.items():
            start_time, end_time = k.split(" - ")
            start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            end_datetime = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            formatted_start_time = start_datetime.strftime("%m/%d %H:%M")
            formatted_end_time = end_datetime.strftime("%m/%d %H:%M")

            result += "{0} - {1}: \n{2} , {3}°C, 降雨: {4}% \n\n".format(formatted_start_time, formatted_end_time, v['Wx'], v['MaxT'], v['PoP'])
        log.info(result)
        return result

    def getBnbRoomStatus(self, bnbNameList, bnbUrlList):
        resultList=[]
        i=0
        for bnbUrl in bnbUrlList:
            resultStr=''
            resultStr += str(bnbNameList[i]) + "\n"
            i+=1
            response = requests.get(bnbUrl)
            if response.status_code == 200:
                bnbStrList=str(response.text).split("\n")
                for bnbStr in reversed(bnbStrList):
                    regResult=re.search(r"^(SUMMARY:){1}(.*)$",bnbStr)
                    if regResult != None:
                        resultStr += regResult.group(2) + '\n'
                    regResult=re.search(r"^(DTSTART;VALUE=DATE:){1}(.*)$",bnbStr)
                    if regResult != None:
                        resultStr += '開始:' + regResult.group(2) + '\n'
                    regResult=re.search(r"^(DTEND;VALUE=DATE:){1}(.*)$",bnbStr)
                    if regResult != None:
                        resultStr += '結束:'+ regResult.group(2) + '\n'
            resultList.append(resultStr)
        return resultList
    
    def getDbData(self):
        data=[]
        try:
            conn = pymysql.Connect(host=const.DB_HOST,user=const.DB_ACCOUNT,passwd=const.DB_PASSWORD,db=const.DB_DB,charset='utf8')
            data = dao.Database(conn).queryAirBnb(1)
            log.info(len(data))
            result = json.loads(data[0][1])
            log.info(result)
            if len(data) == 1:
                data=result
        except Exception as e:
            log.info("query_airbnb occured some error: " + utils.except_raise(e))
        finally:
            try:
                conn.close()
            except Exception as e:
                log.info("close connection error: " + utils.except_raise(e))

        bnbNameList=[]
        bnbUrlList=[]
        for i in data:
            bnbNameList.append(i.get('room_name'))
            bnbUrlList.append(i.get('room_url'))

        return bnbNameList,bnbUrlList

    def get_weather(self, city_name):
        # url = f"https://www.cwa.gov.tw/V8/C/W/County/County.html?CID="
        try:
            date_str = datetime.datetime.today().strftime("%Y%m%d")
            url = "https://www.cwa.gov.tw/V8/C/W/County/MOD/Week/{cid}_Week_m.html?T={date}01-5".format(cid=city_name, date=date_str)
            log.info(url)
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                weather_data = []
                panels = soup.find_all('div', class_='panel panel-default')
                for panel in panels:
                    date_section = panel.find('span', class_='date')
                    day = date_section.find('span', class_='daily').text
                    date = date_section.find_all('span')[1].text
                    full_date = f"{date}  {day}"

                    day_weather = panel.find('span', class_='Day')
                    morning_weather = day_weather.find('img')['alt']
                    morning_temp = day_weather.find('span', class_='tem-C is-active').text.strip()

                    night_weather = panel.find('span', class_='Night')
                    night_weather_text = night_weather.find('img')['alt']
                    night_temp = night_weather.find('span', class_='tem-C is-active').text.strip()

                    weather_data.append({
                        "date": full_date,
                        "morning": morning_weather,
                        "night": night_weather_text,
                        "morning-temp": morning_temp,
                        "night-temp": night_temp,
                    })

                return weather_data
            else:
                return "Failed to fetch weather data."
        except Exception as e:
            return "error" + str(e)
