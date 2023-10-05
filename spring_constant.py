import numpy as np
import matplotlib.pyplot as plt

# Experimental data
masses = [20, 40, 60, 80, 100, 120]  # Masses in grams
positions = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1] # Extensions in cm
elongations = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1]  # Extensions in cm

def calculate_spring_constants(masses, elongations):
    """
    Calculate spring constants from mass and extension data.
#Calculation of spring constant
spring_constant = lambda m,x: "ERROR" if x == 0 or m<0 else (m*g)/x
    This function calculates spring constants using the provided mass and extension data and
    the formula (mass * acceleration due to gravity) / extension.
# Given data (mass in grams and extension in centimeters)
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
    # Value of acceleration due to gravity in cm/s^2
    g = 981

    # Calculation of spring constant
    spring_constant = lambda m, x: "ERROR" if x == 0 or m < 0 else (m * g) / x

    # Calculate spring constants
    test_values = map(spring_constant, masses, elongations)
    spring_constants = list(test_values)

    return spring_constants

def plot_mass_vs_extension_with_trendline(masses, elongations):
    """
    Plot a graph of mass vs. extension with a best-fit trendline.

    This function takes experimental data in the form of masses (in grams) and extensions (in centimeters)
    and creates a scatter plot representing the relationship between mass and extension.
    Additionally, it adds a best-fit trendline to the plot.

    Parameters:
        masses_g (list): A list of experimental masses in grams.
        extensions_cm (list): A list of experimental extensions in centimeters.

    Returns:
        None

    Example:
        # Experimental data
        masses = [20, 40, 60, 80, 100, 120]  # Masses in grams
        extensions = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1]  # Extensions in cm

        # Plot mass vs. extension with a best-fit trendline
        plot_mass_vs_extension_with_trendline(masses, extensions)

    Note:
        This function uses the matplotlib library for creating the plot.
        The 'masses_g' and 'extensions_cm' parameters should represent experimental data
        with masses in grams and extensions in centimeters.
    """
    # Fit a linear trendline
    slope, intercept = np.polyfit(masses, elongations, 1)

    # Create a scatter plot of mass vs. extension
    plt.figure(figsize=(8, 6))
    plt.scatter(masses, elongations, color='blue', marker='o', label='Data Points')

    # Plot the best-fit line
    plt.plot(masses, slope * np.array(masses) + intercept, color='red', label='Best-fit Line')

    # Set plot labels and title
    plt.title('Mass vs. Elongation')
    plt.xlabel('Mass (g)')
    plt.ylabel('Elongation (cm)')
    plt.grid(True)
    plt.legend()

    # Display the equation of the best-fit line
    plt.text(0.5, 0.5, f'Equation: y = {slope:.4f}x + {intercept:.4f}', transform=plt.gca().transAxes)

    # Show the plot
    plt.show()

#Printing outputs

# Plot mass vs. extension with a best-fit trendline using the provided function
plot_mass_vs_extension_with_trendline(masses, elongations)

# Calculate spring constants using the provided function
spring_constants = calculate_spring_constants(masses, elongations)

avg = np.average(spring_constants)
print(f"The spring constant of a given spring is {avg:.2f} dyne/cm")
