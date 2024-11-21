from Employee import Employee
from PerformanceMetrics import Performance_metrix

'''
    Evaluator Class:
        * This is the Ai system's engine and all rules (IF THEN) should be implemented here
        * The goal of this class is to provide evaluation based on conditions      
    Attributes
        Rule: composed of conditions and actions
            Conditions (IF)------> Conditions come from different env states based on different percepts
            Actions (THEN)
        Evaluate_condition()
            - A central Algorithm which 
                * looks at different conditions (returned from the condition functions)
                * Evaluate the performance based on this conditions and dependencies
'''
class Evaluator:
    
    def __init__(self):
        pass
    
    def evaluate_employee(self, conditions: list , employee: Employee):
        """
        conditions are functions that evaluate specific performance metrics of an employee.
        employee: An instance of the Employee class to evaluate

        This central evaluation function:
            - Collects values from multiple condition functions
            - Evaluates the employee performance based on these collected values
            - Updates the employee's performance summary
        """
    def employee_sale_state(self, employee: Employee):
        # Returns the current state of the employee's sale, given that the employee is in X role
        if employee.role == "Sales":
            return employee.get_performance_metrics().get("sales_made", 0)
        else:
            return None
