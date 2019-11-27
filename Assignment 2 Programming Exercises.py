def get_days():
    days = x/24 + y/1440 + z/86400
    print("number of days", round(days,4))


def convert_to_days() :
    global x
    global y
    global z
    x = float(input("Enter number of hours: "))
    y = float(input("Enter number of minutes: "))
    z = float(input("Enter number of seconds: "))
    get_days()
    return x, y, z
convert_to_days()

def calc_weight_on_planet(weight, gravity=23.1) :
    w = weight/9.8 * gravity
    print(w)
calc_weight_on_planet(120, 9.8)
calc_weight_on_planet(120)
calc_weight_on_planet(120, 23.1)

def num_atoms(amount, atomic_weight=196.97) :
    number_of_atoms = 6.022 * (10**23) * (amount/atomic_weight)
    print(number_of_atoms)
num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10, 1.008)

def calc_new_height() :
    x = float(input("Enter the current width: "))
    y = float(input("Enter the current height: "))
    z = float(input("Enter the desired width: "))
    corresponding_height = (z/(x/y))
    print(corresponding_height)
    return x, y, z
calc_new_height()

def convert_temp() :
    temp = int(input("Enter temperature in Fahrenheit: "))
    tc = (5/9)*(temp - 32)
    tk = float(tc + 273.15)
    return tk

print(convert_temp())







