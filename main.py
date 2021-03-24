import sys

# with open(argv[1], 'r') as f:
#     arq = f.read().splitlines()

# line = arq[11]
# print(line)

# line = line.split('/')
# cmd, port = line[0].split()
# comment = line[1]

# print(cmd, '-', port, '-', comment)

# python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto 

services_dict = dict()
with open(sys.argv[1], 'r') as f:
        arq = f.read().splitlines()

for line in arq:
    if line != '' and line[0] != '#':
        line = line.split('/')
        service, port = line[0].split()
        description = line[1]
        description = description.split('#')
        comment = None
        if len(description) > 1:
            comment = description[1]

        description = description[0]
        description = description.split()
        
        if service not in services_dict.keys():
            services_dict[service] = {'port': int(port), 'protocol': description[0]}
            if len(description) > 1:
                services_dict[service]['aliases'] = description[1:]
            if comment:
                services_dict[service]['comment'] = comment
            print(services_dict[service])