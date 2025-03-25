FROM chenhung0506/python-with-chrome:latest
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV TZ=Asia/Taipei
RUN pip install redis
ADD module /usr/src/app
RUN ls /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r /usr/src/app/requirements.txt
CMD ["python", "grpc_weather_service.py"]
