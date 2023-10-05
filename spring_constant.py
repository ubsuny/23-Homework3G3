import numpy as np

def calculate_spring_constants(masses, elongations):
    """
    Calculate spring constants from mass and extension data.

    This function calculates spring constants using the provided mass and extension data and
    the formula (mass * acceleration due to gravity) / extension.

    Parameters:
        masses (list): A list of masses (in grams) placed on the spring.
        elongations (list): A list of extensions (in centimeters) of the spring from its equilibrium position.

    Returns:
        list: A list of calculated spring constants.

    Note:
        The function assumes that the value of 'g' is approximately 981 cm/s^2.
        If an extension is zero or the mass is negative, "ERROR" is returned for the corresponding spring constant.

    Example:
        masses = [20, 40, 60, 80, 100, 120]  # Masses in grams
        elongations = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1]  # Extensions in cm
        spring_constants = calculate_spring_constants(masses, elongations)
        # spring_constants will contain the calculated spring constants.
    """
    # Value of acceleration due to gravity in $cm/s^2$
    g = 981

    # Calculation of spring constant
    spring_constant = lambda m, x: "ERROR" if x == 0 or m < 0 else (m * g) / x

    # Calculate spring constants
    test_values = map(spring_constant, masses, elongations)
    spring_constants = list(test_values)

    return spring_constants

# Example data
masses = [20, 40, 60, 80, 100, 120]  # Masses in grams
elongations = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1]  # Extensions in cm

# Calculate spring constants using the provided function
spring_constants = calculate_spring_constants(masses, elongations)

for i in range(len(spring_constants)):
    print(f"The spring constant (k) is approximately {spring_constants[i]:.2f} dyne/cm")
