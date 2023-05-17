import requests
import json
from settings import summoner_name
from settings import api_key

def summoner_info(summoner_name, api_key):

    """ This function retrieves summoner information from the SUMMONER-V4 endpoint 
        and saves it in a text file. For more information, please check the official 
        documentation at https://developer.riotgames.com/apis#summoner-v4. """

    api_url = 'https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name
    url = api_url + '?api_key=' + api_key
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Whale/3.20.182.14 Safari/537.36",
        "Accept-Language": "es-419,es;q=0.9",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": "RGAPI-21440e4d-2243-4a07-a626-fc7e771e4a47"
    }

    response = requests.get(url, headers=headers)
    res = response.json()

    if response.status_code == 200:
        with open('summoner-info.txt', 'a') as f:
            json.dump(res, f)
        print('Contenido JSON guardado en el archivo.')  
        return True   
    else:
        print('Tipo de error: ', response.status_code)
        return False
    
if __name__ == '__main__':
    summoner_info(summoner_name, api_key)
