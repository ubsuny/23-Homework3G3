import numpy as np
import matplotlib.pyplot as plt

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
    
    avg = np.average(spring_constants)*10**(-3)
    return avg 

def plot_mass_vs_extension_with_trendline(masses, elongations, file_name=None):
      """
    Generate a scatter plot of mass vs. elongation with a best-fit trendline.

    Parameters:
        masses (list): A list of mass values (in grams).
        elongations (list): A list of elongation values (in centimeters).
        file_name (str, optional): The filename to save the plot as an image. \
        If not provided, the plot is displayed but not saved.

    Returns:
        None

    This function fits a linear trendline to the provided mass and elongation data \
    points and creates a scatter plot of the data points along with the best-fit line. \
    It also labels the axes, displays a title, and shows the equation of the best-fit line \
    on the plot. Additionally, it can save the plot as an image if a filename is provided.

    Example usage:
    >>> masses = [1, 2, 3, 4, 5]
    >>> elongations = [2, 4, 5, 4, 6]
    >>> plot_mass_vs_extension_with_trendline(masses, elongations, file_name='mass_vs_extension.png')
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

    # Save the plot as an image if a filename is provided
    if file_name:
        plt.savefig(file_name)
        
    # Show the plot
    plt.show()
