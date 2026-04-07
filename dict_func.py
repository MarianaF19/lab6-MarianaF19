def employee_print(employee_info):
    info = employee_info.copy()

    name   = info.pop("Name",   "N/A")
    salary = info.pop("Salary", "N/A")
    role   = info.pop("Role",   "N/A")

   
