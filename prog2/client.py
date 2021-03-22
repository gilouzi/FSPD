from __future__ import print_function
import os
import grpc
import sys
import services_pb2, services_pb2_grpc

def run():
    ip_adress = sys.argv[1]
    service_name = sys.argv[2]
    print(service_name)

    # channel = grpc.insecure_channel(ip_adress)
    channel = grpc.insecure_channel(ip_adress)
    stub = services_pb2_grpc.DoStuffStub(channel)

    response = stub.get_service_port(services_pb2.ServiceName(name=service_name))
    print("GRPC client received: " + str(response.port))

    response = stub.get_service_description(services_pb2.ServiceName(name=service_name))
    print("GRPC client received: " + response.description)

    channel.close()

if __name__ == '__main__':
    run()