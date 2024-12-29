from webCrawler import crawl_and_extract
from multiprocessing import Pool
import pandas as pd
import utils.countUtils as cu


def scrape_parallel(args):
    url, depth, max_sublinks = args
    result = crawl_and_extract(url, depth, max_sublinks)
    return result




def crawl_websites(websites, depth=1, max_sublinks=20, num_processes=4):
    """
    Parallel crawling function that accepts a list of URLs instead of reading from CSV.
    
    :param websites: list of URLs to crawl
    :param depth: how deep to follow sublinks
    :param max_sublinks: max number of sublinks to crawl
    :param num_processes: number of processes in the multiprocessing pool
    :return: list of results (each result is likely whatever crawl_and_extract returns)
    """


    # Prepare args for parallel processing
    args = [(url, depth, max_sublinks) for url in websites]

    # Run in parallel
    with Pool(num_processes) as pool:
        results = pool.map(scrape_parallel, args)


    # dicto = {results[i][0] : cu.list_to_count(results[i][1]) for i in range(len(results))}
    dicto = {"urls" :  [results[i][0] for i in range(len(results))]   ,   "keywords" : [cu.list_to_count(results[i][1]) for i in range(len(results))]}
    df =  pd.DataFrame.from_dict(dicto)
    print(df)
    res = [results[i][1] for i in range(len(results))]
    df.to_csv("static/output.csv", index=False)
    print(f"Results saved to output.csv ")

    return res,df
 