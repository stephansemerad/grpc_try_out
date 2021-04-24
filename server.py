from concurrent import futures  # running threadpool executer
import grpc
import pingpong_pb2
import pingpong_pb2_grpc
import time
import threading


class Listener(pingpong_pb2_grpc.PingPongServiceServicer):
    def __init__(self, *args, **kwargs):
        self.counter = 0
        self.lastPrintTime = time.time()

    # rpc ping (Ping) returns (Pong) {}
    def ping(self, request, context):
        self.counter += 1
        if(self.counter > 10000):
            print("10000 calls in %3f seconds" %
                  (time.time() - self.lastPrintTime))
            print('{}')
            self.lastPrintTime = time.time()
            self.counter = 0

        return pingpong_pb2.Pong(count=request.count + 1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
    pingpong_pb2_grpc.add_PingPongServiceServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("server on: threads %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    serve()
