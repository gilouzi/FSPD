PYTHON = python3

setup:
	@echo "Updating pb2 files..."
	${PYTHON} -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. services.proto
	
run_server:setup
	${PYTHON} server.py $(arg1) $(arg2)

run_client:setup
	${PYTHON} client.py $(arg1) $(arg2)