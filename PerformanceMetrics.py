
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
    
    def __init__(self, department, role):
        self.role = role
        self.department = department
        self.metrics = self.init_metrics_for_employee(role, department)
        
    def init_metrics_for_employee(self, department, role):
        # Initializes Metrics based on role, and dept
        # The metrics dic is essentially states of the employee
        metrics = {}
        
                #ENGINEERING
                    #SOFTWARE_ENGINEER
                    #DEVOPS_ENGINEER
                    #TEST_ENGINEER
                    #SITE_R_ENGINEER
                    
        if department == "engineering":
            # Default metrics for all engineers
            metrics = {
                "tickets_assigned": 0,
                "tickets_finished": 0,
                "prs_opened_per_week": 0,
                "prs_merged_per_week": 0,
                "prs_rejected_per_week": 0              
            }
    
            # Additional metrics based on role
            if role == "software_engineer":
                metrics.update({
                    "commits_per_week": 0,
                    "bugs_fixed": 0,
                    "features_deployed": 0,
                    "code_review_quality_score": 0  # 1-10
                })
   
            elif role == "devops_engineer":
                metrics.update({
                    "deployments_made": 0,
                    "incidents_resolved": 0,
                    "build_pipeline_failures": 0,
                    "system_uptime_percentage": 0.0,  # Tracks system uptime percentage (target is usually high, e.g., 99.9%)
                    "automation_scripts_created": 0  # Measures scripts created to automate tasks
                })

            elif role == "test_engineer":
                metrics.update({
                    "test_cases_written": 0,
                    "test_cases_executed": 0,
                    "bugs_reported": 0,
                    "automation_coverage": 0,  # Percentage of testing that is automated
                    "test_documentation_created": 0  # Number of test plans or documentation pieces created
                })

            elif role == "data_engineer":
                metrics.update({
                    "data_pipelines_created": 0,
                    "pipelines_success_rate": 0,  # Percentage of successful pipeline runs
                    "data_quality_issues_fixed": 0,
                    "etl_jobs_deployed": 0,
                    "data_latency_improvements": 0  # Number of times data latency was improved
                })
                
                #HUMAN_RESOURCE
                    #HUMAN_RELATIONs
                    #TALENT_ACQUISITION
                    
        elif department == "hr":
            # Default metrics for all HR roles
            metrics = {
                "interviews_facilitated": 0,
                "offers_facilitated": 0,
                "interview_offer_conversion_rate": 0,  # Percentage conversion rate
                "issues_resolved": 0
            }

            # Additional metrics based on role
            if role == "human_relations":
                metrics.update({
                    # Offers Management
                    "offers_completed": 0,

                    # Employee Engagement and Well-being
                    "employee_satisfaction_score": 0,  # Average satisfaction score (scale of 1-10)
                    "employee_engagement_sessions": 0,
                    "recognition_awards_given": 0,

                    # Policy and Compliance
                    "hr_policy_updates_made": 0,
                    "compliance_issues_resolved": 0,
                    "training_sessions_organized": 0,

                    # Diversity and Inclusion Initiatives
                    "diversity_training_sessions": 0,
                    "diversity_hiring_programs_executed": 0,

                    # Employee Development
                    "career_development_sessions": 0,
                    "promotion_rate": 0  # Percentage of promotions supported by HR
                })

            elif role == "talent_acquisition":
                metrics.update({
                    # Recruitment Metrics
                    "interns_recruited_for_interview": 0,
                    "interns_recruited_for_offer": 0,
                    "early_career_recruited_for_interview": 0,
                    "early_career_recruited_for_offer": 0,
                    "total_employees_recruited_for_interview": 0,
                    "total_employees_recruited_for_offer": 0,
                    
                    # Key Metrics for Effective Talent Acquisition
                    "offer_acceptance_rate": 0,  # Percentage of offers accepted
                    "average_time_to_fill_position": 0,  # Average number of days to fill open positions
                })
                
        elif department == "marketing":
            metrics = {
                "campaign_roi": 0,
                "leads_generated": 0,
                "marketing_initiatives_taken": 0
            }

            if role == "content_creator":
                metrics.update({
                    "content_created": 0,
                    "content_approved": 0
                })
            elif role == "digital_marketer":
                metrics.update({
                    "social_media_engagement": 0,
                })
            elif role == "brand_manager":
                metrics.update({
                    "campaigns_launched": 0
                })

        elif department == "sales":
            
            metrics = {
                "revenue_generated": 0, #Total sales revenue from cars
                "deals_closed": 0, #Number of cars sold
                "leads_assigned": 0, #Number of leads assigned by marketing
                "conversion_rate": 0, #Number of leads turned into customers
                "avg_sales_cycle": 0, #Average time taken to close a deal
                "additional_sales_revenue": 0 #Revenue generated from selling service, warranty contracts                
                
            }
        elif department == "support":
            
            metrics = {
                "tickets_assigned": 0,
                "tickets_resolved": 0, #Number of tickets resolved
                "satisfaction_score": 0, #Satisfaction from the receiver
                "escalation_rate": 0 #Tickets escalated for further assistance
            }

            if role == "call_center":
                metrics.update({
                    "calls_answered": 0
                })
            elif role == "it_support":
                metrics.update({
                    "average_resolution_time": 0
                })
        elif department == "leadership":
            
            metrics = {
                "goal_achievement": 0,
                "budget_adherence": 0.0 #Percentage over/under budget
            }
            if role == "executive":
                metrics.update({
                    "employee_engagement_score": 0,
                    "innovation_index": 0
                })
            
            elif role == "manager":
                metrics.update({
                    "reviews_conducted": 0,
                    "team_retention_rate": 0
                })

            elif role == "supervisor":
                metrics.update({
                    "employee_engagement_sessions": 0,
                    "team_escalations_assigned" : 0,
                    "team_escalations_resolved" : 0
                })
            
        return metrics
            