import requests
import time
from settings import api_key #import YOUR API KEY 

page = 1
playersGathered = 0

while playersGathered < 2000:

    url = 'https://la1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/SILVER/IV?page='+ str(page)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Whale/3.20.182.14 Safari/537.36",
        "Accept-Language": "es-419,es;q=0.9",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": api_key
    }

    response = requests.get(url, headers=headers)

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
