import unittest


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

class TestTeamLead(unittest.TestCase):

    def test_teamlead_has_attributes(self):
        self.teamlead = TeamLead(
            name="John",
            salary=5000,
            department="Quality Assurance",
            programming_language="Python",
            team_size=5)

        self.assertTrue(hasattr(self.teamlead, "name"))
        self.assertTrue(hasattr(self.teamlead, "salary"))
        self.assertTrue(hasattr(self.teamlead, "department"))
        self.assertTrue(hasattr(self.teamlead, "programming_language"))
        self.assertTrue(hasattr(self.teamlead, "team_size"))