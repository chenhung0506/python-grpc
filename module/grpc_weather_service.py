import grpc
import utils
import weather_pb2
import weather_pb2_grpc
from concurrent import futures
import datetime
import requests
from bs4 import BeautifulSoup
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("WeatherService")

class WeatherService(weather_pb2_grpc.WeatherServiceServicer):
    def GetWeather(self, request, context):
        log.info("GetWeather gRPC API start")
        country = request.country if request.country else '65'
        weather_data = self.get_weather(country)
        
        return weather_pb2.WeatherResponse(
            status=200,
            message='success',
            result=weather_data
        )
    
    def get_weather(self, city_name):
        try:
            date_str = datetime.datetime.today().strftime("%Y%m%d")
            url = f"https://www.cwa.gov.tw/V8/C/W/County/MOD/Week/{city_name}_Week_m.html?T={date_str}01-5"
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
                    
                    weather_data.append(weather_pb2.WeatherData(
                        date=full_date,
                        morning=morning_weather,
                        night=night_weather_text,
                        morning_temp=morning_temp,
                        night_temp=night_temp
                    ))
                return weather_data
            else:
                return []
        except Exception as e:
            log.error("Error fetching weather data: %s", str(e))
            return []


def serve():
    sched = BackgroundScheduler()
    sched.add_job(utils.setLogFileName, CronTrigger.from_crontab('0 0 * * *'))
    sched.start()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port('[::]:50051')
    log.info("Starting Weather gRPC server on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
