
from PerformanceMetrics import Performance_metrix

class Employee:
    def __init__(self, employee_id, name, role, salary):
        
        """
        Represents an Employee with relevant information and metrics tracking.
        
        Attributes:
        - employee_id (str): Unique identifier for the employee.
        - name (str): Name of the employee.
        - role (str): Role of the employee (HR, Manager, Sales, Intern).
        - salary (float): Salary of the employee.
        - performance_metrics (PerformanceMetrics): Metrics tracked based on role.
        - performance_summary (str): Summary of the employee's overall performance.
        """
        
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary
        self.performance_metrics = Performance_metrix(role)
        self.performance_summary = ""
        
    def get_performance_metrics(self):
        """
        Returns the performance metrics dictionary for the employee.
        """
        return self.performance_metrics.metrics