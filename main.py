from Employee import Employee

#Demo To Create The Employee
#performance_metrics will initialize the metrics (percepts or sensors based on the passed dpt, and role)
employee_1 = Employee(employee_id="001", 
                      name="Emp_A", 
                      department="HR", 
                      role="HR",
                      salary=50000)

employee_1.print_employee()