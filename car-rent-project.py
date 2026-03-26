cars = []

def new_cars():
    name = input("Car name:")

    car = {"Car name:":name, "Car state": "Available"}

    cars.append(car)
    print("Car added")