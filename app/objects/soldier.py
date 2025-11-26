from pydantic import BaseModel
import re


class Soldier:

    def __init__(self, military_id, first_name, last_name, sex, city, distance):
        self.military_id: str  = self.check_military_id(str(military_id))
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.sex: str = sex
        self.city: str = city
        self.distance: int = distance
        self.assigned: bool = False

    def check_military_id(self, military_id):
        if not re.match(r"8.", military_id):
            raise Exception("military id number does not start with 8")

        return military_id




