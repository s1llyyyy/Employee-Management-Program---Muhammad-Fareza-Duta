from tabulate import tabulate as tb

employees = {'emp_id' : [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009],
            'name': ['Fareza Duta', 'Angga Valentino', 'Sultan Pasya', 'Fawwaz Purwadhika', 'Namira Azzahra', 'Rara Sinta', 'Yobel Ridwan', 'Nathan Edward', 'Sylvan Gates'],
             'sex' : ['M', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'M'],
             'department' : ['Tech', 'Finance', 'Marketing', 'Tech', 'Marketing', 'Finance', 'Finance', 'Tech', 'Tech'],
             'position' : ['Head', 'Head', 'Head', 'Manager', 'Team Leader', 'Staff', 'Staff', 'Team Leader', 'Staff'],
             'salary' : [8110, 7120, 7280, 5570, 5020, 3510, 3740, 4650, 3440],
             'bonus' : [0, 0, 0, 0, 0, 0, 0, 0, 0]}
take_home_pay = [employees['salary'][i] + employees['bonus'][i] for i in range(len(employees['emp_id']))]


def show_list(): 
    if not employees:
        print("No employees in the system.")
    else:
        print()   
        print(tb(employees, 
                 headers=["Employee ID", "Name", "Sex", "Department", "Position", "Salary (USD)", "Bonus", "Take Home Pay"], tablefmt="github"))
        print()

def menu_1(): # Option 1
    while True:
        try:
            print()
            print("1. Show All Employee Data\n2. Show Employee Data for Specified Department\n3. Back to Main Menu")
            print()
            menu1_confirmation = (input("Enter your choice: "))
            if menu1_confirmation == '1':
                show_list()
                break
            elif menu1_confirmation == '2':
                department = input("Enter the department name you want to show: ").capitalize()
                if department in employees['department']:
                    index = [i for i in range(len(employees['department'])) if employees['department'][i] == department]
                    print()
                    print(f"Employee Data for {department} Department: ")
                    print(tb({
                        'Employee ID': [employees['emp_id'][i] for i in index], 
                        'Name': [employees['name'][i] for i in index], 
                        'Sex': [employees['sex'][i] for i in index],
                        'Department': [employees['department'][i] for i in index], 
                        'Positon': [employees['position'][i]for i in index], 
                        'Salary (USD)': [employees['salary'][i] for i in index], 
                        'Bonus': [employees['bonus'][i] for i in index]}, headers="keys", tablefmt="github"))
                    print()
                    break
                else:
                    print("Invalid department name.")
                    continue
            elif menu1_confirmation == '3':
                main_menu()
            else:
                print("Invalid input. Please enter '1' or '2' ")
        except ValueError:
            print("Invalid input.")



    while True:
        try:
            print("Do you want to show another data?(Y/N): ")
            show_more_confirmation = input("Enter your choice: ").upper()
            if show_more_confirmation == 'Y':
                menu_1()
            elif show_more_confirmation == 'N':
                main_menu()
            else:
                print("Invalid input. Please enter 'Y' or 'N' ")
        except ValueError:
            print("Invalid input.")
    
