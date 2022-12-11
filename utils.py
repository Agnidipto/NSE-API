from operator import index
from bs4 import BeautifulSoup
import requests 
import json

result = {
}

index = open("index.json")
data = json.load(index)

# print(data)

def get_data(name) :

    source=requests.get(data[name]["link"])
    soup = BeautifulSoup(source.text, 'lxml')
    price_div= soup.find('div', class_='stickymcont')
    price= price_div.find('div', class_='pcstkspr nsestkcp bsestkcp futstkcp optstkcp')
    result["price"] = price.text
    # nseopen=soup.find('td', class_='nseprvclose')

    # calc=(float(price.text)-float(nseopen.text))/float(nseopen.text)*100

    # print(round(calc,2))

    price_change_div = price_div.find('div', class_="advdecl")
    entire = price_change_div.text.replace("("," ").replace(")","")
    points = entire.split(" ")[0]
    change = entire.split(" ")[1]

    result["points"] = points
    result["change"] = change
    result["up_down"] = "down" if ("-" in change) else "up"

    return (result)

print(get_data("Infosys"))