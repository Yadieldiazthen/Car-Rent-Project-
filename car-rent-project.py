cars = []
customers = []
rents = []

def new_cars():
    name = input("Car name:")

    car = {"name":name, "state": "Available"}

    cars.append(car)
    print("Car added")

def view_cars():
    if len(cars) == 0:
        print("No cars")
    else:
        for car in cars:
            print(car["name"], "is", car["state"])

def new_costumer():
    name = input("Costumer name:")

    if name == "":
        print("write a properly name")
        return
    
    costumer = {"name": name}
    costumer.append(costumer)
    print("Costumer added")

def view_customers():
    if len(customers) == 0:
        print("No customers")
    else:
        for i, c in enumerate(customers):
            print(i,"-",c["name"])
        
while True:
    print("RENT CAR")
    print("1. Add car:")
    print("2. View car:")
    print("3. Add Customer:")
    print("4. View customers")
    print("5. Exit:")

    select = input("Choose a number:")

    if select == "1":
        new_cars()
    elif select == "2":
        view_cars()
    elif select == "3":
        new_costumer()
    elif select == "4":
        view_customers()
    elif select == '5':
        break
    else:
        print("Try again")