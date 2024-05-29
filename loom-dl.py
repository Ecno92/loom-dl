#!/usr/bin/python3

import argparse
import json
import urllib.request
from tqdm import tqdm

def fetch_loom_download_url(id):
    request = urllib.request.Request(
        url=f"https://www.loom.com/api/campaigns/sessions/{id}/transcoded-url",
        headers={},
        method="POST",
    )
    response = urllib.request.urlopen(request)
    body = response.read()
    content = json.loads(body.decode("utf-8"))
    url = content["url"]
    return url

def download_loom_video(url, filename):
    # Fetch the size of the file to be downloaded
    response = urllib.request.urlopen(url)
    total_size = int(response.headers.get('Content-Length').strip())
    
    # Start downloading the file with progress bar
    with open(filename, 'wb') as f:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as pbar:
            block_size = 1024  # 1 Kibibyte
            while True:
                buffer = response.read(block_size)
                if not buffer:
                    break
                f.write(buffer)
                pbar.update(len(buffer))

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="loom-dl", description="script to download loom.com videos"
    )
    parser.add_argument(
        "url", help="Url of the video in the format https://www.loom.com/share/[ID]"
    )
    parser.add_argument("-o", "--out", help="Path to output the file to")
    arguments = parser.parse_args()
    return arguments

def extract_id(url):
    return url.split("/")[-1]

def main():
    arguments = parse_arguments()
    id = extract_id(arguments.url)

    url = fetch_loom_download_url(id)
    filename = arguments.out or f"{id}.mp4"
    print(f"Downloading video {id} and saving to {filename}")
    download_loom_video(url, filename)

if __name__ == "__main__":
    main()