def add_employee():  # Option 2
    show_list()
    
    while True:
        try:
            print("1. Add Employee\n2. Back to Main Menu\n")
            menu2_confirmation = input("Enter your choice: ")
            print()
            
            if menu2_confirmation == '1':
                break
            elif menu2_confirmation == '2':
                main_menu()
            else:
                print("Invalid input. Please enter '1' or '2'\n")
        except ValueError:
            print("Invalid input.\n")

    while True:
        try:
            emp_id = int(input("Input employee ID (4 Digits): "))
            str_emp_id = str(emp_id)
            
            if emp_id in employees['emp_id']:
                print("Employee ID is taken, please input another Employee ID.\n")
                continue
            elif len(str_emp_id) != 4:
                print("Employee ID invalid, please enter 4 digits only.\n")
                continue
            
            name = input("Enter name: ").title()
            
            while True:
                sex = input("Enter sex (M/F): ").upper()
                if sex in ['M', 'F']:
                    break
                else:
                    print("Incorrect input, please enter M or F.\n")
            
            department = input("Enter department: ")
            position = input("Enter position: ")
            
            while True:
                try:
                    salary = int(input("Enter salary (USD): "))
                    break
                except ValueError:
                    print("Invalid input, please input salary as a number.\n")
            
            while True:
                print()
                print("Y. Add Data\nN. Cancel")
                add_confirmation = input(f"Are you sure you want to add {name}? (Y/N): ").upper()
                if add_confirmation == 'Y':
                    employees['emp_id'].append(emp_id)
                    employees['name'].append(name)
                    employees['sex'].append(sex)
                    employees['department'].append(department)
                    employees['position'].append(position)
                    employees['salary'].append(salary)
                    employees['bonus'].append(0)
                    print("Employee added successfully.\n")
                    break
                elif add_confirmation == 'N':
                    print("Input cancelled. Returning to 'Add Employee Feature'.\n")
                    add_employee()
                else:
                    print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.\n")
            
            while True:
                print()
                add_more_confirmation = input("Do you want to add more employees? (Y/N): ").upper()
                if add_more_confirmation == "Y":
                    add_employee()
                elif add_more_confirmation == "N":
                    main_menu()
                else:
                    print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.\n")
        except ValueError:
            print("Wrong character type, please input again.\n")


def remove_employee(): # Option 3
    show_list()
    while True:
        try:
            print("1. Delete Employee\n2. Back to Main Menu")
            menu3_confirmation = (input("Enter choice: "))
            if menu3_confirmation == '1':
                break
            elif menu3_confirmation == '2':
                main_menu()
            else:
                print("Invalid input. Please enter '1' or '2' ")
        except ValueError:
            print("Invalid input.")

    while True:
        try:
            emp_id = int(input("Enter the employee ID of employee you want to remove: "))
            if emp_id in employees['emp_id']:
                index = employees['emp_id'].index(emp_id)
                print()
                print(f"Are you sure want to delete {employees['name'][index]}? (Y/N): ")
                break
            else:
                print("Invalid employee ID.")
                continue
        except ValueError:
            print("Invalid input.")
            continue

    while True:
        try:
            remove_confirmation = input("Enter choice (Y/N): ").upper()
            if remove_confirmation == 'Y':
                employees['emp_id'].pop(index)
                employees['name'].pop(index)
                employees['sex'].pop(index)
                employees['department'].pop(index)
                employees['position'].pop(index)
                employees['salary'].pop(index)
                employees['bonus'].pop(index)
                print("Employee removed successfully.")
                break
            elif remove_confirmation == 'N':
                print("Input cancelled. Returning to 'Remove Employee Feature'")
                remove_employee()
                break
            else:
                print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.")
                continue
        except ValueError:
            print("Invalid input.")
            continue

    while True:
        try:
            remove_more_confirmation = input("Do you want to remove more employees? (Y/N): ").upper()
            if remove_more_confirmation == 'Y':
                remove_employee()
            elif remove_more_confirmation == 'N':
                main_menu()
            else:
                print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.")
                continue
        except ValueError:
            print("Invalid input.")

