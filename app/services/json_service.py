

def get_not_assigned_soldier(soldier):
    """this function will return the soldier object without the room and the dorm"""

    return {
        "military_id" : soldier.military_id,
        "first_name" : soldier.first_name,
        "last_name" : soldier.last_name,
        "sex" : soldier.sex,
        "city" : soldier.city,
        "distance" : soldier.distance,
        "assigned" : soldier.assigned
    }


def get_json_format(soldiers, dorms, waiting_list):


    return {"placed" : dorms.get_amount_of_soldiers_in_dorms(),
            "waiting" : waiting_list.get_amount_waiting(),
            "soldiers_placed" : [soldier for soldier in soldiers if soldier.assigned == True],
            "soldiers_waiting" : [get_not_assigned_soldier(soldier) for soldier in waiting_list.not_assigned_soldiers]
            }



