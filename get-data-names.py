import requests
import time
from settings import api_key #import YOUR API KEY 

page = 1
playersGathered = 0

while playersGathered < 2000:

    url = 'https://la1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/SILVER/IV?page='+ str(page)
    
    response = requests.get(url, headers=headers) #Get headers on https://developer.riotgames.com

    with open('summoners-name.txt', 'a', encoding='utf-8') as f:
        for summoner in response.json():
            try:
                f.write(summoner['summonerName'] + '\n')
                playersGathered += 1
                print(f'page: {page} | players gathered: {playersGathered} | summoner name: {summoner["summonerName"]}')
            except UnicodeDecodeError:
                pass
    time.sleep(1.3)
    page += 1
