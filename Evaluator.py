from Employee import Employee
from PerformanceMetrics import Performance_metrics
import numpy as np
import matplotlib.pyplot as plt

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

    def nps_editor(self, emp: Employee, metric, lower, higher):
        if metric < lower:
            emp.nps -=1
        elif metric >= higher:
           emp.nps +=1 

    
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
            # employee.print_employee()
            self.evaluate_engineer(employee)
        elif employee.department == "hr":
            self.evaluate_hr(employee)
        elif employee.department == "support":
            self.evaluate_support(employee)
        elif employee.department == "marketing":
            self.evaluate_marketing(employee)
        elif employee.department == "leadership":
            self.evaluate_leadership(employee)
        elif employee.department == "sales":
            self.evaluate_sales(employee)
        


    def evaluate_engineer(self,e):
        tickets_assigned = e.get_metrics_attribute("tickets_assigned")
        tickets_finished = e.get_metrics_attribute("tickets_finished")
        prs_opened = e.get_metrics_attribute("prs_opened_per_week")
        prs_rejected = e.get_metrics_attribute("prs_rejected_per_week")

        #tickets
        self.nps_editor(e, tickets_finished, 200, 300)

        if tickets_assigned>0:
            self.nps_editor(e, (tickets_finished/tickets_assigned), 0.8, 0.9)
        
        # PRs
        self.nps_editor(e, prs_opened, 3, 5)
        # percent
        if prs_opened> 0:
            self.nps_editor(e, (prs_rejected/prs_opened), 0.2, 0.1)       

        if e.role == "software_engineer":
            print("Software Engineer Eval")
            commits = e.get_metrics_attribute("prs_rejected_per_week")
            bugs_fixed = e.get_metrics_attribute("bugs_fixed")
            features = e.get_metrics_attribute("features_deployed")
            code_quality = e.get_metrics_attribute("code_review_quality_score")

            self.nps_editor(e, commits, 7, 10)
                      
            self.nps_editor(e, bugs_fixed, 100, 150)
                        
            self.nps_editor(e, features, 5, 10)
                      
            self.nps_editor(e, code_quality, 7, 8)
            

        elif e.role == "devops_engineer":
            print("DevOPs Eval")
            deployments_made = e.get_metrics_attribute("deployments_made")
            incidents = e.get_metrics_attribute("incidents_resolved")
            uptime_percentage = e.get_metrics_attribute("system_uptime_percentage")
            scripts_created = e.get_metrics_attribute("automation_scripts_created")

            self.nps_editor(e, deployments_made, 30, 50)
            
            self.nps_editor(e, incidents, 20, 35)
            
            self.nps_editor(e, uptime_percentage, 99.0, 99.5)
                        
            self.nps_editor(e, scripts_created, 300, 350)
            

        elif e.role == "test_engineer":
            print("Test Eval")
            test_written = e.get_metrics_attribute("test_cases_written")
            test_executed = e.get_metrics_attribute("test_cases_executed")
            bugs_reported = e.get_metrics_attribute("bugs_reported")
            automation = e.get_metrics_attribute("automation_coverage")
            
            self.nps_editor(e, test_written, 250, 400)
            
            self.nps_editor(e, (test_written/test_executed), 0.8, 0.9)
            
            self.nps_editor(e, bugs_reported, 100, 150)
            
            self.nps_editor(e, automation, 50, 75)
            

        elif e.role == "data_engineer":
            print("Data Eval")
            etl_jobs = e.get_metrics_attribute("etl_jobs_deployed")
            data_quality_fixes = e.get_metrics_attribute("data_quality_issues_fixed")
            latency_improvement = e.get_metrics_attribute("data_latency_improvements")

            self.nps_editor(e, etl_jobs, 20, 25)
            self.nps_editor(e, data_quality_fixes, 150, 200)
            
            self.nps_editor(e, latency_improvement, 10, 15)

    
    def evaluate_hr(self, e):
        interviews_facilitated = e.get_metrics_attribute("interviews_facilitated")
        interview_conv = e.get_metrics_attribute("interview_offer_conversion_rate")
        issues_resolved = e.get_metrics_attribute("issues_resolved")

        self.nps_editor(e, interviews_facilitated, 20, 25)
        self.nps_editor(e, interview_conv, 0.5, 0.8)
        self.nps_editor(e, issues_resolved, 0.9, 0.95)

        if e.role == "human_relations":
            satisfaction_score = e.get_metrics_attribute("employee_satisfaction_score")
            engagement_session = e.get_metrics_attribute("employee_engagement_sessions")
            training = e.get_metrics_attribute("training_sessions_organized")

            self.nps_editor(e, engagement_session, 12, 15)
            
            self.nps_editor(e, satisfaction_score, 7, 9)
            self.nps_editor(e, training , 5, 8)

        elif e.role == "talent_acquisition":
            interns_interviewed = e.get_metrics_attribute("interns_recruited_for_interview")
            interns_recruited = e.get_metrics_attribute("interns_recruited_for_offer")
            early_career_interviewed = e.get_metrics_attribute("early_career_recruited_for_interview")
            early_career_recruited = e.get_metrics_attribute("early_career_recruited_for_offer")

            self.nps_editor(e, interns_interviewed, 20, 30)
            self.nps_editor(e, interns_recruited, 10, 15)
            self.nps_editor(e, early_career_interviewed, 20, 30)
            self.nps_editor(e, early_career_recruited, 10, 15)



    def evaluate_sales(self, e):
        revenue = e.get_metrics_attribute("revenue_generated")
        deals_closed = e.get_metrics_attribute("deals_closed")
        conv_rate = e.get_metrics_attribute("conversion_rate")
        avg_cycle = e.get_metrics_attribute("avg_sales_cycle")
        additional_sales = e.get_metrics_attribute("additional_sales_revenue")

        self.nps_editor(e, revenue, 200000, 300000)
        self.nps_editor(e, deals_closed, 60, 100)
        self.nps_editor(e, conv_rate, 35, 50)
        self.nps_editor(e, additional_sales, 60000, 80000)
        self.nps_editor(e, avg_cycle, 5, 3)


    
    def evaluate_support(self, e):
        issues_assigned = e.get_metrics_attribute("issues_assigned")
        issues_resolved = e.get_metrics_attribute("issues_resolved")
        satisfaction = e.get_metrics_attribute("satisfaction_score")
        escalation_rate = e.get_metrics_attribute("escalation_rate")

        if issues_assigned>0:
            self.nps_editor(e, (issues_resolved/issues_assigned), 0.9, 0.95)
        self.nps_editor(e, satisfaction, 7, 9)
        self.nps_editor(e, escalation_rate, 30, 10)

        if e.role == "call_center":
            calls_answered = e.get_metrics_attribute("calls_answered")
            self.nps_editor(e, calls_answered, 1000, 1200)

        elif e.role == "it_support":
            res_time = e.get_metrics_attribute("average_resolution_time")
            self.nps_editor(e, res_time, 24, 18)
    

    def evaluate_leadership(self, e):
        goal_achieved =  e.get_metrics_attribute("goal_achievement")
        budget_adherence = e.get_metrics_attribute("budget_adherence") 

        self.nps_editor(e, goal_achieved, 90, 95)
        self.nps_editor(e, budget_adherence, 5, 3)

        if e.role == "executive":
            engagement_score = e.get_metrics_attribute("employee_engagement_score")
            innovation_index = e.get_metrics_attribute("innovation_index")
            self.nps_editor(e, engagement_score, 8, 9)
            self.nps_editor(e, innovation_index, 10, 15)

        elif e.role == "manager":
            reviews_conducted = e.get_metrics_attribute("reviews_conducted")
            team_retention = e.get_metrics_attribute("team_retention_rate")

            self.nps_editor(e, reviews_conducted, 90, 99)
            self.nps_editor(e, team_retention, 80, 90)

        
        elif e.role == "supervisor":
            engagement_sessions = e.get_metrics_attribute("employee_engagement_sessions")
            escalations_assigned = e.get_metrics_attribute("team_escalations_assigned")
            escalations_resolved = e.get_metrics_attribute("team_escalations_resolved")

            self.nps_editor(e, engagement_sessions, 4, 8)
            self.nps_editor(e, (escalations_resolved/escalations_assigned), 0.9, 0.95)
    
    def evaluate_marketing(self, e):
        leads_generated = e.get_metrics_attribute("leads_generated")
        roi = e.get_metrics_attribute("campaign_roi")
        initiatives_taken = e.get_metrics_attribute("marketing_initiatives_taken")

        self.nps_editor(e, leads_generated, 300, 500)
        self.nps_editor(e, roi, 150, 200)
        self.nps_editor(e, initiatives_taken, 10, 15)

        if e.role == "content_creator":
            media_engagement = e.get_metrics_attribute("social_media_engagement")
            content_created = e.get_metrics_attribute("content_created")
            content_approved = e.get_metrics_attribute("content_approved")

            self.nps_editor(e, media_engagement, 300000,500000)
            self.nps_editor(e, content_created, 50, 70)
            self.nps_editor(e, (content_created/content_approved), 0.7, 0.8) 

        
        elif e.role == "brand_manager":
            campaign_launched = e.get_metrics_attribute("campaigns_launched")
            brand_awareness = e.get_metrics_attribute("brand_awareness_score")
            feedbacks = e.get_metrics_attribute("customer_feedback_collected")

            self.nps_editor(e, campaign_launched, 5, 8)
            self.nps_editor(e, feedbacks, 800, 1000)
            self.nps_editor(e, brand_awareness, 0.7, 0.8)

    def evaluate_nps(self, emp, low, high):

        #Converting the NPS scores to a scale of 0-10 using Linear Interpolation
        #NPS Score range [a,b]
        #Scale range [c,d]
        #NPS Score [x]

        x = emp.nps
        a = low
        b = high
        c = 1
        d = 10
        
        adjusted = abs(((x-a)/(b-a)) * (d-c) + a)+3
        

        if adjusted<4:
            # print("Bad")
            emp.performance_summary = "Low Performance"
        elif adjusted>=4 and adjusted<7:
            # print("Ok")
            emp.performance_summary = "Moderate Performance"
        elif adjusted >= 7:
            # print("Good")
            emp.performance_summary = "High Performance"
        


    def employee_sale_state(self, employee: Employee):
        # Returns the current state eof the employee's sale, given that the employee is in X role
        if employee.role == "Sales":
            return employee.get_performance_metrics().get("sales_made", 0)
        else:
            return None
