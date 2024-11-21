
'''
For each employee(role, department)
The metrics in the PerformanceMetrics class represent percepts about that employee’s current state. 
They are effectively observations about the performance of the employee.

    Performance_Metrics Class:
        * A class to manage different perormances (which are percepted from the Employee's Env)
        * Metrics are determined based on roles (Different Env for each role)
    # State represents the information an agent knows about the world at any given point.
        Each Metrics is a representation of different state for an employee
'''

class Performance_metrics:
    def __init__(self, role, department):
        self.role = role
        self.department = department
        self.metrics = self.init_metrics_for_employee(role, department)
        
    def init_metrics_for_employee(self, role, department):
        # Initializes Metrics based on role, and dept
        # The metrics dic is essentially states of the employee
        metrics = {}
        
        if role == "HR":
            
            metrics = {
                "attendance_rate":0,
                "recruiments_clsoed":0,
            }
            
        elif role == "Manager":
            
            metrics = {
                "projects_completed": 0,
                "team_performance" : 0
            }
            
            if department == "Sales":
                metrics["total_cars_sold"] = 0
                
        elif role == "Sales":
            
            metrics = {
                "sales_made":0,
            }
            
        ## We can add more roles, based on need and update the metrics
        else:   #Default metrics, for debugging
            metrics = {
                "attendance_rate":0,
            }
        
        return metrics
            