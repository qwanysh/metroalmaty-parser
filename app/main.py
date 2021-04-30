import httpx
from bs4 import BeautifulSoup


URL = 'http://metroalmaty.kz/?q=ru/schedule-list'


def main():
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.select_one('table.tab-sch > tbody')
    rows = table.select('tr')

    data = parse_data(rows)

    for item in data:
        print('{:30}{:10}{:10}'.format(*item.values()))


def parse_data(rows):
    data = []
    for row in rows:
        cells = row.select('td')

        data.append({
            'station_name': cells[0].get_text(),
            'time_1': cells[1].get_text(),
            'time_2': cells[2].get_text(),
        })
    return data


def get_html(url):
    response = httpx.get(url)
    return response.content.decode()


if __name__ == '__main__':
    main()
