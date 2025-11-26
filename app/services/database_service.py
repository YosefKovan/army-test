from app.memory_data.data import dorms, waiting_list, soldiers
from app.models.dorms import Dorms
from app.models.rooms import Rooms
from app.models.soldiers import Soldiers
from sqlmodel import select


def add_dorms_to_database(session):

    for dorm in dorms.dorms:
        dorm = Dorms(dorm_number=dorm.dorm_number)
        session.add(dorm)

    session.commit()

def add_rooms_to_db(session):

    for dorm in dorms.dorms:
        for room in dorm.rooms:
            room = Rooms(room_number=room.room_number, dorm_number=room.dorm_number, max_capacity=room.max_beds)
            session.add(room)

    session.commit()


def add_soldiers_to_db(session):

    for soldier in soldiers:
        db_soldier = Soldiers(military_id=soldier.military_id,
                              first_name=soldier.first_name,
                              last_name=soldier.last_name,
                              sex=soldier.sex,
                              city=soldier.city,
                              distance=soldier.distance,
                              assigned=soldier.assigned,
                              room_number=soldier.room_number,
                              dorm_number=soldier.dorm_number)


        session.add(db_soldier)

    session.commit()



def get_all_dorms_from_db(session):
     return session.exec(select(dorms))

