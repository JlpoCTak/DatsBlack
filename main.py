import requests
import tkinter


href_map = 'https://datsblack.datsteam.dev/api/map'
href_scan = 'https://datsblack.datsteam.dev/api/scan'
href_longscan = 'https://datsblack.datsteam.dev/api/longScan'
href_shipCommand = 'https://datsblack.datsteam.dev/api/shipCommand'
map_pole = 'https://datsblack.datsteam.dev/api/map'

href_reg_death_match = 'https://datsblack.datsteam.dev/api/deathMatch/registration'

TOKEN = 'd9cffc6c-9843-4c25-b4d7-befea89919a1'
headers = {'X-API-Key': 'd9cffc6c-9843-4c25-b4d7-befea89919a1'}

def map_fight(url):
    resp = requests.get(url, headers=headers)
    return resp.json()

def reg_death_match():
    pass


def scan(url):
    resp = requests.get(url, headers=headers)
    return resp.json()


def main():
    print('1) ', scan(href_scan))
    print('2)', map_fight(map_pole))


if __name__ == '__main__':
    main()
