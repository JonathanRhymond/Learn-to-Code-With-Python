employee_salaries = {
    "Guido": 100000,
    "James": 500000,
    "Brandon": 900000
}

extra_employee_salaries = {
    "Yukihiro": 1000000,
    "Guido": 333333
}

employee_salaries.update(extra_employee_salaries)
print(employee_salaries)
print(extra_employee_salaries)