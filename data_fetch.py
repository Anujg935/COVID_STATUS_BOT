from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

mohfw_url = "https://www.mohfw.gov.in/"
world_url = "https://www.worldometers.info/coronavirus/" 

def getIndiaData():
    india_data = urlopen(mohfw_url)
    india_html = india_data.read()
    india_soup = soup(india_html,"html.parser")
    table = india_soup.findAll("table")
    last_row_data = table[-1].findAll("tr")[-2]
    india_data = last_row_data.findAll("td",{})

    indian =int(india_data[1].text[:-1])
    foreign_national = int(india_data[2].text[:-1])
    total_active_cases = indian + foreign_national
    total_recovered = int(india_data[3].text[:-1])
    deaths = int(india_data[4].text[:-1])
    total_cases = total_active_cases + total_recovered + deaths

    return total_cases,total_active_cases,deaths

def getWorldData(top=5):

    world_data = urlopen(world_url)
    world_html = world_data.read()
    world_soup = soup(world_html,"html.parser")
    table_world = world_soup.findAll("table",{'class':'main_table_countries'})[0]
    
    table_head = table_world.findAll('th')
    head = [ct.text for ct in table_head]
    head = head[0:4]
    head.remove('NewCases')

    table_row = table_world.findAll("tr")[1:]
    top_countries = {}
    for i in range(top):
        row = table_row[i]
        col = [r.text for r in row.findAll("td",{}) ]
        if(col[0] not in top_countries.keys()):
            top_countries[col[0]] = []
        top_countries[col[0]].append(col[1].strip())
        top_countries[col[0]].append(col[3].strip())

    return top_countries

