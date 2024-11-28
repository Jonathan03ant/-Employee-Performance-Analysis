from Employee import Employee
from PerformanceMetrics import Performance_metrics

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
    
    # def evaluate_employee(self, conditions: list , employee: Employee):
    def evaluate_employee(self, employee: Employee):
        """
        conditions are functions that evaluate specific performance metrics of an employee.
        employee: An instance of the Employee class to evaluate

        This central evaluation function:
            - Collects values from multiple condition functions
            - Evaluates the employee performance based on these collected values
            - Updates the employee's performance summary
        """

        if employee.department ==  "engineering":
            employee.print_employee()
            self.evaluate_engineer(employee)
        elif employee.department == "hr":
            print("HR")
        elif employee.department == "support":
            print("support")
        


    def evaluate_engineer(self,e):
        nps_score = 0
        tickets_assigned = e.get_metrics_attribute("tickets_assigned")
        tickets_finished = e.get_metrics_attribute("tickets_finished")
        prs_opened = e.get_metrics_attribute("prs_opened_per_week")
        prs_merged = e.get_metrics_attribute("prs_merged_per_week")
        prs_rejected = e.get_metrics_attribute("prs_rejected_per_week")

        if tickets_finished < 200 or (tickets_finished/tickets_assigned)<0.8:
            nps_score -= 1
        elif tickets_finished >= 300 or (tickets_finished/tickets_assigned)>=0.9:
            nps_score += 1
        
        if prs_opened <= 3:
            nps_score -= 1
        elif prs_opened >= 5:
            nps_score += 1
        
        if (prs_rejected/prs_opened)>0.2:
            nps_score -= 1
        elif (prs_rejected/prs_opened)<= 0.1:
            nps_score += 1

        print("NPS")
        print(nps_score)        

        if e.role == "software_engineer":
            print("Software Engineer Eval")
            commits = e.get_metrics_attribute("prs_rejected_per_week")
            bugs_fixed = e.get_metrics_attribute("bugs_fixed")
            features = e.get_metrics_attribute("features_deployed")
            code_quality = e.get_metrics_attribute("code_review_quality_score")

            if commits < 7:
                nps_score -= 1
            elif commits >= 10:
                nps_score += 1
            
            if bugs_fixed < 100:
                nps_score -= 1
            elif bugs_fixed >= 150:
                nps_score += 1
            
            if features < 5:
                nps_score -= 1
            elif features >= 10:
                nps_score += 2

            if code_quality < 7:
                nps_score -= 1
            elif code_quality >= 8:
                nps_score += 1

        elif e.role == "devops_engineer":
            print("DevOPs Eval")
            deployments_made = e.get_metrics_attribute("deployments_made")
            incidents = e.get_metrics_attribute("incidents_resolved")
            uptime_percentage = e.get_metrics_attribute("system_uptime_percentage")
            scripts_created = e.get_metrics_attribute("automation_scripts_created")

            if deployments_made < 30:
                nps_score -= 1
            elif deployments_made >= 50:
                nps_score += 1
            

            if incidents < 20:
                nps_score -= 1
            elif incidents >= 35:
                nps_score += 1

            if uptime_percentage < 99.0:
                nps_score -= 1
            elif uptime_percentage >= 99.5:
                nps_score += 1
            
            if scripts_created < 300:
                nps_score -= 1
            elif scripts_created >= 350:
                nps_score += 1

        elif e.role == "test_engineer":
            print("Test Eval")
            test_written = e.get_metrics_attribute("test_cases_written")
            test_executed = e.get_metrics_attribute("test_cases_executed")
            bugs_reported = e.get_metrics_attribute("bugs_reported")
            automation = e.get_metrics_attribute("automation_coverage")
            
            if test_written < 250:
                nps_score -= 1
            elif test_written >= 400:
                nps_score += 1
            
            if test_written/test_executed < 0.8:
                nps_score -= 1
            elif test_written/test_executed < 0.9:
                nps_score += 1

            if bugs_reported < 100:
                nps_score -= 1
            elif bugs_reported >= 150:
                nps_score += 1

            if automation < 50:
                nps_score -= 1
            elif automation >= 75:
                nps_score += 1

        # elif e.role == "data_engineer":
        #     print("Data Eval")
        



    def employee_sale_state(self, employee: Employee):
        # Returns the current state of the employee's sale, given that the employee is in X role
        if employee.role == "Sales":
            return employee.get_performance_metrics().get("sales_made", 0)
        else:
            return None
