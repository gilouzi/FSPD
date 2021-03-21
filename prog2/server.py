from concurrent import futures
import grpc
import hello_pb2, hello_pb2_grpc

class DoStuff(hello_pb2_grpc.DoStuffServicer):

    def say_hello(self, request, context):
        print("GRPC server in say_hello, pid =", str(request.pid))
        return hello_pb2.HelloReply(retval='Hello, %s!' % str(request.pid))
    
    def say_hello_again(self, request, context):
        print("GRPC server in say_hello_again, pid =", str(request.pid))
        return hello_pb2.HelloReply(retval='Hello again, %s!' % str(request.pid))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_DoStuffServicer_to_server(DoStuff(), server)
    server.add_insecure_port('localhost:8888')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()