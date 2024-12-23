from webCrawler import crawl_and_extract
from multiprocessing import Pool
import pandas as pd
import time


# It returned nan (key error in dictionary ( when it arrived to 944))
start_time =  time.time()
df = pd.read_csv('companies-11-27-2024.csv')
url_list = df['Website'].tolist()

# dicto =  {url_list[i] : i for i in range(len(url_list))}


url_list2 =  url_list[:8]


def scrape_parallel(url):

    print(url,'loaded')
    result = crawl_and_extract(url)
    if len(result) == 0 : 
        print(url,'NOT ACCESSIBLE')
    else : 
        print(url,'SCRAPED')

    return result

num_processes = 4


with Pool(num_processes) as pool:
    results = pool.map(scrape_parallel, url_list2)


    
print(len(results))

end_time = time.time()
# # Displaying results
# for result in results:
#     if result:
#         print(result)

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")