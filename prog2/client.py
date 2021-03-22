from __future__ import print_function
import os
import grpc
import sys
import hello_pb2, hello_pb2_grpc

def run():
    ip_adress = sys.argv[1]
    service_name = sys.argv[2]

    channel = grpc.insecure_channel(ip_adress)
    stub = hello_pb2_grpc.DoStuffStub(channel)

    my_pid = os.getpid()

    response = stub.say_hello(hello_pb2.HelloRequest(pid=my_pid))
    print("GRPC client received: " + response.retval)

    response = stub.say_hello_again(hello_pb2.HelloRequest(pid=my_pid))
    print("GRPC client received: " + response.retval)

    response = stub.get_service_port(hello_pb2.ServiceName(name=service_name))
    print("GRPC client received: " + str(response.port))

    response = stub.get_service_description(hello_pb2.ServiceName(name=service_name))
    print("GRPC client received: " + response.description)

    channel.close()

if __name__ == '__main__':
    run()