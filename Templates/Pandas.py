from typing import TextIO
import requests
import json
import pandas as pd
import pandas_datareader
from bs4 import BeautifulSoup


file: TextIO = open("../File.csv", "r")

def simple_api():
    url = 'https://dog.ceo/api/breeds/list/all'
    r = requests.get(url)
    r.status_code: 200
    result = json.loads(r.text)
    df = pd.DataFrame(result)
    print(df)

def Playlistrating():
    PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
    i = 0
    ratings = PlayListRatings[0]
    while (i < len(PlayListRatings) and ratings > 6):
        print(PlayListRatings)
        i = i + 1
        ratings = PlayListRatings[i]

    for i in range(0, 3):
        print(i)

def webscraping():
    #https://labs.cognitiveclass.ai/v2/tools/jupyterlab?ulid=ulid-7cb60dcb9baa86aadffe516df2758a67ab9d3cfb
    url = 'https://www.spiegel.de'
    data = requests.get(url).text
    soup = BeautifulSoup(data,"html5lib")
    links = soup.find_all('a')
    print(links)


def readdata():
    #csv
    read = pd.read_csv(file)
    df = pd.DataFrame(read)
    colum = df.iloc[[0, 1], 0]
    print(colum)
    #json


readdata()
webscraping()

