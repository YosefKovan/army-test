from fastapi import HTTPException

from app.services.csv_reader import csv_to_dict
from app.services.json_service import get_json_format
from app.services.placement_service import place_soldiers
from app.services.soldiers_service import create_soldiers
from app.services.database_service import add_dorms_to_database
from app.services.database_service import add_rooms_to_db
from app.services.database_service import add_soldiers_to_db

#=========================================
#
#=========================================
async def assign_with_csv_service(session, file, soldiers, dorms, waiting_list):

    csv_dict = await csv_to_dict(file)
    soldiers = create_soldiers(csv_dict)
    place_soldiers(dorms=dorms, soldiers=soldiers, waiting_list=waiting_list)

    #add_dorms_to_database(session)
    #add_rooms_to_db(session)
    #add_soldiers_to_db(session)

    return get_json_format(soldiers, dorms, waiting_list)


#=========================================
#
#=========================================
def search_by_military_id_service(military_id, soldiers):

    for soldier in soldiers:
        if soldier.military_id == military_id:
           return soldier

    raise HTTPException(status_code=404, detail="soldier not found!")
