# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: weather.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'weather.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rweather.proto\x12\x07weather\"!\n\x0eWeatherRequest\x12\x0f\n\x07\x63ountry\x18\x01 \x01(\t\"X\n\x0fWeatherResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12$\n\x06result\x18\x03 \x03(\x0b\x32\x14.weather.WeatherData\"e\n\x0bWeatherData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07morning\x18\x02 \x01(\t\x12\r\n\x05night\x18\x03 \x01(\t\x12\x14\n\x0cmorning_temp\x18\x04 \x01(\t\x12\x12\n\nnight_temp\x18\x05 \x01(\t2Q\n\x0eWeatherService\x12?\n\nGetWeather\x12\x17.weather.WeatherRequest\x1a\x18.weather.WeatherResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'weather_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WEATHERREQUEST']._serialized_start=26
  _globals['_WEATHERREQUEST']._serialized_end=59
  _globals['_WEATHERRESPONSE']._serialized_start=61
  _globals['_WEATHERRESPONSE']._serialized_end=149
  _globals['_WEATHERDATA']._serialized_start=151
  _globals['_WEATHERDATA']._serialized_end=252
  _globals['_WEATHERSERVICE']._serialized_start=254
  _globals['_WEATHERSERVICE']._serialized_end=335
# @@protoc_insertion_point(module_scope)
