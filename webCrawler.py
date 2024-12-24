import requests 
from bs4 import BeautifulSoup
from cleanHTML import cleanHTML

class Link:

    _instances = {}

    def __new__(cls, url, visited=False):

        if url in cls._instances:
            return cls._instances[url]

        instance = super().__new__(cls)
        cls._instances[url] = instance
        return instance

    def __init__(self, url, visited=False):
        if not hasattr(self, 'url'):
            self.url = url
            self.visited = visited
          

def crawl_and_extract(link : str , depth = 1 , max_websites = 20) : 
    """ Function to extract all sub pages of the given page"""
    initial_link =  Link(link )
    keywords = []
    urls = [initial_link]
    accessible = 0


    for _ in range(depth) : 
        for l in urls : 

            if l.visited == False : 
                try :
                    response = requests.get(l.url)
                    
                    l.visited = True
                    if response.status_code == 200 :
                        accessible+=1
                        # print("Getting URL : " + l.url)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        link_elements = soup.select("a[href]")


                        for link_element in link_elements:
                            url = link_element['href']
                            if len(url) == 0 or url == " " :
                                continue
                            
                            elif l.url in url :
                                if "http" in url[0:6] : 
                                    urls.append(Link(url)) 
                            elif url[0] == "/"  :
                                if "http" in (initial_link.url + url)[0:6] :
                                    urls.append(Link(initial_link.url + url))

                        urls =  list(set(urls))
                        
                        keywords.extend(cleanHTML(soup)) 
                        if accessible > max_websites :
                            return keywords
                        
                    else  :
                        if accessible == 0 and "https" not in l.url:
                            
                            initial_link = Link(link.replace("http","https"))
                            urls = [initial_link]
                        
                        # print(l.url + '  '+ "Page not accessible" )
                except :
                    print("Website not available")
                    continue
    return keywords

        

  