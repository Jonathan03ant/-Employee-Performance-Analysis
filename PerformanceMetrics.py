
'''
    Performance_Metrics Class:
        * A class to manage different perormances (which are percepted from the Employee's Env)
        * Metrics are determined based on roles (Different Env for each role)
    # State represents the information an agent knows about the world at any given point.
        Each Metrics is a representation of different state for an employee
'''

class Performance_metrix:
    def __init__(self, role):
        self.role = role
        self.metrics = self.init_metrics(role)
        
    def init_metrics(self, role):
        # Initializes Metrics based on role
        # The metrics dic is essentially states of the employee
        metrics = {}
        
        if role == "HR":
            metrics = {
                "attendance_rate":0,
                "recruiments_clsoed":0,
            }
        elif role == "Sales":
            metrics = {
                
            }
        elif role == "Manager":
            metrics = {
                
            }
        ## We can add more roles, based on need and update the metrics
        else:   #Default metrics, for debugging
            metrics = {
                "attendance_rate":0,
            }
        
        return metrics
            