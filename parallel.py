from webCrawler import crawl_and_extract
from multiprocessing import Pool
import pandas as pd
import time

def scrape_parallel(args):
    url, depth, max_sublinks = args
    result = crawl_and_extract(url, depth, max_sublinks)
    return result

def crawl_websites(file_path, depth=1, max_sublinks=20, num_processes=4, num_urls=-1):
    start_time = time.time()

    df = pd.read_csv(file_path)
    url_list = df['Website'].tolist()

    if num_urls > 0: 
        url_list = url_list[:num_urls]

    args = [(url, depth, max_sublinks) for url in url_list]

    with Pool(num_processes) as pool:
        results = pool.map(scrape_parallel, args)

    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Number of results: {len(results)}")

    return results