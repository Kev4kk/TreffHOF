import requests
from bs4 import BeautifulSoup
import re
import json

kaust = "infolehed4"
urlObject = {}

aasta = 14
# URL of the website to scrape
url = f'https://www.htg.tartu.ee/Infolehed{aasta}'

aastastr = "20" + str(aasta)
print(aastastr)
# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object with the website's HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all anchor tags ('a') in the HTML
anchor_tags = soup.find_all('a')

i = 0
# Extract and print the href attribute of each anchor tag
for tag in anchor_tags:
    href = tag.get('href')
    if href and "infoleht" in href and ".html" in href:
        # print(href)

        nodeUrl = f"{href}"
        
        nodeResp = requests.get(nodeUrl) 

        html_str = nodeResp.content.decode("windows-1257", errors="ignore")
        urlObject[f"{kaust}/{aastastr}_{i}.txt"] = href
        # print(html_str)
        num = href.split("/")[-1]
        splitted = html_str
        f = open(f"{kaust}/{aastastr}_{i}.txt", "w")
        f.write(splitted)
        f.close()
        i+=1


for aasta in range(15, 22):
    # URL of the website to scrape
    url = f'https://www.htg.tartu.ee/Infolehed{aasta}'

    aastastr = "20" + str(aasta)
    print(aastastr)
    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object with the website's HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags ('a') in the HTML
    anchor_tags = soup.find_all('a')

    i = 0
    # Extract and print the href attribute of each anchor tag
    for tag in anchor_tags:
        href = tag.get('href')
        if href and "node" in href:
            # print(href)

            nodeUrl = f"https://www.htg.tartu.ee{href}"

            nodeResp = requests.get(nodeUrl) 

            html_str = nodeResp.content.decode("utf-8")
            urlObject[f"{kaust}/{aastastr}_{i}.txt"] = nodeUrl
            # print(html_str)
            num = href.split("/")[-1]
            splitted = html_str.split('<div class="field-items">', 1)[1].split('<aside id="sidebar-second" role="complementary">', 1)[0]
            f = open(f"{kaust}/{aastastr}_{i}.txt", "w")
            f.write(splitted)
            f.close()
            i+=1

# 2023 
url = "https://www.htg.tartu.ee/Infolehed"
response = requests.get(url)
print("2023")
# Create a BeautifulSoup object with the website's HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all anchor tags ('a') in the HTML
anchor_tags = soup.find_all('a')

i = 0
# Extract and print the href attribute of each anchor tag
for tag in anchor_tags:
    href = tag.get('href')
    if href and "node" in href:
        # print(href)

        nodeUrl = f"https://www.htg.tartu.ee{href}"

        nodeResp = requests.get(nodeUrl) 

        html_str = nodeResp.content.decode("utf-8")
        urlObject[f"{kaust}/2023_{i}.txt"] = nodeUrl
        # print(html_str)
        num = href.split("/")[-1]
        splitted = html_str.split('<div class="field-items">', 1)[1].split('<aside id="sidebar-second" role="complementary">', 1)[0]
        f = open(f"{kaust}/2023_{i}.txt", "w")
        f.write(splitted)
        f.close()
        i += 1

# 2002 - 2013
for aasta in range(2, 14):
    if (aasta < 10):
        aastastr = "0" + str(aasta)
    else:
        aastastr = str(aasta)
    uusAastStr = "20" + aastastr    
    print("20" + aastastr)

    url = f"http://www.htg.tartu.ee/kinfoleht/{aastastr}_infoleht.php"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags with .html URLs
    html_urls = soup.find_all("a", href=re.compile(r"\.html$"))

    # Extract the URLs
    urls = [link["href"] for link in html_urls]
    i = 0
    # Print the URLs
    for url in urls:
        failinimi = url.split("/")[-1].replace(".html", "")
        resp = requests.get("http://www.htg.tartu.ee/" + url)
        urlObject[f"{kaust}/{uusAastStr}_{i}.txt"] = "http://www.htg.tartu.ee/" + url

        f = open(f"{kaust}/{uusAastStr}_{i}.txt", "w")
        # print(resp.content)
        f.write(resp.content.decode("windows-1257", errors="ignore"))
        f.close()
        i += 1

with open("urls.json", "w") as outfile:
    json.dump(urlObject, outfile)
