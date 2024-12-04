from Employee import Employee
from data_loader import load_employee_from_csv
from Evaluator import Evaluator
from MainWindow import UI, QApplication, sys

#Demo To Create The Employee
#performance_metrics will initialize the metrics (percepts or sensors based on the passed dpt, and role)
employee_1 = Employee(employee_id="001", 
                      name="Emp_A", 
                      department="HR", 
                      email="fordford@ford.com",
                      role="HR",
                      salary=50000)

evaluator = Evaluator()

employee_1.print_employee()

print("Populating from csv")
employees = load_employee_from_csv()

#printing employees
for emp in employees[:10]:
    emp.print_employee()
    print(emp.get_performance_metrics())
    print("-----------------------------")
    
# Run Window
app = QApplication(sys.argv)
window = UI()

# Populate Window
for emp in employees:
    window.add_entry(emp)

window.show()
sys.exit(app.exec())

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