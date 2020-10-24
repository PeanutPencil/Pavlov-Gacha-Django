import requests
import shutil

from bs4 import BeautifulSoup

BASE_VRML_URL = 'https://vrmasterleague.com'

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
    """ Returns (id, name, picture, team) for a given line """
    cells = line.find_all('td')
    id_ = line.find("td", class_="player_cell").find("a")['href'].split('/')[-1]
    image = line.find("td", class_="player_cell").img['src']
    name = line.find("td", class_="player_cell").find('span').text
    team = line.find("td", class_="team_cell").find('span').text


    return (id_, name, image, team)


if __name__ == '__main__':
    for i in range(0, 500, 100):
        # Get vrml page with posMin value
        resp = requests.get(f'{BASE_VRML_URL}/Pavlov/Players/List/?posMin={i}')
        # Ensure there was no error
        if resp.status_code != 200:
            raise('you fucked up bitch')

        # Get a BeautifulSoup object to scrape the data
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Find all lines in the table
        for line in soup.find_all('tr')[1:]:
            try:
                # Get the id, name, image, and team from a given line
                id_, name, image, team = get_line_data(line)
            except AttributeError as e:
                print(e)
                print(line)
                continue

            # Download and save the image
            response = requests.get(f'{BASE_VRML_URL}{image}', stream=True)
            with open(f'.{image}', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)

            # Create cards in the db which are unique to player and weapon
            for weapon, rarity in WEAPONS.items():
                r = requests.post('http://127.0.0.1:8000/cards/', data={
                    'name': name,
                    'weapon': weapon,
                    'rarity': rarity,
                    'image': image,
                    'vrml_id': id_,
                })
                print(r.status_code, name)
                if r.status_code != 201:
                    print(r.text)

    print('success')



