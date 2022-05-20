n = int(input())

parking = set()
for i in range(n):
    data = input().split(", ")
    command = data[0]
    car_reg = data[1]
    if command == "IN":
        parking.add(car_reg)
    elif command == "OUT":
        parking.remove(car_reg)


if parking:
    [print(car) for car in parking]
else:
    print("Parking Lot is Empty")
