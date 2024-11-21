from Employee import Employee

#Demo To Create The Employee
#performance_metrics will initialize the metrics (percepts or sensors based on the passed dpt, and role)
employee_1 = Employee(employee_id="001", 
                      name="Emp_A", 
                      department="HR", 
                      role="HR",
                      salary=50000)

employee_1.print_employee()

'''
    Possible steps
    1. Populate Employee from a csv file, with many employees
        -> Generally, the csv is abstracted, 
        -> Can be edited/changed/modified (Forexample of employee sold a car)
    2. The Constructor inside the employee will automatically generate performance_metrics
    Evaluator.py
    3. Make conditions (with dependencies)
        -> Conditions are functions to evaluate a cetrain performance
    4. Use the evaluate_employee function
        4.1 Pass condition and employee to evaluate_employee
        4.2 Let this function calculate evaluation
        4.3 Once the system evaluates the performance of the employee, populate "performance_summary" of employee
            -> Summary is saved inside employee's attribute
        4.4 return the summary for the employee
            -> Return Employees with performance_summary = "Something"
                   Return Options 
            (A= Return employyes with Something = "Promote")
            (B= Return employyes with Something = "Give Warning")
            (C= Return employyes with Something = "...")

'''