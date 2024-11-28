import pandas as pd
from Employee import Employee

def load_employee_from_csv(csv_file_path="Employee_Data.csv"):
    employee_data = pd.read_csv(csv_file_path)
    employees = []
    
    #Iterating over each row
    for index, row in employee_data.iterrows():
        employee_id = row['employee_id']
        name = row['name']
        email = row['email']
        department = row['department']
        role = row['role']
        salary = row['salary']
        
        #creating an instance
        employee = Employee(
            employee_id=employee_id,
            name=name,
            email=email,
            department=department,
            role=role,
            salary=salary
        )

        #populating the performance metrics
        metrics = employee.get_performance_metrics()
        # Debug output: print available metrics keys and row keys to match
        #print(f"Expected Metrics Keys for Employee {employee_id}: {list(metrics.keys())}")
        #print(f"Available Columns in CSV Row: {list(row.index)}")
        
        for metric_key in metrics.keys():
            #update metric values if found
            if metric_key in row and pd.notna(row[metric_key]):
                metrics[metric_key] = row[metric_key]

                
        #append employee to the list created earlier
        employees.append(employee)
    
    return employees

        