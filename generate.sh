python -m grpc_tools.protoc -I. --python_out=./friend_service --grpc_python_out=./friend_service friend_service.proto