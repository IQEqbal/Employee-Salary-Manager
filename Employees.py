# I used a list to store employee names because there might be duplicate names
staff = []
salaries = []


def choose() : 
    print("""Choose a number
        1 = Add employees
        2 = See all employees 
        3 = Search an employees name 
        4 = Reduce employees' wages
        5 = Deducte employees' salaries based on attendance
        6 = Total wages and Total employees
        7 = Exit the program """)
    
    while True : 
        try :
            option = int(input("Please choose a number : "))
            assert 0 < option < 7
            break
        except AssertionError :
            print("Please select a number")
        except ValueError :
            print("Please enther a number")
            print()
    return option


def caculate_percentage(name , days):
        if name in staff :
            index = staff.index(name)
            name = salaries[index]
            new_wage = name * days
            new_wage /= 30
            return new_wage
        else :
            return f"{name} is not found"  
            
select = choose()    
 
while True :
    
    
    # To add employees
    if select == 1 :
        
        while True :                                           # To take number of employees
            try:
                number_of_employees = int(input("Enter the number of employees : "))
                break
            except ValueError :
                print("you can't enter a word ")
            
            
        for i in range(0,number_of_employees):                  # To take a valid employee name 
            while True :
                try :
                    employee = input("Enter the employee's name : ")
                    assert not any(char.isdigit() for char in employee)
                    break
                except AssertionError :
                    print("Please enter a valid name without numbers ")
            staff.append(employee)
            
            
            while True :                                        # To take a valid wage
                try:
                    wage = int(input(f"{employee}'s wage : "))
                    break
                except ValueError :
                    print(f"Please enter {employee}'s wage")
            salaries.append(wage)
        select = choose()

    # To see all employees
    if select == 2 :
        print()
        for i in range(len(staff)):
            print(staff[i]  ,  salaries[i])
        print()
        select = choose()
            

    # To search for an employee
    if select == 3 :
        print("if you want to exit, type (Exit) or (exit)")
        while True :
            staffCopy = staff[:]
            salaries_copy = salaries[:]
            search_name = input("Search an employess : ")
            while search_name in staffCopy :
                
                index = staffCopy.index(search_name)
                print(f" {staffCopy[index]} wage is {salaries_copy[index]}")
                staffCopy.remove(staffCopy[index])
                salaries_copy.remove(salaries_copy[index])
            
            if search_name == "Exit" or search_name == "exit" :
                break
            if search_name not in staff :
                print("not found")
        print()
        select = choose()   
            
    
        
    # To reduce an employee's wage
    if select == 4 :
        print("Whose salary do you want to reduce? ")
        print("if you're done, type (exit) or (Exit)")
        while True :
            employee = input("Enter the name : ")
            if employee in staff :
                index = staff.index(employee)
                while  True :
                    try :
                        salaries[index] = int(input("Enter the new salary : "))
                        break
                    except ValueError :
                        print("Please enter the employee's salary ")
                print(f"{employee}'s salary is changed to {salaries[index]} ")
            elif employee == "exit" or employee == "Exit" :
                break
            elif employee not in staff :
                print("Not found")
        print()
        select = choose()
        
        
    # To deduct an employee's salary based on attendance
    if select == 5 :
        print("if you're done, type (exit) or (Exit)")
        while True :
            employee = input("Enter the employee's name : ")
            if employee in staff :
                while True :
                    try :
                        days = int(input("Enter the number of days present in a month : "))
                        assert 0 <= days <= 30
                        break
                    except AssertionError :
                        print("A person can't be present for more than 30 days or less than 0 days in a month")
                    except ValueError :
                        print("Please enter the days present ")
                new_wage = caculate_percentage(employee , days)
                print(f"{employee}'s salary for this month is {new_wage}")
            elif employee == "Exit" or employee == "exit" :
                break
            else :
                print("Not found")
           
        print()
        select = choose()
        
        
    # Total wages and total employees
    if select == 6 :
        total_wages = 0
        for i in salaries :
            total_wages += i
        print(f"Total wages : {total_wages}")
        print(f"Total employees : {len(staff)}")
        print()
        select = choose()
        
    # Exit the program
    if select == 7 :
        break