def update_data():  # Option 4
    show_list()
    while True:
        try:
            print("1. Update Data\n2. Back to Main Menu")
            menu4_confirmation = (input("Enter choice: "))
            if menu4_confirmation == '1':
                break
            elif menu4_confirmation == '2':
                main_menu()
            else:
                print("Invalid input. Please enter '1' or '2' ")
        except ValueError:
            print("Invalid input.")
    
    while True:
        try:
            print()
            print("Enter the Employee ID of the employee you want to update: ")
            update_id = int(input("Enter Employee ID: "))
            
            if update_id in employees['emp_id']:
                index = employees['emp_id'].index(update_id)
                print()
                print(tb({
                    'Employee ID': [employees['emp_id'][index]], 
                    'Name': [employees['name'][index]], 
                    'Sex': [employees['sex'][index]],
                    'Department': [employees['department'][index]], 
                    'Position': [employees['position'][index]], 
                    'Salary': [employees['salary'][index]], 
                    'Bonus': [employees['bonus'][index]]}, headers="keys", tablefmt="github"))
                print()
                break
            else:
                print("Invalid employee ID.")
                continue
        except ValueError:
            print("Invalid input.")
            continue

    
    while True:
        try:
            print()
            print("1. Update Name\n2. Update Sex\n3. Update Department\n4. Update Position\n5. Update Salary\n6. Cancel Update")
            update = (input("Enter choice: "))
            if update == '1':
                new_name = input("Enter new name: ").title()
                employees['name'][index] = new_name
                print("Name updated successfully.")
                break
            elif update == '2':
                new_sex = input("Enter updated sex(M/F): ").upper()
                employees['sex'][index] = new_sex
                print("Sex updated successfully")
                break
            elif update == '3':
                new_department = input("Enter new department: ").capitalize()
                employees['department'][index] = new_department
                print("Department updated successfully")
                break
            elif update == '4':
                new_position = input("Enter new position: ").capitalize()
                employees['positon'][index] = new_position
                print("Position updated successfully")
                break
            elif update == '5':
                new_salary = int(input("Enter new salary: "))
                employees['salary'][index] = new_salary
                print("Salary updated successfully")
                break
            elif update == '6':
                print("Update cancelled. Returning to 'Update Data Feature'")
                update_data()
                break
            else: 
                print("Invalid input. Please enter '1', '2', '3', '4', '5', or '6' ")
        except ValueError:
            print("Invalid input.")
            continue

    while True: 
        try:
            print()
            update_more_confirmation = input("Do you want to update more data? (Y/N): ").upper()
            if update_more_confirmation == 'Y':
                update_data()
            elif update_more_confirmation == 'N':
                main_menu()
            else:
                print("Invalid input. Please enter 'Y' to update more or 'N' to main menu.")
        except ValueError:
            print("Invalid input.")
            continue

def adjust_salary(): # Option 5
    show_list()

    while True:
        try:
            print()
            print("1. Adjust Salary\n2. Back to Main Menu")
            menu5_confirmation = (input("Enter choice: "))
            if menu5_confirmation == '1':
                break
            elif menu5_confirmation == '2':
                main_menu()
            else:
                print("Invalid input. Please enter '1' or '2' ")
        except ValueError:
            print("Invalid input.")

    while True:
        try:
            print()
            print("1. Adjust All Salary\n2. Adjust One Salary")
            adjust_choice = (input("Enter choice: "))
            if adjust_choice == '1':
                adjust_all_salary()
                break
            elif adjust_choice == '2':
                adjust_one_salary()
                break
            else:
                print("Invalid input. Please enter '1' or '2' ")
        except ValueError:
            print("Invalid input.")
    
    while True:
        try:
            print()
            adjust_more_confirmation = input("Do you want to adjust more salary? (Y/N): ").upper()
            if adjust_more_confirmation == 'Y':
                adjust_salary()
                break
            elif adjust_more_confirmation == 'N':
                main_menu()
            else:
                print("Invalid input. Please enter 'Y' to adjust more or 'N' to main menu.")
        except ValueError:
            print("Invalid Input")
            
def adjust_all_salary(): 
    while True:
        try:
            print()
            print("1. Add Salary\n2. Reduce Salary")
            adjust_all_choice = input("Enter choice: ")
            if adjust_all_choice == '1':
                try:
                    add_salary = int(input("Enter the amount of salary you want to add: ")) 
                    print(f"Are you sure you want to add {add_salary} to all employees? (Y/N): ")
                    print("Y. Add Salary\nN. Cancel")
                    add_confirmation = input("Input choice (Y/N): ")
                    if add_confirmation == 'Y':
                        for i in range(len(employees['emp_id'])):
                            employees['salary'][i] += add_salary
                        print("Salary adjusted successfully for all employees.")
                        break
                    elif add_confirmation == 'N':
                        print("Input cancelled. Returning to 'Adjust Salary Feature'")
                        break
                    else:
                        print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.")
                except ValueError:
                    print("Invalid input.")
            elif adjust_all_choice == '2':
                try:
                    reduce_salary = int(input("Enter the amount of salary you want to reduce: "))
                    print(f"Are you sure you want to reduce {reduce_salary} from all employees? (Y/N): ")
                    print("Y. Reduce Salary\nN. Cancel")
                    reduce_confirmation = input("Input choice (Y/N): ")
                    if reduce_confirmation == 'Y':
                        for i in range(len(employees['emp_id'])): 
                            employees['salary'][i] -= reduce_salary
                        print("Salary adjusted successfully for all employees.")
                        break
                    elif reduce_confirmation == 'N':
                        print("Input cancelled. Returning to 'Adjust Salary Feature'")
                        break
                    else:
                        print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.")
                except ValueError:
                    print("Invalid input.")
            else:
                print("Invalid input. Please enter '1' or '2'")
        except ValueError:
            print("Invalid input.")

