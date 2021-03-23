from sys import argv

with open(argv[1], 'r') as f:
    arq = f.read().splitlines()

line = arq[11]
print(line)

line = line.split('/')
cmd, port = line[0].split()
comment = line[1]

print(cmd, '-', port, '-', comment)

# python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto 