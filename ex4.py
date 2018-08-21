# define the variable cars
cars = 100

# define the variable space_in_a_car
space_in_a_car = 4.0

# define the variable drivers
drivers = 30

# define the variable passengers
passengers = 90

# define the variable cars_not_driven
cars_not_driven = cars - drivers

# define the variable cars_driven as equal to drivers
cars_driven = drivers

# define the variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car

# define the variable average_passengers_in_a_car
average_passengers_in_a_car = passengers / cars_driven

# line 20 defines the variable carpool_capacity. average_passengers_in_a_car = car_pool_capacity / passenger
# would return an error becaus both the variables 'car_pool_capacity' and 'passenger' are not defined

# print the string "There are" and the value of the variable cars and the string "cars available"
print ("There are", (cars), "cars available" )
print ("There are only", (drivers), "drivers available")
print ("There will be", (cars_not_driven), "empty cars today.")
print ("We can transport", (carpool_capacity), "people today.")
print ("We have", (passengers), "to carpool today.")
print ("We need to put about", (average_passengers_in_a_car), "in each car.")