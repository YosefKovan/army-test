from app.objects.room import Room

class Dorm:

    def __init__(self, number_of_rooms, max_beds, dorm_number):
        self.rooms = self.__create_rooms(number_of_rooms, max_beds, dorm_number)
        self.dorm_number = dorm_number

    def __create_rooms(self, number_of_rooms, max_beds, dorm_number):

        rooms = []

        for room_number in range(number_of_rooms):
            rooms.append(Room(max_beds, dorm_number, room_number))

        return rooms


    def space_available(self):
        for room in self.rooms:
            if room.room_available():
                return True

        return False


    def place_soldier(self, soldier):

        for room in self.rooms:
            if room.add_soldier(soldier):
                return True

        return False


    def get_amount_in_rooms(self):

        amount_in_rooms = 0

        for room in self.rooms:
            amount_in_rooms += room.amount_in_room()

        return amount_in_rooms
