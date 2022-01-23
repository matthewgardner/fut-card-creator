from enum import Enum

from resources.languages_dictionary import languages_dict
from resources.language import Language
from resources.exceptions import InvalidPositionError, InvalidLanguageError
from resources.en_position import EnPosition




class Player:
    def __init__(self, data):
        
        self.name = data["name"].upper()

        try:
            self.language = Language[data["lang_code"]]
        except KeyError:
            raise InvalidLanguageError(f'Language ({data["lang_code"]}) is not a valid language.')

        try:
            position = Enum('Position', languages_dict.get(data["lang_code"]).get('positions'))
            self.position = position[data["position"].upper()]
        except KeyError:
            try:
                en_position = EnPosition[data["position"].upper()]
                position = Enum('Position', languages_dict.get(data["lang_code"]).get('positions'))
                index = en_position.value - 1
                self.position = position[languages_dict.get(data["lang_code"]).get('positions')[index]]
            except (KeyError, IndexError):
                raise InvalidPositionError(f'Position ({pos}) is not available in language {self.language}.'
                                           f'Conversion of {pos} from English position to {language} unsuccessful.')

        self.club = data["club"]
        self.country = data["country"].lower()

        self.overall = str(data["overall"]).zfill(2)
        self.pac = str(data["pac"]).zfill(2)
        self.dri = str(data["dri"]).zfill(2)
        self.sho = str(data["sho"]).zfill(2)
        self.deff = str(data["def"]).zfill(2)
        self.pas = str(data["pas"]).zfill(2)
        self.phy = str(data["phy"]).zfill(2)