import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

HOST = "http://www.kivano.kg"
URL = "http://www.kivano.kg"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req

@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='item product_listbox oh')
    tires = []

    for item in items:
        tires.append(
            {
                'title': URL + item.find('a').get("href"),
                'title_text': item.find('div', class_='listbox_title oh').get_text(),
                'price': item.find('div', class_='listbox_price text-center').get_text(),
                'image': URL + item.find('div', class_='listbox_img pull-left').find('img').get('src')
            }
        )
    return tires

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        tires1 = []
        for page in range(0, 1):
            html = get_html(f'http://www.kivano.kg/shiny-zimnie', params=page)
            tires1.extend(get_data(html.text))
        return tires1
    else:
        raise ValueError('Error in parser...')