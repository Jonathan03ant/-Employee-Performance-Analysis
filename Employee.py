

'''
    Employee Class: 
        * Represents Employees [HR, Manager, Sales, Intern]
        * Reference to Performance Metrix Class
        * Each Employee has a role, which determines what metrics to track
'''

class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary
        self.performance_metrics = performance_metrics(role)