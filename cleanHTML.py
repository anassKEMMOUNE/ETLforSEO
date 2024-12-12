from bs4 import BeautifulSoup


useless_tags =  ["script","style","img","svg" ,"noscript" ,"iframe","object","embed","applet","form","textarea","button","input","select","option","link","meta","figure","figcaption"]

def decomp(soup : BeautifulSoup , tags = []) : 
         
    """Function to search for useless HTML tags, remove them with their content """
    for tag in tags : 
        searched_tags = soup.find_all(tag)
        for searched_tag in searched_tags : 
                searched_tag.decompose()

      

def cleanHTML(input) :

    """Function to clean the HTML input"""

    soup =  BeautifulSoup(input, 'html.parser')
    decomp(soup)
    soup.get_text(strip=True)
    soup.prettify()

    res = soup.text.strip()
    res = res.split(" ")
    res  = [i for i in res if i != ""]
    res = " ".join(res)
    return res

    


