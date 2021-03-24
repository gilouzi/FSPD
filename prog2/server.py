from concurrent import futures
import grpc
import sys
import services_pb2, services_pb2_grpc

services_dict = dict()
class DoStuff(services_pb2_grpc.DoStuffServicer):
    def __init__(self, txt):
        self.services_dict = dict()
        with open(txt, 'r') as f:
            arq = f.read().splitlines()

        for line in arq:
            if line != '' and line[0] != '#':
                line = line.split('/')
                service, port = line[0].split()
                description = line[1]
                description = description.split('#')
                comments = None
                if len(description) > 1:
                    comments = description[1]
                description = description[0]
                description = description.split()
                
                if service not in services_dict.keys():
                    services_dict[service] = {'port': int(port), 'protocol': description[0]}
                    
                    if len(description) > 1:
                        services_dict[service]['aliases'] = ', '.join(description[1:])
                    else:
                        services_dict[service]['aliases'] = ''

                    if comments:
                        services_dict[service]['comments'] = comments
                    else:
                        services_dict[service]['comments'] = ''
                        
    def get_service_port(self, request, context):
        service_port = services_dict[request.name]['port'] if request.name in services_dict.keys() else -1
        print("client adress =", str(context.peer()), 
                ",command called = get_service_port ",
                ", service name =", request.name, 
                ", port =", str(service_port))
        return services_pb2.ServicePort(port=service_port)
    
    def get_service_description(self, request, context):
        if request.name in services_dict.keys():
            print("client adress =", str(context.peer()), 
                    ", command called = get_service_description ",
                    ", service name =", request.name, 
                    ", protocol =", services_dict[request.name]['protocol'],
                    ", aliases =", services_dict[request.name]['aliases'],
                    ", comments =", services_dict[request.name]['comments'])
            return services_pb2.ServiceDescription(protocol=services_dict[request.name]['protocol'], 
                                                aliases=services_dict[request.name]['aliases'],
                                                comments=services_dict[request.name]['comments'])
        else:
            print("client adress =", str(context.peer()), 
                    ", command called = get_service_description ",
                    ", service name =", request.name, 
                    "not found")
            return services_pb2.ServiceDescription(protocol='',aliases='',comments='')

def serve():
    print(sys.argv)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_DoStuffServicer_to_server(DoStuff(sys.argv[2]), server)
    server.add_insecure_port('0.0.0.0:' + sys.argv[1])

    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()