import sqlite3
con = sqlite3.connect("Cars.db")
from datetime import date

cur = con.cursor()

def cars_view():
    cur.execute("SELECT * FROM Cars")

    filas = cur.fetchall()

    if len(filas) == 0:
        print("NO CARS!")
        return

    for fila in filas:
        print(fila)

def new_cars():
    print(" ")
    Year = input("Car year:")
    print(" ")
    Model = input("Car model:")
    print(" ")
    Brand = input("Car brand:")

    cur.execute("""
    INSERT INTO cars (brand, model, year, state)
    VALUES (?, ?, ?, 'Available')
    """, (Brand, Model, Year))

    con.commit()

    print(" ")
    print("CAR ADDED!")
    print(" ")

def new_customers():
    print(" ")
    Name = input("Customer name:")
    print(" ")
    
    if Name == "":
        print("ENTER A PROPERLY NAME")
        return
    
    cur.execute("INSERT INTO Customers (Name) VALUES (?)",
    (Name,))

    con.commit()
    
    print("CUSTOMER ADDED!")

def view_customers():
    cur.execute("SELECT * FROM Customers")

    filas = cur.fetchall()

    if len(filas) == 0:
        print("NO CUSTOMERS!")
        return

    for fila in filas:
        print(fila)

def view_rents():
    cur.execute("SELECT * FROM Rents")
    filas = cur.fetchall()

    if len(filas) == 0:
        print("NO RENTS!")
        return

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
        
    try: 
        car_id = int(input("Choose car id:"))
    except: 
        print("Type a properly number")
        return   
    
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
    
    try:
        days = int(input("Select the amount of days you want the car:"))
        print(" ")
    except:
        print("ENTER A VALID NUMBER OF DAYS!")
        return
    today = date.today()

    cur.execute("""INSERT INTO Rents (car_id, customer_id, date, days) VALUES (?, ?, ?, ?)""", (car_id, customer_id, today, days))
    cur.execute("""UPDATE Cars SET state = 'Rented' WHERE id = ? """, (car_id,))

    con.commit()
 
    print("Car rented")

def return_car():
    print(" ")
    
    try:
        car_id = int(input("Enter car Id to return:"))
    except:
        print("WRITE AN ID!")
        return 
        
    cur.execute("""UPDATE Cars SET state = 'Available' Where id = ? """, (car_id,))
    con.commit()

    print("Car was perfectly returned")

while True:
    print("")
    print("RENT CAR")
    print("1. Add car:")
    print("2. View car:")
    print("3. Add Customer:")
    print("4. View customers:")
    print("5. Rent car:")
    print("6. Return Car:")
    print("7. View rents:")
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
    elif select == '5':
        rent_car()
    elif select == '6':
        return_car()
    elif select == '7':
        view_rents()
    elif select == '8':
        break
    else:
        print("Try again")