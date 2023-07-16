import argparse
import requests


def download_file(url, local_filename):
    # If the local_filename is not provided, extract it from the URL
    if local_filename is None:
        local_filename = url.split('/')[-1]

    # Download the file using requests library
    with requests.get(url, stream=True) as r:
        # Check if the request was successful
        r.raise_for_status()

        # Open the file in binary mode for writing
        with open(local_filename, 'wb') as f:
            # Iterate over the response content in chunks and write them to the file
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    # Return the local filename of the downloaded file
    return local_filename


# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Define a positional argument for the URL
parser.add_argument("url", help="URL of the file to download")

# Define an optional argument for the output filename
parser.add_argument("-o", "--output", type=str,help="Name of the file", default=None)

# Parse the command-line arguments
args = parser.parse_args()

# Print the provided URL
print(args.url)

# Print the output filename (if provided)
print(args.output, type(args.output))

# Call the download_file function with the provided URL and output filename
download_file(args.url, args.output)
