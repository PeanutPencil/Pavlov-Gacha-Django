import sys
print(sys.path)
sys.path.append(".")
print(sys.path)

from cards.models import Card
from libs.scrape import WEAPONS

"""
Card(
    name="",
    weapon="",
    rarity=,
    image="/images/player_logo_40.png",
    vrml_id=None,
    seeded=True,
).save()
"""

""" Populate db with non-vrml but known pavlov players """
players = (
    ('Reimus Klinsman', '/images/player_logo_40.png'),
    ('PeanutPencil', '/images/player_logo_40.png'),
    ('Birb', '/images/player_logo_40.png'),
    ('Snoopinator', '/images/player_logo_40.png'),
    ('Perkins', '/images/player_logo_40.png'),
    ('SposhJears', '/images/player_logo_40.png'),
    ('NeedBail', '/images/player_logo_40.png'),
    ('Immoutal', '/images/player_logo_40.png'),
    ('SEXCOPTER RUL', '/images/player_logo_40.png'),
    ('Robin', '/images/player_logo_40.png'),
    ('ZockerCH', '/images/player_logo_40.png'),
    ('Private Prof', '/images/player_logo_40.png'),
    ('Chronobrodi', '/images/player_logo_40.png'),
    ('Sev', '/images/player_logo_40.png'),
    ('Scortched', '/images/player_logo_40.png'),
)
for player, image in players:
    if Card.objects.filter(name=player):
        continue
    for weapon_name, rarity in WEAPONS.items():
        Card(
            name=player,
            weapon=weapon_name,
            rarity=rarity,
            image=image,
            vrml_id=None,
            seeded=True,
        ).save()

""" Add new cards """
Card(
    name="Reimus Klinsman",
    weapon="Throwing Knives",
    rarity=1,
    image="/images/player_logo_40.png",
    vrml_id=None,
    seeded=True,
).save()

Card(
    name="Reimus Klinsman",
    weapon="Dual M249s",
    rarity=2,
    image="/images/player_logo_40.png",
    vrml_id=None,
    seeded=True,
).save()

Card(
    name="TheCrimsonFucker",
    weapon="Spin bot",
    rarity=2,
    image="/images/player_logo_40.png",
    vrml_id=None,
    seeded=True,
).save()

Card(
    name="Perkins",
    weapon="Dual Uzis",
    rarity=2,
    image="/images/player_logo_40.png",
    vrml_id=None,
    seeded=True,
).save()

Card(
    name="Perkins",
    weapon="Dual M1911s",
    rarity=8,
    image="/images/player_logo_40.png",
    vrml_id=None,
    seeded=True,
).save()

Card(
    name="SEXCOPTER RUL",
    weapon="Cellphone antenna internet",
    rarity=1,
    image="/images/player_logo_40.png",
    vrml_id=None,
    seeded=True,
).save()

""" Modify current cards """
# PeanutPencil
c = Card.objects.get(name="PeanutPencil", weapon="Five-seveN")
c.rarity = 1
c.seeded = True
c.save()

# WizardOnAMountain/ThatGuyChriss
c = Card.objects.get(vrml_id="NXoyN2M0SlRJajQ90", weapon="Clippers")
c.weapon = "Dual Clippers"
c.rarity = 2
c.seeded = True
c.save()

# Pgati
c = Card.objects.get(vrml_id="akVNa0tTMndIV2s90", weapon="P90")
c.rarity = 2
c.seeded = True
c.save()

# Snoopinator
c = Card.objects.get(name="Snoopinator", weapon="Grenade")
c.weapon = "Suicide Grenade"
c.rarity = 2
c.seeded = True
c.save()