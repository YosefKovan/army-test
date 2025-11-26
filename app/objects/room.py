

class Room:
    def __init__(self, max_beds, dorm_number, room_number):
        self.__soldiers = []
        self.max_beds = max_beds
        self.dorm_number = dorm_number
        self.room_number = room_number


    def add_soldier(self, soldier):

        if len(self.__soldiers) < self.max_beds:
            self.__soldiers.append(soldier)
            soldier.room_number = self.room_number
            soldier.dorm_number = self.dorm_number
            soldier.assigned = True
            return True

        return False

    def room_available(self):
        return len(self.__soldiers) < self.max_beds


    def amount_in_room(self):
        return len(self.__soldiers)