from abc import ABCMeta, abstractmethod

class MititaryObject(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, spy):
        pass

class GeneralStaff(MititaryObject):
    def __init__(self, generals, secretPaper):
        self.generals = generals
        self.secretPaper = secretPaper

    def accept(self, spy):
        spy.visitstaff(self)

    def __str__(self):
        return f"GeneralStaff: У генеральному штабі є {self.generals} геренералів та {self.secretPaper} секретних паперів."


class MilitaryBase():
    def __init__(self, officers, soldiers, jeeps, tanks):
        self.officers = officers
        self.soldiers = soldiers
        self.jeeps = jeeps
        self.tanks = tanks

    def accept(self, spy):
        spy.visitbase(self)

    def __str__(self):
        return f"MilitaryBase: На військовій базі є {self.officers} офіцерів, {self.soldiers} солдатів, {self.jeeps} джипів та {self.tanks} танків."

class Spy(metaclass=ABCMeta):
    @abstractmethod
    def visitbase(self,base):
        pass

    @abstractmethod
    def visitstaff(self, staff):
        pass

class Diversant(Spy):
    def visitbase(self,base):
        print(f" Destroyed {base.officers} officers, {base.soldiers} soldiers, and {base.jeeps} jeeps and {base.tanks} tanks.")
    def visitstaff(self, staff):
        print(f"Destroyed {staff.generals} generals, {staff.secretPaper} secret papers.")


class SecretAgent(Spy):
    def visitstaff(self, staff):
        print(f" foto of {staff.generals} generals, {staff.secretPaper} secret papers.")
    def visitbase(self,base):
        print(f" foto of {base.officers} officers, {base.soldiers} soldiers, and {base.jeeps} jeeps and {base.tanks} tanks.")


if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100)
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20)
    print(militaryBase)

    secretagent1=SecretAgent()
    print(secretagent1)
    diversant1=Diversant()
    print(diversant1)


