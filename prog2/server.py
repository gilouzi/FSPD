from concurrent import futures
import grpc
import sys
import services_pb2, services_pb2_grpc

services_dict = dict()
class DoStuff(services_pb2_grpc.DoStuffServicer):

    def say_hello(self, request, context):
        print("GRPC server in say_hello, pid =", str(request.pid))
        return services_pb2.HelloReply(retval='Hello, %s!' % str(request.pid))
    
    def say_hello_again(self, request, context):
        print("GRPC server in say_hello_again, pid =", str(request.pid))
        return services_pb2.HelloReply(retval='Hello again, %s!' % str(request.pid))

    def get_service_port(self, request, context):
        print(1)
        service_port = services_dict[request.serviceName]['port'] if request.service_name in services_dict.keys() else -1
        print(2)
        print("GRPC server in get_service_port, adress =", str(context.peer()), "service name =", str(request.serviceName), "port =", services_port)
        print(3)
        return services_pb2.ServicePort(port=service_port)
    
    def get_service_description(self, request, context):
        service_description = services_dict[request.serviceName]['description'] if request.service_name in services_dict.keys() else -1
        print("GRPC server in get_service_port, adress =", str(context.peer()), "service name =", str(request.serviceName), "description =", service_description)
        return services_pb2.ServiceDescription(description=service_description)

def serve():
    port = sys.argv[1]
    with open(sys.argv[2], 'r') as f:
        arq = f.read().splitlines()

    for line in arq:
        if line[0] != '#':
            line = line.split('/')
            print(line)
            service, port = line[0].split()
            description = line[1]
            services_dict[service] = {'port': port, 'description': description}

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_DoStuffServicer_to_server(DoStuff(), server)
    server.add_insecure_port('localhost:8888')
    # server.add_insecure_port('localhost:'+str(port))

    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()