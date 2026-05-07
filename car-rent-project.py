import sqlite3
con = sqlite3.connect("Cars.db")
from datetime import date

cur = con.cursor()

def cars_view():
    cur.execute("SELECT * FROM Cars")

    filas = cur.fetchall()

    for fila in filas:
        print(fila)

def new_cars():
    Year = input("Car year:")
    Model = input("Car model:")
    Brand = input("Car brand:")

    cur.execute("""
    INSERT INTO cars (brand, model, year, state)
    VALUES (?, ?, ?, 'Available')
    """, (Brand, Model, Year))

    con.commit()
    
    print("Car added")

def new_customers():
    Name = input("Customer name:")

    cur.execute("INSERT INTO Customers (Name) VALUES (?)",
    (Name,))

    con.commit()
    
    print("Customer added")

def view_customers():
    cur.execute("SELECT * FROM Customers")

    filas = cur.fetchall()

    for fila in filas:
        print(fila)

def view_rents():
    cur.execute("SELECT * FROM Rents")
    filas = cur.fetchall()

    for fila in filas:
        print(fila)

        
def rent_car():
    cur.execute("SELECT * FROM Cars WHERE state = 'Available' ")
    cars = cur.fetchall()
    
    if len(cars) == 0:
        print("No cars")
        return
    
    print("Cars:")
    for car in cars:
        print(car)


    while True:    
        try: 
            car_id = int(input("Choose car id:"))

            cur.execute('SELECT * FROM Cars WHERE id = ? AND state = "Available"', (car_id, ))
            car = cur.fetchone()
        
            if car is None:
                print('That car does not exist or is not available')
            else:
                break
        
        except: 
            print("Type a properly number")   
    
    cur.execute("SELECT * FROM Customers")
    customers = cur.fetchall()

    if len(customers) == 0:
        print("No customers")
        return  
    
    print("Customers:")
    for custo in customers:
        print(custo)
    
    try:
        customer_id = int(input("Choose customer id:"))
    except:
        print("Choose a properly number:")
        return
    

    while True:
        try:
            days = int(input("How many days?"))

            if days > 0:
                break
            else:
                print("Days must be greater than 0: ")

        except:
            print("Type a valid number")
            
    today = date.today()

    cur.execute("""INSERT INTO Rents (car_id, customer_id, dates, days) VALUES (?, ?, ?, ?)""", (car_id, customer_id, today, days))
    cur.execute("""UPDATE Cars SET state = 'Rented' WHERE id = ? """, (car_id,))

    con.commit()

    print("Car rented")

def return_car():
    car_id = int(input("Enter car Id to return:"))

    cur.execute("""UPDATE Cars SET state = 'Available' Where id = ? """, (car_id,))
    con.commit()
   
    print("Car was perfectly returned")

while True:
    print(' ')
    print("RENT CAR")
    print("1. Add car:")
    print("2. View car:")
    print("3. Add Customer:")
    print("4. View customers:")
    print("5. View rents")
    print("6. Rent car:")
    print("7. Return Car:")
    print("8. Exit:")

    select = input("Choose a number:")

    if select == "1":
        new_cars()
    elif select == "2":
        cars_view()
    elif select == "3":
        new_customers()
    elif select == "4":
        view_customers()
    elif select == "5":
        view_rents()
    elif select == '6':
        rent_car()
    elif select == '7':
        return_car()
    elif select == '8':
        break
    else:
        print("Try again")