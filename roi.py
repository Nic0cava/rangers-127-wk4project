class User():
    id_counter = 1 #class attribute 
    def __init__(self, username, password):
        self.username = username
        self.password = password[::-2]
        self.id = User.id_counter
        User.id_counter += 1
        
    def __str__(self):
        formatted_user = f"""
        {self.id} - {self.username.title()}
        pw: {self.password}      
        """
        return formatted_user
    
    def __repr__(self):
        return f"<User {self.id} | {self.username}>"
    
    def check_password(self, password_guess):
        return self.password == password_guess[::-2]

    def view(self):
        print(self.property_list)

class Property():
    id_counter = 1 #class attribute 
    def __init__(self, purchase_price, rental_income, total_expenses, total_investment):
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.total_expenses = total_expenses
        self.total_investment = total_investment
        self.property_list = []
        self.prop = []
        self.id = Property.id_counter
        Property.id_counter += 1

    def ROI(self):
        cash_flow = self.rental_income - self.total_expenses 
        annual_cash_flow = cash_flow * 12
        self.ROI = (annual_cash_flow / self.total_investment) * 100
        self.prop.append(self.ROI)
        return f"The ROI for this property is {self.ROI}%"

    def add(self):
        self.prop.append(self.id)
        self.prop.append(self.purchase_price)
        self.prop.append(self.rental_income)
        self.prop.append(self.total_expenses)
        self.prop.append(self.total_investment)
        self.property_list.append(self.prop)

    def view(self):
        return self.property_list
    



class Program():
    def __init__(self):
        self.users = set()       
        self.current_user = None
        
    #add a user
    def add_user(self):
        username = input("Please enter a username: ")
        
        if username in {u.username for u in self.users}:
            print("User with that name already exists. Please try again!") # 409 Error, conflict in request
        else:
            password = input("Please enter your password. ")
            user = User(username, password)
            self.users.add(user)
            print(f"{username} has been created!!!")            
        
        
     
        self.login_user()
        
    #choose a user
    def login_user(self):
        username = input("What is your username? ")
        password = input("What is your password? ")

        for user in self.users:
            if user.username == username and user.check_password(password):
                self.current_user = user
                print(f"{username} has logged in")
                break
        else:
            print("Username and/or password is incorrect")
            
    def logout(self):
        self.current_user = None
        print("You have succesfully been logged out!")
        
    def update_user(self):
        
        if self.current_user:
            print(self.current_user)
            new_user = input("Please enter the updated username or enter skip to keep your current username")
            if new_user.lower() != 'skip':
                self.current_user.username = new_user
            new_pw = input("Please enter the updated password or enter skip to keep current password")
            if new_pw.lower() != 'skip':
                self.current_user.password = new_pw
            print(f"{self.current_user.username}'s info has been updated")
            
        else:
            print('please login to update user')
            self.login_user()

    #add property
    def add_property(self):
        
        purchase_price = int(input("Enter property purchase price: "))
        rental_income = int(input("Enter rental_income: "))
        total_expenses = int(input("Enter total expenses: "))
        total_investment = int(input("Enter total investment: "))
        self.property = Property(purchase_price, rental_income, total_expenses, total_investment)

        self.property.add()
        print(f"Your property has been added to your property list!")
        print(f"Your properties: {self.property.view()}")
        print(self.property.ROI())

     #view properties
    def view_properties(self):
        print(f"Your properties: {self.property.view()}")

    
         # run function to drive the program
    def run(self):
        """
        Method allowing users to interact with program
        """
        
        if self.users:
            self.choose_user()
        else:
            self.add_user()            
            
            print("""            
            What would you like to do?            
            Add - add a new user
            Login - login to your profile
            Update - update user info
            Logout - logout of your profile                       
            View - view properties
            New - Add property & calculate ROI
            Quit - close the application           
            
            """)
            
        while True:
            response = input("What would you like to do? (add, update, login, logout, new, view, quit) ")
            
            
            if response.lower() == "add":
                self.add_user()
            elif response.lower() == 'logout':
                self.logout()
                new_response = input("What would you like to do next? login, add, quit")
                if new_response.lower() == 'add':
                    self.add_user()
                elif new_response.lower() == 'login':
                    self.login_user()
                elif new_response.lower() == 'quit':
                    print("Have a great day!")
                    break
                else:
                    print("Please enter a valid response and try again!")
            elif response.lower() == 'login':
                self.login_user()
            elif response.lower() == "update":
                self.update_user()
            elif response.lower() == "new":
                self.add_property()
            elif response.lower() == "view":
                self.view_properties()
            elif response.lower() == "quit":
                print(f"Have a great day!")
                break
            else:
                print("Invalid Input: please choose from the list!")
        
        

program = Program()

program.run()




