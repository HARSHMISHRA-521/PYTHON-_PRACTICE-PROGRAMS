import argparse
import requests


def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)


#
# This is a Python code that defines a function to download a file from a given URL
# using the requests module. The code also includes command-line
# arguments parsing using the argparse module to allow the user to specify the URL to
# download and the local file name to save the downloaded file.
#
# Here is a step-by-step breakdown of the code:
#
# The argparse module is imported to parse command-line arguments.
# The requests module is imported to handle HTTP requests.
# The download_file() function is defined that takes two arguments: the URL of the file to download and the
# local filename to save the downloaded file. If the local_filename argument
# is not provided, it is set to the last part of the URL.
# The requests.get() method is used to retrieve the file from the specified URL. The stream=True parameter is used
# to download the file in chunks rather than all at once, which can save memory.
# The r.raise_for_status() method is called to check for any errors that occurred during the download process.
# The downloaded data is written to a file using the open() function with the wb mode. The data is written to the
# file in chunks using the iter_content() method.
# The download_file() function returns the local filename of the downloaded file.
# The argparse.ArgumentParser() method is called to create an ArgumentParser object to parse command-line arguments.
# The add_argument() method is used to add two arguments: the URL of the file to download (required) and the local
# filename to save the downloaded file (optional).
# The parse_args() method is called to parse the command-line arguments provided by the user.
# The args.url and args.output variables are used to access the values of the command-line
# arguments provided by the user.
# The download_file() function is called with the URL and output filename to download the file
# and save it to the local file system.
# To run this code, save it as a Python script (e.g., file_downloader.py) and run it from the command
# line, passing in the URL of the file to download as a required argument and optionally specifying
# the local filename to save the downloaded file using the -o or --output