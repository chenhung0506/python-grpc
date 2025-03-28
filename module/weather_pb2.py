# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weather.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rweather.proto\x12\x07weather\"!\n\x0eWeatherRequest\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\"X\n\x0fWeatherResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12$\n\x06result\x18\x03 \x03(\x0b\x32\x14.weather.WeatherData\"e\n\x0bWeatherData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07morning\x18\x02 \x01(\t\x12\r\n\x05night\x18\x03 \x01(\t\x12\x14\n\x0cmorning_temp\x18\x04 \x01(\t\x12\x12\n\nnight_temp\x18\x05 \x01(\t2Q\n\x0eWeatherService\x12?\n\nGetWeather\x12\x17.weather.WeatherRequest\x1a\x18.weather.WeatherResponseb\x06proto3')



_WEATHERREQUEST = DESCRIPTOR.message_types_by_name['WeatherRequest']
_WEATHERRESPONSE = DESCRIPTOR.message_types_by_name['WeatherResponse']
_WEATHERDATA = DESCRIPTOR.message_types_by_name['WeatherData']
WeatherRequest = _reflection.GeneratedProtocolMessageType('WeatherRequest', (_message.Message,), {
  'DESCRIPTOR' : _WEATHERREQUEST,
  '__module__' : 'weather_pb2'
  # @@protoc_insertion_point(class_scope:weather.WeatherRequest)
  })
_sym_db.RegisterMessage(WeatherRequest)

WeatherResponse = _reflection.GeneratedProtocolMessageType('WeatherResponse', (_message.Message,), {
  'DESCRIPTOR' : _WEATHERRESPONSE,
  '__module__' : 'weather_pb2'
  # @@protoc_insertion_point(class_scope:weather.WeatherResponse)
  })
_sym_db.RegisterMessage(WeatherResponse)

WeatherData = _reflection.GeneratedProtocolMessageType('WeatherData', (_message.Message,), {
  'DESCRIPTOR' : _WEATHERDATA,
  '__module__' : 'weather_pb2'
  # @@protoc_insertion_point(class_scope:weather.WeatherData)
  })
_sym_db.RegisterMessage(WeatherData)

_WEATHERSERVICE = DESCRIPTOR.services_by_name['WeatherService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WEATHERREQUEST._serialized_start=26
  _WEATHERREQUEST._serialized_end=59
  _WEATHERRESPONSE._serialized_start=61
  _WEATHERRESPONSE._serialized_end=149
  _WEATHERDATA._serialized_start=151
  _WEATHERDATA._serialized_end=252
  _WEATHERSERVICE._serialized_start=254
  _WEATHERSERVICE._serialized_end=335
# @@protoc_insertion_point(module_scope)
