import requests
from bs4 import BeautifulSoup
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