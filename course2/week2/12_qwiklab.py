import csv

def read_employees(csv_file_location):

  with open(csv_file_location) as file:
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    dic = csv.DictReader(file, dialect='empDialect')
    employee_list = []
    for data in dic:
      employee_list.append(data)
    file.close()

  return employee_list;


def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])

  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)

  return department_data


def write_report(dictionary, report_file):
  with open(report_file, "w+") as file:
    for key in sorted(dictionary):
      file.write(str(key) + ':' + str(dictionary[key]) + '\n')
    file.close()

employee_list = read_employees('employees.csv')
# print(process_data(employee_list))
dictionary = process_data(employee_list)
write_report(dictionary, 'report.txt')

