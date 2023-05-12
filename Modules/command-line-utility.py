import argparse
import requests


def download_file(url, local_file_name):
    if local_file_name is None:
        local_file_name = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_file_name


parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")

#Optional argument
parser.add_argument("-o", "--output", help="Name of the file", default=None)


# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output)

download_file(args.url, args.output)


# To run this code, go to terminal and run
# python3 command-line-utility.py https://imagej.net/images/2D_Gel.jpg -o sambit.jpg