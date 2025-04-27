import psycopg2

connection = psycopg2.connect(database='management')
# print('connected')


def db_search():
    user_input = input('Please select employee or company to search: ')
    print(user_input)
    if user_input == 'employee':
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE first_name = %s AND last_name = %s", (first_name, last_name))
        # print(cursor.fetchall())
        results = cursor.fetchall()
        if results:
            print(results)
        else:
            print('No employee found by that first and last name.')

    elif user_input == 'company':
          name = input('Company name: ').strip()
          cursor = connection.cursor()
          cursor.execute("SELECT * FROM companies WHERE name = %s", (name,))
          results = cursor.fetchall()
          if results:
            print(results)
          else:
            print('No company found by that name.')

    else:
        print("Please provide a valid request")
        

def db_add():
    user_input = input("Please select 'add employee' or 'add company' to add: ")
    print(user_input)
    if user_input == 'add employee':
        company_id = input("Company ID: ").strip()
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        email = input("Email: ").strip()
        job_title = input("Job title: ").strip()
        hire_date = input("Hire date (YYYY-MM-DD): ").strip()
        salary = input("Salary").strip()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (company_id, first_name, last_name, email, job_title, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)", [company_id, first_name, last_name, email, job_title, hire_date, salary])
        connection.commit()
        print('New employee added.') 

    elif user_input == 'add company':
        name       = input("Company name: ").strip()
        industry   = input("Industry: ").strip()
        headquarters = input("Headquarters: ").strip()
        founded_date = input("Founded date (YYYY-MM-DD): ").strip()
        website    = input("Website URL: ").strip()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO companies (name, industry, headquarters, founded_date, website) VALUES (%s, %s, %s, %s, %s)", [name, industry, headquarters, founded_date, website])
        connection.commit()
        print('New company added.')

    else:
        print("Please provide a valid request")

def db_update():
    user_input =input("Please select 'update employee' or 'update company' to update: ")
    print(user_input)
    if user_input == 'update employee':
        company_id = input("Company ID: ").strip()
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        email = input("Email: ").strip()
        job_title = input("Job title: ").strip()
        hire_date = input("Hire date (YYYY-MM-DD): ").strip()
        salary = input("Salary").strip()
        id = input("ID").strip()
        cursor = connection.cursor()
        cursor.execute("UPDATE employees SET company_id = %s, first_name = %s, last_name = %s, email = %s, job_title = %s, hire_date = %s, salary = %s WHERE id = %s", [company_id, first_name, last_name, email, job_title, hire_date, salary, id])
        connection.commit()
        print('Employee updated.')

    elif user_input == 'update company':
        name       = input("Company name: ").strip()
        industry   = input("Industry: ").strip()
        headquarters         = input("Headquarters: ").strip()
        founded_date    = input("Founded date (YYYY-MM-DD): ").strip()
        website    = input("Website URL: ").strip()
        id = input("ID: ").strip()
        cursor = connection.cursor()
        cursor.execute("UPDATE companies SET name = %s, industry = %s, headquarters = %s, founded_date = %s, website = %s WHERE id = %s", [name, industry, headquarters, founded_date, website, id])
        connection.commit()
        print('Company updated.')

    else:
        print("Please provide a valid request")

def db_delete():
    user_input =input("Please select 'delete employee' or 'delete company' to delete: ")
    print(user_input)
    if user_input == 'delete employee':
        id = input('Employee ID: ').strip()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE id = %s", [id])
        connection.commit()
        print('Employee deleted.')

    elif user_input == 'delete company':
        id = input('Company ID: ').strip()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM companies WHERE id = %s", [id])
        connection.commit()
        print('Company deleted.')

    else:
        print("Please provide a valid request")

user_input = input('How can we we help you today? 1-Search 2-Add 3-Update 4-Delete ')
if user_input == '1':
    db_search()
elif user_input == '2':
    db_add()
elif user_input =='3':
    db_update()
elif user_input == '4':
    db_delete()
else:
    print("Please provide a valid request")


connection.close()