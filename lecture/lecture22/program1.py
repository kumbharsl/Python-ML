class Boss:
    def report(self):
        print("Boss : Report")

class Manager1(Boss):
    def report(self):
        print("Manager : Report")

class Manager2(Boss):
    def report(self):
        print("Manager : Report")

class Manager3(Boss):
    def report(self):
        print("Manager : Report")

class TeamLead1(Manager1, Manager3):
    def report(self):
        print("TeamLead : Report")

class TeamLead2(Manager2, Manager3):
    def report(self):
        print("TeamLead : Report")

class Developer(TeamLead1,TeamLead2):
    def report(self):
        print("Developer : Report")

print(Developer.__mro__)ssss