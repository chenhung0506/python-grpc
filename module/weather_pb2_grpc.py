# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import weather_pb2 as weather__pb2


class WeatherServiceStub(object):
    """定義 WeatherService 服務
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetWeather = channel.unary_unary(
                '/weather.WeatherService/GetWeather',
                request_serializer=weather__pb2.WeatherRequest.SerializeToString,
                response_deserializer=weather__pb2.WeatherResponse.FromString,
                )


class WeatherServiceServicer(object):
    """定義 WeatherService 服務
    """

    def GetWeather(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WeatherServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetWeather': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWeather,
                    request_deserializer=weather__pb2.WeatherRequest.FromString,
                    response_serializer=weather__pb2.WeatherResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weather.WeatherService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WeatherService(object):
    """定義 WeatherService 服務
    """

    @staticmethod
    def GetWeather(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weather.WeatherService/GetWeather',
            weather__pb2.WeatherRequest.SerializeToString,
            weather__pb2.WeatherResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
