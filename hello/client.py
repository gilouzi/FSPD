from __future__ import print_function
import os
import grpc
import hello_pb2, hello_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:8888')
    stub = hello_pb2_grpc.DoStuffStub(channel)

    my_pid = os.getpid()

    response = stub.say_hello(hello_pb2.HelloRequest(pid=my_pid))
    print("GRPC client received: " + response.retval)

    response = stub.say_hello_again(hello_pb2.HelloRequest(pid=my_pid))
    print("GRPC client received: " + response.retval)

    channel.close()

if __name__ == '__main__':
    run()