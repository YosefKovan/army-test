from app.objects.dorms import Dorms
from app.objects.waiting_list import WaitingList
from app.memory_data import data


def place_soldiers(dorms: Dorms, waiting_list : WaitingList, soldiers):

    try:
        for soldier in data.soldiers:
            if not dorms.place_soldier(soldier):
                break

    except Exception as e:
        print("Error occurred", e)


    waiting_list.add_to_waiting_list(soldiers)