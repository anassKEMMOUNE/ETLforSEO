import requests
from cleanHTML import cleanHTML
r = requests.get("https://medium.com/@siladityaghosh/web-scraping-with-python-parallizing-and-scaling-with-spark-b7d2166602b7")

if r.status_code == 200 : 

    print(cleanHTML(r.text))

else  :
    print("Some Error has occured")