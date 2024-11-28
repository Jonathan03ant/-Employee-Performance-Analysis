
from PerformanceMetrics import Performance_metrics

class Employee:
    def __init__(self, employee_id, email, name, department, role, salary):
        
        """
        Represents an Employee with relevant information and metrics tracking.
        
        Attributes:
        - employee_id (str): Unique identifier for the employee.
        - name (str): Name of the employee.
        - role (str): Role of the employee (HR, Manager, Sales, Intern).
        - salary (float): Salary of the employee.
        - performance_metrics (PerformanceMetrics): Metrics tracked based on role and department.
            Returns a metrics dict
        - performance_summary (str): Summary of the employee's overall performance.
        """
        
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.email = email
        self.role = role
        self.salary = salary
        self.performance_metrics = Performance_metrics(department,role) #returns a metrix dict
        self.performance_summary = ""
        
    def get_performance_metrics(self):
        """
        Returns the performance metrics dictionary for the employee.
        """
        return self.performance_metrics.metrics
    
    def get_metrics_attribute(self, attr):

        return self.performance_metrics.metrics[attr]
    
    def print_employee(self):
        """
        Prints the details of the employee, excluding the performance summary.
        """
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Name: {self.email}")
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(f"Metrics: {self.get_performance_metrics()}")