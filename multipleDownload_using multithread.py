import requests
from concurrent.futures import ThreadPoolExecutor

def download_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        # Save or process the downloaded content as needed
        print(f"Downloaded {url}")
    else:
        print(f"Failed to download {url}")

def download_multiple_urls(urls, num_threads=5):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(download_url, urls)

# Example usage:
urls = [
    "https://example.com/file1.txt",
    "https://example.com/file2.txt",
    "https://example.com/file3.txt",
    "https://example.com/file4.txt",
    "https://example.com/file5.txt"
]

download_multiple_urls(urls)

#
# Explanation:
#
# The code imports the necessary libraries: requests for making HTTP requests and
# ThreadPoolExecutor from concurrent.futures for handling multithreading.

# The download_url function takes a URL as input and downloads its content using the requests.get method.

# If the response status code is 200 (indicating a successful request), the content is obtained from response.content.

# You can replace the # Save or process the downloaded content as needed comment with your own code to
# # handle the downloaded content (e.g., save it to a file or perform further processing).

# If the response status code is not 200, a failure message is printed.

# The download_multiple_urls function takes a list of URLs and the number of threads to use (default is 5).

# Inside this function, a ThreadPoolExecutor is created using the with statement, limiting the maximum number
# of workers to the specified num_threads.

# The executor.map method is used to concurrently execute the download_url function for each URL in the list.

# Finally, an example usage is shown, where a list of URLs is defined and download_multiple_urls is called to
# start the downloading process.