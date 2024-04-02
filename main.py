import requests
from PIL import Image, ImageDraw
import json
import time

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


def draw_map():
    mapUrl = map_fight(map_pole)['mapUrl']
    resp = requests.get(mapUrl).json()

    height = resp['height']
    width = resp['width']
    im = Image.new('RGB', (height, width), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    kolvo_islands = len(resp['islands'])
    # print(resp['islands'])
    # print(resp)
    for i in range(kolvo_islands):
        # print(resp['islands'][i])
        map_island = resp['islands'][i]['map']
        start_island = resp['islands'][i]['start']
        height_island = len(map_island)
        width_island = len(map_island[1])
        # print(height_island, width_island)
        # print(start_island)
        draw.rectangle(
            (start_island[0], start_island[1], start_island[0] + width_island, start_island[1] + height_island),
            fill='Black')
    # print(resp['islands'][49]['start'])
    im.save('map.png', quality=95)


def scan(url):
    resp = requests.get(url, headers=headers)
    # print(json.dumps(resp.json(), indent=4))
    return resp.json()


def draw_ships():
    im = Image.open('map.png')
    draw = ImageDraw.Draw(im)
    data_scan = scan(href_scan)
    myShips = data_scan['scan']['myShips']
    enemyShips = data_scan['scan']['enemyShips']
    for ship in myShips:
        # print(ship)
        x_ship_start = ship['x']
        y_ship_start = ship['y']
        x_ship_end = 0
        y_ship_end = 0
        size_ship = ship['size']
        direction = ship['direction']
        if direction == 'north':
            x_ship_end = x_ship_start
            y_ship_end = y_ship_start - size_ship
        elif direction == 'south':
            x_ship_end = x_ship_start
            y_ship_end = y_ship_start + size_ship
        elif direction == 'west':
            x_ship_end = x_ship_start - size_ship
            y_ship_end = y_ship_start
        elif direction == 'east':
            x_ship_end = x_ship_start + size_ship
            y_ship_end = y_ship_start

        draw.rectangle((x_ship_start, y_ship_start, x_ship_end, y_ship_end), fill='green')
    for ship in enemyShips:
        # print(ship)
        x_ship_start = ship['x']
        y_ship_start = ship['y']
        x_ship_end = 0
        y_ship_end = 0
        size_ship = ship['size']
        direction = ship['direction']
        if direction == 'north':
            x_ship_end = x_ship_start
            y_ship_end = y_ship_start - size_ship
        elif direction == 'south':
            x_ship_end = x_ship_start
            y_ship_end = y_ship_start + size_ship
        elif direction == 'west':
            x_ship_end = x_ship_start - size_ship
            y_ship_end = y_ship_start
        elif direction == 'east':
            x_ship_end = x_ship_start + size_ship
            y_ship_end = y_ship_start

        draw.rectangle((x_ship_start, y_ship_start, x_ship_end, y_ship_end), fill='red')

    im.save('map.png', quality=95)


def move_ships():
    im = Image.open('map.png')
    draw = ImageDraw.Draw(im)
    data_scan = scan(href_scan)
    myShips = data_scan['scan']['myShips']
    # print(myShips)

def cannonShot():
    while True:
        data_scan = scan(href_scan)
        myShips = data_scan['scan']['myShips']
        enemyShips = data_scan['scan']['enemyShips']
        print(enemyShips)
        # print(myShips)
        for data in myShips:
            print(data)
        for j in range(len(enemyShips)):
            x_enemy_ship = enemyShips[j]['x']
            y_enemy_ship = enemyShips[j]['y']
            for i in range(len(myShips)):
                id = myShips[i]['id']
                body = {'ships': [{'id': id, 'cannonShoot': {'x': x_enemy_ship, 'y': y_enemy_ship}}]}
                print(requests.post(href_shipCommand, headers=headers, data=json.dumps(body)).json())
        time.sleep(3)
def main():
    draw_map()
    draw_ships()
    move_ships()
    cannonShot()


if __name__ == '__main__':
    main()