def adjust_one_salary(): 
    show_list()
    while True:
        try:       
            emp_id = int(input("Enter the employee ID of employee you want to adjust: "))
            if emp_id in employees['emp_id']:
                index = employees['emp_id'].index(emp_id)
                new_salary = int(input(f"Enter the new salary for {employees['name'][index]}: "))
                while True:
                    adjust_one_salary_confirmation = input(f"Are you sure you want to adjust salary for {employees['name'][employees['emp_id'].index(emp_id)]}? (Y/N): ")
                    if adjust_one_salary_confirmation == "Y":
                        employees['salary'][index] = new_salary
                        print(f"Salary adjusted successfully for {employees['name'][index]}.")
                        break  
                    elif adjust_one_salary_confirmation == "N":
                        print("Input cancelled. Returning to 'Adjust Salary Feature'")
                        break 
                    else:
                        print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.")
                break  
            else:
                print("Invalid employee ID.")
        except ValueError:
            print("Invalid input.")


def add_bonus(): # Option 6
    show_list()
    while True:
        try:
            print()
            print("1. Add Bonus\n2. Back to Main Menu")
            menu6_confirmation = input("Enter your choice: ")
            if menu6_confirmation == '1':
                break
            elif menu6_confirmation == '2':
                main_menu()
            else:
                print("Invalid input. Please enter '1' or '2' ")
        except ValueError:
            print("Invalid input.")
    
    while True:
        try:
            print()
            print("1. Add Bonus to All Employees\n2. Add Bonus to One Employee")
            bonus_choice = input("Enter your choice: ")
            if bonus_choice == '1':
                add_bonus_all()
                break
            elif bonus_choice == '2':
                add_bonus_one()
                break
            else:
                print("Invalid input. Please enter '1' or '2' ")
        except ValueError:
            print("Invalid input.")

    while True:
        try:
            print()
            check_more_confirmation = input("Do you want to add more bonus? (Y/N): ")
            if check_more_confirmation == 'Y':
                add_bonus()
            elif check_more_confirmation == 'N':
                main_menu()
            else:
                print("Invalid input. Please enter 'Y' to add more or 'N' to main menu.")
        except ValueError:
            print("Invalid input")

def add_bonus_all(): # Option 6.1
    while True:
        try:
            print()
            bonus = int(input("Enter the amount of bonus you want to add: ")) 
            print(f"Are you sure you want to add {bonus} to all employees? (Y/N): ")
            print("Y. Add Bonus\nN. Cancel")
            add_bonus_confirmation = input("Input your choice (Y/N): ")
            if add_bonus_confirmation == 'Y':
                for i in range(len(employees['emp_id'])):
                    employees['bonus'][i] += bonus
                print("Bonus added successfully for all employees.")
                break
            elif add_bonus_confirmation == 'N':
                print("Input cancelled. Returning to 'Add Bonus Feature'")
                add_bonus()
                break
            else:
                print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.")
        except ValueError:
            print("Invalid input.")
            continue

def add_bonus_one(): # Option 6.2
    show_list()
    while True:
        try:
            print()
            emp_id = int(input("Enter the employee ID of the employee you want to add bonus to: "))
            if emp_id in employees['emp_id']:
                index = employees['emp_id'].index(emp_id)
                bonus = int(input(f"Enter the bonus for {employees['name'][index]}: "))
            else:
                print("Invalid employee ID.")
                continue
            
            while True:
                try:
                    print()
                    add_bonus_one_confirmation = input(f"Are you sure you want to add bonus for {employees['name'][index]}? (Y/N): ")
                    if add_bonus_one_confirmation.upper() == 'Y':
                        employees['bonus'][index] += bonus
                        print(f"Bonus added successfully for {employees['name'][index]}.")
                        break  
                    elif add_bonus_one_confirmation.upper() == 'N':
                        print("Input cancelled. Returning to 'Add Bonus Feature'")
                        add_bonus()
                    else:
                        print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.")
                except ValueError:
                    print("Invalid input.")
                    continue
            break
        except ValueError:
            print("Invalid input.")
            continue



