import psycopg2

connection = psycopg2.connect(
    database='crm_db'
)
cursor = connection.cursor()
# -------------COMPANIES-------------------
def create_company(name, industry):
      cursor.execute(
            'INSERT INTO companies (name, industry) ' 
            'VALUES (%s,%s);', [name, industry])
      connection.commit()
      print('----Added Company!----')

def print_companies():
    cursor.execute('SELECT id, name, industry FROM companies;')
    companies = cursor.fetchall()
    print('----Companies----')
    if not companies:
        print('----No Companies Found----')
    else:
         for company in companies:
              print(f'Id: {company[0]}, Name: {company[1]}, Industry: {company[2]}')

def update_company(id, name, industry):
    cursor.execute('UPDATE companies ' \
    'SET name = %s, ' \
    'industry = %s ' \
    'WHERE id = %s;', 
    [name, industry, id])
    connection.commit()
    print('----Company Updated----')
    print_companies()
# -------------------EMPLOYEES--------------------

def create_employee(first, last, company):
    cursor.execute(
        'INSERT INTO employees (first_name, last_name, company_id)' \
        ' VALUES (%s, %s, %s);', 
        [first, last, company])
    connection.commit()
    print('-----Employee Added-----')

def print_employees():
    cursor.execute('SELECT e.id, e.first_name, e.last_name, c.name FROM employees e JOIN companies c On e.company_id = c.id;')
    employees = cursor.fetchall()
    print('----Emploees----')
    if not employees:
        print('-----No Employees Found----')
    else:
        for employee in employees:
            print(f'Id: {employee[0]}, Name: {employee[1]} {employee[2]}, Company: {employee[3]}')

def update_empoyee(id, first, last, company):
    cursor.execute('UPDATE employees SET first_name = %s, last_name = %s, company_id = %s WHERE id = %s;', [first, last, company, id])
    connection.commit()
    print('----Employee Updated----')

def main():
    while True:
        print('---- CRM TOOL ----')
        print('1. Create Company')
        print('2. List Company')
        print('3. Update Company')
        print('4. Delete Company')
        print('5. Create Employee')
        print('6. List Employee')
        print('7. Update Employee')
        print('8. Delete Employee')
        print('9. Exit')

        choice = input('Enter your choice (1-9): ')

        if choice == '1':
            name = input('Enter A Company Name: ')
            industry = ''
            while not industry:
                industry = input(f'Enter {name}s Industry: ')
                if not industry:
                    print('Please Enter Industry')
            create_company(name, industry)
        elif choice == '2':
            print_companies() 
            
        elif choice == '3':
            print_companies()
            company_id = input('Enter the Id of the comapny you want to update: ')
            new_name = input('Enter New Company Name: ')
            new_industry = ''
            while not new_industry:
                new_industry = input(f'Enter {new_name}s Industry: ')
                if not new_industry:
                    print('Please Enter Industry')
            update_company(company_id, new_name, new_industry)
            
        elif choice == '4':
            print_companies()
            delete_company = input('Enter the Id of the company you want to delete: ')
            cursor.execute('DELETE FROM companies WHERE id = %s;', [delete_company])
            connection.commit()
            print('----Company Deleted----')
            print_companies()
        elif choice == '5':
            first_name = input('What is empolyee first name?: ')
            last_name = input('What is employees last name?: ')
            company_id = False
            print_companies()
            while not company_id:
                company_id = input(f'Enter id of {first_name}s company if listed or press Enter to add a new company: ')
                if not company_id:
                    name = input('Enter A Company Name: ') 
                    industry = ''
                    while not industry:
                       industry = input(f'Enter {name}s Industry')
                       if not industry:
                           print('Please Enter Industry')
                    create_company(name, industry)
                    print_companies()
            create_employee(first_name, last_name, company_id)
        elif choice == '6':
            print_employees()
        elif choice == '7':
            print_employees()
            employee_id = input('Enter the Id of the employee to Update: ')
            new_first_name = input('Enter new first name: ')
            new_last_name = input('Enter new last name: ')
            new_company_id = False
            print_companies()
            while not new_company_id:
                new_company_id = input('Enter id of employees company if listed or press Enter to add a new company: ')
                if not new_company_id:
                    name = input('Enter A Company Name: ') 
                    industry = ''
                    while not industry:
                       industry = input(f'Enter {name}s Industry')
                       if not industry:
                           print('Please Enter Industry')
                    create_company(name, industry)
                    print_companies()
            update_empoyee(employee_id, new_first_name, new_last_name, new_company_id)
        elif choice == '8':
            print_employees()
            delete_employee = input('Enter the Id of employee you want to delete: ')
            cursor.execute('DELETE FROM employees WHERE id = %s;', [delete_employee])
            connection.commit()
            print('----Employee Deleted----')
            print_employees
        elif choice == '9':
            print('Exiting CRM')
            break
        else:
             print('Still working')

main()
connection.close()
print('Connection Closed.')