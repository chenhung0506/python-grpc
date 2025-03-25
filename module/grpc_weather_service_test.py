import grpc
import weather_pb2
import weather_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = weather_pb2_grpc.WeatherServiceStub(channel)
    
    country = input("Enter country code: ")
    request = weather_pb2.WeatherRequest(country=country)
    response = stub.GetWeather(request)
    
    print(f"Status: {response.status}")
    print(f"Message: {response.message}")
    
    for weather in response.result:
        print(f"Date: {weather.date}, Morning: {weather.morning}, Night: {weather.night}, Morning Temp: {weather.morning_temp}, Night Temp: {weather.night_temp}")

if __name__ == "__main__":
    run()