def check_thp(): # Option 7
    print()
    global take_home_pay
    take_home_pay = [employees['salary'][i] + employees['bonus'][i] for i in range(len(employees['emp_id']))]
    while True:
        try:
            print()
            print("1. Check Take Home Pay\n2. Back to Main Menu")
            menu7_confirmation = input("Enter your choice: ")
            print()
            if menu7_confirmation == '1':
                break
            elif menu7_confirmation == '2':
                main_menu()
            else:
                print("Invalid input. Please enter '1' or '2' ")
        except ValueError:
            print("Invalid input.")
    
    while True:
        try:
            print()
            print("1. Check Take Home Pay for All Employees\n2. Check Take Home Pay for Specified Department\n3. Check Take Home Pay for One Employee")
            thp_choice = (input("Enter your choice: "))
            if thp_choice == '1':
                check_thp_all()
                break
            elif thp_choice == '2':
                check_thp_department()
                break
            elif thp_choice == '3':
                check_thp_one()
                break
            else:
                print("Invalid input. Please enter '1', '2', or '3'")
        except ValueError:
            print("Invalid input.")
    
    while True:
            try:
                print()
                check_more_confirmation = input("Do you want to check more THP? (Y/N): ")
                if check_more_confirmation == 'Y':
                    check_thp()
                elif check_more_confirmation == 'N':
                    main_menu()
                else:
                    print("Invalid input. Please enter 'Y' to check more or 'N' to main menu.")
            except ValueError:
                print("Invalid input")


def check_thp_all(): # Option 7.1
    print()
    print(tb({'emp_id': employees['emp_id'], 'name': employees['name'], 'salary': employees['salary'], 'bonus': employees['bonus'], 'take_home_pay': take_home_pay}, headers="keys", tablefmt="github"))
    print()

def check_thp_department(): # Option 7.2
    while True:
        try:
            print()
            department = input("Enter the department name you want to check: ").capitalize()
            if department in employees['department']:
                index = [i for i in range(len(employees['department'])) if employees['department'][i] == department]
                print()
                print(tb({
                    'emp_id': [employees['emp_id'][i] for i in index], 
                    'name': [employees['name'][i] for i in index], 
                    'department': [employees['department'][i] for i in index], 
                    'position': [employees['position'][i]for i in index], 
                    'salary': [employees['salary'][i] for i in index], 
                    'bonus': [employees['bonus'][i] for i in index], 
                    'take_home_pay': [take_home_pay[i] for i in index]}, headers="keys", tablefmt="github"))
                print()
                break
            else:
                print("Invalid department name.")
                continue
        except ValueError:
            print("Invalid input.")

def check_thp_one(): # Option 7.3
    while True:
        try:
            print()
            emp_id = int(input("Enter the employee ID of employee you want to check: "))
            if emp_id in employees['emp_id']:
                index = employees['emp_id'].index(emp_id)
                print()
                print(tb({'emp_id': [employees['emp_id'][index]], 'name': [employees['name'][index]], 'salary': [employees['salary'][index]], 'bonus': [employees['bonus'][index]], 'take_home_pay': [take_home_pay[index]]}, headers="keys", tablefmt="github"))
                print()
                break
            else:
                print("Invalid employee ID.")
                continue
        except ValueError:
            print("Invalid input.")
        continue


def main_menu():
    try:
        while True:
            print("\nEmployee Management System")
            print("1. Show List")
            print("2. Add Employee")
            print("3. Remove Employee")
            print("4. Update Data")
            print("5. Adjust Salary")
            print("6. Add Bonus")
            print("7. Check Take Home Pay")
            print("8. Exit Program")
            choice = input("Enter your choice: ")

            if choice == '1':
                menu_1()
            elif choice == '2':
                add_employee()
            elif choice == '3':
                remove_employee()
            elif choice == '4':
                update_data()
            elif choice == '5':
                adjust_salary()
            elif choice == '6':
                add_bonus()
            elif choice == '7':
                check_thp()
            elif choice == '8':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input")
        
        
        

main_menu()
