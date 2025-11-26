from csv import excel

#from app.models.soldier import Soldier
from app.objects.soldier import Soldier


def order_soldiers(soldiers):
    soldiers.sort(key = lambda  obj : obj.distance, reverse=True)

def get_soldier_objects(data):
    soldiers = []

    for row in data:

        try:
            # for every row in the csv file we will create a soldier object
            soldier = Soldier(military_id=row["military_id"],
                              first_name=row["first_name"],
                              last_name=row["last_name"],
                              sex=row["sex"],
                              city=row["city"],
                              distance=int(row["distance"])
                              )

            soldiers.append(soldier)

        except Exception as e:
            print("unable to add soldier", e)

    return soldiers

def create_soldiers(data):
    """this will create the soldier objects"""

    soldiers = get_soldier_objects(data)
    order_soldiers(soldiers)

    for soldier in soldiers:
        print(soldier.distance)


    return soldiers



