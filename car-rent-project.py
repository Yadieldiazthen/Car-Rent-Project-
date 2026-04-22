import request
def Car_Api():
    url = "https://carapi.app/api/models/v2"
    response = request.gets(url)
    data = response.json()

    print("Cars from Api")

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

def new_customers():
    name = input("Costumer name:")

    if name == "":
        print("write a properly name")
        return
    customer = {'name': name}
    customers.append(customer)
    print("Costumer added")

def view_customers():
    if len(customers) == 0:
        print("No customers")
    else:
        for i, c in enumerate(customers):
            print(i,"-",c["name"])
        
def rent_car():
    if len(cars) == 0 or len(customers) == 0:
        print("Add a car and a customer")
        return
    
    print("Cars:")
    for i, car in enumerate(cars):
        print(i, car["name"], car['state'])
    try: 
        car_number = int(input("Choose car number:"))
    except: 
        print("Type a properly number")
        return   
    if car_number < 0 or car_number >= len(cars):
        print("Write a properly number")
        return  
    if cars[car_number]['state'] != 'Available':
        print("Car is already rented")
        return 
    print("Customers:")
    for i, c in enumerate(customers):
        print(i, c['name'])
    try:
        customer_number = int(input("Choose customer number:"))
    except:
        print("Choose a properly number:")
        return
    if customer_number < 0 or customer_number >= len(customers):
        print("Incorrect")
        return
    cars[car_number]['state'] = 'Rented'

    rental = {'car': cars[car_number]['name'], 'customer': customers[customer_number]['name']}

    rents.append(rental)
    print("Car rented")

def view_rents():
    if len(rents) == 0:
        print("No rents")
    else:
        for r in rents:
            print(r["customer"], "rented", r["car"])

def return_car():
    print("Cars:")
    for i, car in enumerate(cars):
        print(i, car['name'], car['state'])

    car_number = int(input('Choose you car:'))

    cars[car_number]['state'] = 'Available'
    print("Car was perfectly returned")


while True:
    print("RENT CAR")
    print("1. Add car:")
    print("2. View car:")
    print("3. Add Customer:")
    print("4. View customers:")
    print("5. Rent car:")
    print("6. View rents:")
    print("7. Return Car:")
    print("8. Exit:")

    select = input("Choose a number:")

    if select == "1":
        new_cars()
    elif select == "2":
        view_cars()
    elif select == "3":
        new_customers()
    elif select == "4":
        view_customers()
    elif select == '5':
        rent_car()
    elif select == '6':
        view_rents()
    elif select == '7':
        return_car()
    elif select == '8':
        break
    else:
        print("Try again")