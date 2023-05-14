import requests
from bs4 import BeautifulSoup
import re
'''
for aasta in range(14, 22):
    # URL of the website to scrape
    url = f'https://www.htg.tartu.ee/Infolehed{aasta}'

    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object with the website's HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags ('a') in the HTML
    anchor_tags = soup.find_all('a')

    # Extract and print the href attribute of each anchor tag
    for tag in anchor_tags:
        href = tag.get('href')
        if href and "node" in href:
            print(href)

            nodeUrl = f"https://www.htg.tartu.ee{href}"

            nodeResp = requests.get(nodeUrl) 

            html_str = nodeResp.content.decode("utf-8")

            # print(html_str)
            num = href.split("/")[-1]
            splitted = html_str.split('<div class="field-items">', 1)[1].split('<aside id="sidebar-second" role="complementary">', 1)[0]
            f = open(f"infolehed2/INFOLEHT_{num}.txt", "w")
            f.write(splitted)
            f.close()
'''
'''
# 2023 
url = "https://www.htg.tartu.ee/Infolehed"
response = requests.get(url)

# Create a BeautifulSoup object with the website's HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all anchor tags ('a') in the HTML
anchor_tags = soup.find_all('a')

# Extract and print the href attribute of each anchor tag
for tag in anchor_tags:
    href = tag.get('href')
    if href and "node" in href:
        print(href)

        nodeUrl = f"https://www.htg.tartu.ee{href}"

        nodeResp = requests.get(nodeUrl) 

        html_str = nodeResp.content.decode("utf-8")

        # print(html_str)
        num = href.split("/")[-1]
        splitted = html_str.split('<div class="field-items">', 1)[1].split('<aside id="sidebar-second" role="complementary">', 1)[0]
        f = open(f"infolehed2/INFOLEHT_{num}.txt", "w")
        f.write(splitted)
        f.close()
'''

# 2002 - 2013
for aasta in range(2, 14):
    if (aasta < 10):
        aastastr = "0" + str(aasta)
    else:
        aastastr = str(aasta)
    
    print("20" + aastastr)

    url = f"http://www.htg.tartu.ee/kinfoleht/{aastastr}_infoleht.php"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags with .html URLs
    html_urls = soup.find_all("a", href=re.compile(r"\.html$"))

    # Extract the URLs
    urls = [link["href"] for link in html_urls]

    # Print the URLs
    for url in urls:
        failinimi = url.split("/")[-1].replace(".html", "")
        resp = requests.get("http://www.htg.tartu.ee/" + url)
        f = open(f"./infolehed2/{failinimi}.txt", "w")
        # print(resp.content)
        f.write(resp.content.decode("windows-1257", errors="ignore"))
        f.close()
