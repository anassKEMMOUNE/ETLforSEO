from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

# nltk.download('stopwords')



useless_tags =  ["script","style","img","svg" ,"noscript" ,"iframe","object","embed","applet","form","textarea","button","input","select","option","link","meta","figure","figcaption"]
stop_words = set(stopwords.words('english'))


def decomp(soup : BeautifulSoup , tags = []) : 
    """Function to search for useless HTML tags, remove them with their content """
    for tag in tags : 
        searched_tags = soup.find_all(tag)
        for searched_tag in searched_tags : 
                searched_tag.decompose()

      

def cleanHTML(soup : BeautifulSoup) :
    """Function to clean the HTML input"""

    decomp(soup)
    soup.get_text(strip=True)
    soup.prettify()

    res = soup.text.strip()
    res = res.split(" ")
    res  = [i for i in res if i != ""]
    filtered_list = [   
    s.lower().strip()
    for s in res
    if re.match(r'^[a-zA-Z]+$', s.strip())  
    and len(s.strip()) > 1                 
    and s.strip().lower() not in stop_words  
]
    
    # res = " ".join(res)
    return filtered_list

    


