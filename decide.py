import socket
from cacheparser import CacheParser


def decide(cache, server):
    global sock
    while 1:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(("127.0.0.1", 53))
            data, addr = sock.recvfrom(512)
            if not data:
                break

            parsed_data = CacheParser.parse_from(data)
            cached = cache.read_cache(parsed_data)
            if cached is None:
                returned_data = get_recv(server, data)
                caching_data = CacheParser.parse_from(returned_data)
                cache.cache(caching_data)
            else:
                returned_data = CacheParser.parse_to(parsed_data, cached)

            sock.sendto(returned_data, addr)
        finally:
            sock.close()
            cache.set_cache()


def get_recv(server, data):
    socks = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socks.bind(("", 0))
    socks.sendto(data, (server, 53))
    return socks.recvfrom(512)[0]
