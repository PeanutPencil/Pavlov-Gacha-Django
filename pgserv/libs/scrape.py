import requests

from bs4 import BeautifulSoup

# from cards.models import Card



WEAPONS = {
    'm4':           1,
    'Aug':          2,
    'Ak47':         4,
    'AK12':         7,
    'Famas':        8,
    'G-3':          9,
    'AWP':          10,
    '.50 Cal':      3,
    'Sawed off':    11,
    'Pump':         12,
    'Spas12':       13,
    'Saiga 12':     14,
    'M249':         15,
    'Uzi':          16,
    'Ump45':        17,
    'mp5':          18,
    'p90':          19,
    'PP Bison':     20,
    'm1911':        21,
    'Glock':        22,
    'FiveSeven':    23,
    'Deagle':       6,
    'Revolver':     5,
    'Beretta':      24,
    'Tec9':         25,
    'Knife':        26,
    'Grenade':      27,
    'Clipers':      28,
    'Flash':        29,
    'Smoke':        30,
}


def get_line_data(line):
    """ Returns (name, picture, team) for a given line """
    cells = line.find_all('td')
    image = line.find("td", class_="player_cell").img['src']
    name = line.find("td", class_="player_cell").find('span').text
    team = line.find("td", class_="team_cell").find('span').text
    return (name, image, team)


if __name__ == '__main__':
    for i in range(0, 500, 100):
        resp = requests.get(f'https://vrmasterleague.com/Pavlov/Players/List/?posMin={i}')
        if resp.status_code != 200:
            raise('you fucked up bitch')

        soup = BeautifulSoup(resp.text, 'html.parser')

        for line in soup.find_all('tr')[1:]:
            name, image, team = get_line_data(line)

            for weapon, rarity in WEAPONS.items():
                # Card(name=name, weapon=weapon, rarity=rarity).save()
                r = requests.post('http://127.0.0.1:8000/cards/', data={
                    'name': name,
                    'weapon': weapon,
                    'rarity': rarity,
                })
                print(r.status_code, r.json()['name'])

    print('success')



