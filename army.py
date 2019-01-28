from soldier import Soldier
from medic import Medic

class Army:
    def __init__(self, soldiers, medics):
        self.soldiers = Soldier(soldiers)
        self.medics = Medic(medics)

    def health(self):
        return self.soldiers.health() + self.medics.health()