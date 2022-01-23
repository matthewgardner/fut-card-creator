from os import environ
from cardcreator import render_card
from resources.exceptions import *


# Team info
club = 777
card_code = 'EL'
dynamic_fl = False 

# Player Data
emerson_data = { "name":'Emerson Camp',"position":'CM', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/emerson.png' }
harry_h_data = { "name":'Harry Hitchcock',"position":'LM', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/harryh.png'}
harry_s_data = { "name":'Harry Stone',"position":'CF', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/harrys.png'}
jacob_data = { "name":'Jacob Martins',"position":'CF', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/jacob.png'}
marcus_data = { "name":'Marcus Akinboroye',"position":'RM', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/marcus.png'}
matthew_data = { "name":'Matthew Parrish',"position":'LB', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/matthew.png'}
moses_data = { "name":'Moses Purrier',"position":'CB', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/moses.png'}
samuel_data = { "name":'Samuel Gardner',"position":'RB', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/samuel.png' }
simmy_data = { "name":'Simmy Ewles',"position":'CM', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/simi.png' }
thomas_data = { "name":'Thomas Bennet',"position":'CM', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/thomas.png' }
valentino_data = { "name":'Val MacDonald',"position":'GK', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/valentino.png' }
zack_data = { "name":'Zachary Stock',"position":'CM', "club": 777, "country": 'GB-ENG', "overall": 88, "pac": 88, "dri": 88,
            "sho": 88, "def": 88, "pas": 88, "phy": 88, "lang_code":'EN', "mug_shot": 'assets/players/emerson.png' }


rangers = [emerson_data,harry_h_data,harry_s_data,jacob_data,marcus_data,matthew_data,
            moses_data,samuel_data,simmy_data,thomas_data,valentino_data,zack_data]

for ranger in rangers:
    print(f'Building card for:({ranger["name"]}) ' )
    render_card(card_code, dynamic_fl,ranger)
    print(f'Complete card for:({ranger["name"]}) ' )
