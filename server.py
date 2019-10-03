import grpc
from concurrent import futures
import time

# import the generated classes
import g2p_pb2
import g2p_pb2_grpc

import g2pFunction

class g2pServicer(g2p_pb2_grpc.g2pServicer):
    def g2p(self, request, context):
        response = g2p_pb2.Prons()
        prons = g2pFunction.getG2P(request.word)
        response.pron.extend(list(prons))
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

g2p_pb2_grpc.add_g2pServicer_to_server(g2pServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
