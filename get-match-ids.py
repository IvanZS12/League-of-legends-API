import requests
import time
from settings import api_key

with open( 'puuids.txt', 'r') as f:
    puuids = f.read().splitlines()

with open('matches.txt', 'a') as f:
    idx = 1
    for puuid in puuids:
        print(idx)
        url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?type=ranked&start=0&count=1'
        response = requests.get(url, headers=headers)
        for match in response.json():
            print(match)
            f.write(match + '\n')
        idx += 1
        time.sleep(1.3)
