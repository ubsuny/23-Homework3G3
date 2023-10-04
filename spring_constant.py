import numpy as np

# value of acceleration due to gravity in $cm/s^2$
g = 981

#Calculation of spring constant
spring_constant = lambda m,x: "ERROR" if x == 0 or m<0 else (m*g)/x

# Given data (mass in grams and extension in centimeters)
masses = [20, 40, 60, 80, 100, 120]  # Masses in grams
positions = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1] # Extensions in cm

#Printing output
test_values = map(spring_constant, masses, positions)
spring_constants = list(test_values)
print(spring_constants)
