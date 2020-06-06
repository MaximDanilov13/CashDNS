import argparse
import cache
import decide

parser = argparse.ArgumentParser(description='Enter a server')
parser.add_argument('-s', '--server', help='Server')
server_name = parser.parse_args().server


def main():
    if server_name is not None:
        server = server_name
    else:
        server = input()
    new_cache = cache.Cache()
    while KeyboardInterrupt:
        try:
            new_cache.get_cache()
            decide.decide(new_cache, server)
        except Exception:
            pass


if __name__ == "__main__":
    main()
