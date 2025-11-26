from app.objects.dorm import Dorm
from app.objects.room import Room

class Dorms:

    def __init__(self, number_of_dorms, number_of_rooms, max_beds):
        self.dorms = self.__create_dorms(number_of_dorms, number_of_rooms, max_beds)



    def __create_dorms(self, number_of_dorms, number_of_rooms, max_beds):
        """this function will initialize the list of the dorms"""
        dorms_list = []

        for dorm_number in range(number_of_dorms):
            dorms_list.append(Dorm(number_of_rooms, max_beds, dorm_number))

        return dorms_list


    def place_soldier(self, soldier):

        for dorm in self.dorms:
            if dorm.place_soldier(soldier):
                return True

        return False


    def get_amount_of_soldiers_in_dorms(self):

        amount_placed = 0
        for dorm in self.dorms:
            amount_placed += dorm.get_amount_in_rooms()

        return amount_placed




