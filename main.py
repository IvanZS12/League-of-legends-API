import requests
import json
from settings import summoner_name
from settings import api_key

def summoner_info(summoner_name, api_key):

    """ This function retrieves summoner information from the SUMMONER-V4 endpoint 
        and saves it in a text file. For more information, please check the official 
        documentation at https://developer.riotgames.com/apis#summoner-v4. """

    url = 'https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name
    response = requests.get(url, headers=headers) #Get headers on https://developer.riotgames.com
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
