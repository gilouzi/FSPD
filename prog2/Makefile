# Signifies our desired python version
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.
PYTHON = python3

# This generates the desired project file structure
# A very important thing to note is that macros (or makefile variables) are referenced in the target's code with a single dollar sign ${}, but all script variables are referenced with two dollar signs $${}
setup:
	
	@echo "Updating pb2 files..."
	${PYTHON} -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. services.proto

# The ${} notation is specific to the make syntax and is very similar to bash's $() 
run_server:setup
	${PYTHON} server.py $(arg1) $(arg2)

run_client:setup
	${PYTHON} client.py $(arg1) $(arg2)