cars = []

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

while True:
    print("RENT CAR")
    print("1. Add car:")
    print("2. View car:")
    print("3. Exit:")

    select = input("Choose a number:")

    if select == "1":
        new_cars()
    elif select == "2":
        view_cars()
    elif select == "3":
        break
    else:
        print("Try again")
print("hola")