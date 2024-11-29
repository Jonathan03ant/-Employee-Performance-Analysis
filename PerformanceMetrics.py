
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
        self.metrics = self.init_metrics_for_employee(department, role)
        
    def init_metrics_for_employee(self, department, role):
        # Initializes Metrics based on role and department
        metrics = {}

        # ENGINEERING Department
        if department.lower() == "engineering":
            metrics = {
                "tickets_assigned": 0,
                "tickets_finished": 0,
                "prs_opened_per_week": 0,
                "prs_merged_per_week": 0,
                "prs_rejected_per_week": 0
            }

            # Software Engineer Metrics
            if role.lower() == "software_engineer":
                metrics.update({
                    "commits_per_week": 0,
                    "bugs_fixed": 0,
                    "features_deployed": 0,
                    "code_review_quality_score": 0
                })

            # DevOps Engineer Metrics
            elif role.lower() == "devops_engineer":
                metrics.update({
                    "deployments_made": 0,
                    "incidents_resolved": 0,
                    "build_pipeline_failures": 0,
                    "system_uptime_percentage": 0.0,
                    "automation_scripts_created": 0
                })

            # Test Engineer Metrics
            elif role.lower() == "test_engineer":
                metrics.update({
                    "test_cases_written": 0,
                    "test_cases_executed": 0,
                    "bugs_reported": 0,
                    "automation_coverage": 0,
                    "test_documentation_created": 0
                })

            elif role.lower() == "data_engineer":
                metrics.update({
                    "etl_jobs_deployed": 0,
                    "data_quality_issues_fixed": 0,
                    "data_latency_improvements": 0
                })

        # HR Department
        elif department.lower() == "hr":
            metrics = {
                "interviews_facilitated": 0,
                "offers_facilitated": 0,
                "interview_offer_conversion_rate": 0,
                "issues_resolved": 0
            }

            # Human Relations
            if role.lower() == "human_relations":
                metrics.update({
                    "offers_completed": 0,
                    "employee_satisfaction_score": 0,
                    "employee_engagement_sessions": 0,
                    "recognition_awards_given": 0
                })

            # Talent Acquisition
            elif role.lower() == "talent_acquisition":
                metrics.update({
                    "interns_recruited_for_interview": 0,
                    "interns_recruited_for_offer": 0,
                    "early_career_recruited_for_interview": 0,
                    "early_career_recruited_for_offer": 0
                })

        # SUPPORT Department
        elif department.lower() == "support":
            metrics = {
                "tickets_resolved": 0,
                "satisfaction_score": 0,
                "escalation_rate": 0,
                "average_resolution_time": 0
            }

            if role.lower() == "it_support":
                metrics.update({
                    "average_resolution_time": 0,
                    "avg_response_time": 0
                })

        # Default Case
        else:
            metrics = {
                "attendance_rate": 0
            }
        
        return metrics
