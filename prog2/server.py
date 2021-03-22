from concurrent import futures
import grpc
import sys
import services_pb2, services_pb2_grpc

services_dict = dict()
class DoStuff(services_pb2_grpc.DoStuffServicer):

    def get_service_port(self, request, context):
        service_port = services_dict[request.name]['port'] if request.name in services_dict.keys() else -1
        print("client adress =", str(context.peer()), 
                ",command called = get_service_port ",
                ",parameter =", request.name, 
                ",answer =", str(service_port))
        return services_pb2.ServicePort(port=service_port)
    
    def get_service_description(self, request, context):
        service_description = services_dict[request.name]['description'] if request.name in services_dict.keys() else ""
        print("client adress =", str(context.peer()), 
                ", command called = get_service_description ",
                ",parameter =", request.name, 
                ",answer =", service_description)
        return services_pb2.ServiceDescription(description=service_description)

def serve():
    port = sys.argv[1]
    with open(sys.argv[2], 'r') as f:
        arq = f.read().splitlines()

    for line in arq:
        if line != '' and line[0] != '#':
            line = line.split('/')
            service, port = line[0].split()
            description = line[1]
            if service not in services_dict.keys():
                services_dict[service] = {'port': int(port), 'description': description}

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_DoStuffServicer_to_server(DoStuff(), server)
    server.add_insecure_port('localhost:8888')
    # server.add_insecure_port('localhost:'+str(port))

    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()