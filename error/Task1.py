class SalaryGivingError(Exception):
    def __init__(self, message):
        super(SalaryGivingError, self).__init__(message)
class NotEmployeeException(Exception):
    def __init__(self, message):
        super(NotEmployeeException, self).__init__(message)
class WrongEmployeeRoleError(Exception):
    def __init__(self, message):
        super(WrongEmployeeRoleError, self).__init__("Employee " + message +" has unexpected role!")



class Employe:
    #first_name = ""
    @property
    def get_salary(self):
        total_salary  = self.salary
        if self.experiance > 5:
            total_salary *= 1.2
            total_salary += 500
        elif self.experiance > 2:
            total_salary
        return self.salary
    def __init__(self, first_name = None, second_name = None, salary = None, experiance = None, manager = None):
        self.first_name  = first_name
        self.second_name = second_name
        self.salary = salary
        self.experiance = experiance
        self.manager = manager
    def __repr__(self):
        return self.first_name + " " + self.second_name + ", manager:" + self.second_name  + ", experiance:" + self.experiance




class Developer(Employe):
    def __init__(self, first_name = None, second_name = None, salary = None, experiance = None, manager = None):
        super(Developer, self).__init__(first_name, second_name, salary, experiance, manager)


class Designer(Employe):
    def __init__(self,first_name = None, second_name = None, salary = None, experiance = None, manager = None, effectivness = None):
        super(Designer, self).__init__(first_name, second_name, salary, experiance, manager)
        self.effectivness = effectivness

    def get_salary(self):
        return super.getsalary() * self.effectivness

class Manager(Employe):
    def __init__(self, team = [], first_name = None, second_name = None, salary = None, experiance = None, manager = None):
        super(Manager, self).__init__(first_name, second_name, salary, experiance, manager)

        self.team = team
    def get_team(self):
        return self.team
    def get_salary(self):
        total_salary = super.getsalary()
        if len(filter(lambda e: type(e) is Developer, self.team ))>len(self.team)/2:
            total_salary *= 1.1
        if len(self.team) > 5 & len(self.team) <= 10:
            total_salary += 200
        elif len(self.team) > 10:
            total_salary += 300
        return total_salary
    def add_to_team(self, array):
        try:
            if(len(array) == None):
                raise NotEmployeeException("NotEmployeeException")
            managers = filter(lambda e: type(e) is Manager, array)
            if(len(managers) > 0):
                raise WrongEmployeeRoleError(managers[0].second_name)
            self.team.extend(array)
        except Exception as e:
            print(e)


class Department(object):
    def __init__(self, managers = []):
        self.managers = managers

    def give_salary(self):

        for i in range(0, len(self.managers)):
            try:
                team_size = len(self.managers[i].get_team())
                if team_size == 0:
                    raise SalaryGivingError(self.managers[i].first_name + " not have team!")
                for j in range(0, team_size):
                    employee = self.managers[i].team[j]
                    print(employee.first_name + " " + employee.second_name + ": got salary:" + str(employee.salary))
            except SalaryGivingError as e:
                details = e.args[0]
                print(details)
    def add_team_members(self, manager, array):
        manager.add_to_team(array)


m1 = None
d1 = Developer("Alex", "Sergeevich", 800, 1, m1)
d2 = Developer("Foo", "Bar", 9000, 20, m1)
des1 = Designer("Grisha", "Perelman", 100, 20, m1, 0.5)
m1 = Manager([d1, d2, des1], "Andrii", "Petrov", 1000, 1 , manager = None)
m2 = Manager([], "ABC", "ABC", 100 , 0, manager = None)
someDep = Department([m1, m2])
someDep.give_salary()