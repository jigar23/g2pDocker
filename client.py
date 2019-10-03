import grpc

import g2p_pb2_grpc
import g2p_pb2

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub object
stub = g2p_pb2_grpc.g2pStub(channel)

# create a request with word
word = g2p_pb2.Word(word='JIGAR')

prons = stub.g2p(word)

print(prons.pron)
