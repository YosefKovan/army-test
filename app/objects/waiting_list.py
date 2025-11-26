
class WaitingList:

    def __init__(self):
        self.not_assigned_soldiers = []

    def add_soldier(self, soldier):
        self.not_assigned_soldiers.append(soldier)

    def remove_soldier(self, soldier):
        self.not_assigned_soldiers.remove(soldier)

    def add_to_waiting_list(self, soldiers):

        count = 0
        for soldier in soldiers:
            if soldier.assigned == False:
                count += 1
                self.not_assigned_soldiers.append(soldier)

    def get_amount_waiting(self):
        return len(self.not_assigned_soldiers)

