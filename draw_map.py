import requests

from PIL import Image, ImageDraw
headers = {'X-API-Key': 'd9cffc6c-9843-4c25-b4d7-befea89919a1'}
map_pole = 'https://datsblack.datsteam.dev/api/map'




def map_fight(url):
    resp = requests.get(url, headers=headers)
    return resp.json()


def draw_map():
    im = Image.new('RGB', (500, 300), (219, 193, 27))
    draw = ImageDraw.Draw(im)
    mapUrl = map_fight(map_pole)['mapUrl']
    resp = requests.get(mapUrl).json()

    height = resp['height']
    width = resp['width']
    canvas = Canvas(tk, height=height, width=width, bg='white')
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
        canvas.create_rectangle(start_island[0], start_island[1], start_island[0]+width_island, start_island[1]+height_island)
    print(resp['islands'][49]['start'])
    canvas.pack()
    canvas.update()
    canvas.postscript(file="a.eps", colormode='color')
    img = Image.open("a.eps")
    fig = img.convert('RGBA')
    fig.save('map.png', lossless=True)
    tk.mainloop()


def main():
    draw_map()


if __name__ == '__main__':
    main()
