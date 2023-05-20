import requests
import time
from settings import api_key
url = 'https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'

with open('summoners-name.txt', 'r', encoding='utf-8') as f:
    summonerNames = f.read().splitlines()
with open('puuids.txt', 'a', encoding='utf-8') as f:
    for summonerName in summonerNames:
        print(summonerName)
        try:
            response = requests.get(url+str(summonerName), headers=headers)
            f.write(response.json()['puuid'] + '\n')
        except KeyError:
            print('failed to get', summonerName)
            pass
        time.sleep(1.3)  
        
