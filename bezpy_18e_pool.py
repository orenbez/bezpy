import requests
from multiprocessing import Pool

def fetch_data(url):
    """
    Function to fetch data from a given URL.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def main():
    # List of URLs to scrape
    urls = [
        "https://example.com",
        "https://example.com",
        "https://example.com",
        "https://example.com",
        "https://example.com"
    ]

    # Number of concurrent processes
    num_processes = 5

    # Create a pool of processes
    with Pool(num_processes) as pool:
        # Fetch data from each URL concurrently
        results = pool.map(fetch_data, urls)

    # Process the results
    for idx, result in enumerate(results, start=1):
        if result:
            print(f"Data from URL {idx}:")
            print(result[:100])  # Print the first 100 characters of the fetched data
            print("-" * 50)
        else:
            print(f"Failed to fetch data from URL {idx}")

if __name__ == "__main__":
    main()