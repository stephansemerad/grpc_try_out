
python -m pip install --upgrade pip
python -m pip install virtualenv
virtualenv venv


# Linux 
source venv/bin/activate

# Windows 
cd venv/Scripts
activate


# Install GRPC
python -m pip install --upgrade pip
python -m pip install grpcio
python -m pip install grpcio-tools
python -m pip install autopep8

# After creating pingpong.proto
# Compile proto file 

python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/pingpong.proto 





#tensorflow 2.4.0 requires grpcio~=1.32.0, but you have grpcio 1.37.0 which is incompatible.
