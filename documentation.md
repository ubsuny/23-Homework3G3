# **Spring Constant**
The spring constant, denoted as "**k**," is a fundamental property of a spring that quantifies its stiffness or rigidity. It defines the relationship between the force applied to a spring and the amount of deformation (either compression or extension) the spring undergoes in response to that force. In mathematical terms, the spring constant is described by Hooke's Law:
$$F = -kx$$
Where:
- F represents the force applied to the spring, measured in Newtons (N).
- k is the spring constant, measured in Newtons per meter (N/m).
- x is the deformation or displacement of the spring from its equilibrium position, measured in meters (m).

The negative sign indicates that the force exerted by the spring is in the opposite direction of the displacement.

## Experiment Overview:
In this experiment, we use a spring to investigate the relationship between mass and extension, aiming to determine the spring constants and validate Hooke's law.

We placed various masses on the spring and noted its elongations. We collected experimental data with two main variables:

| **Masses (grams)**             | 20   | 40  | 60  | 80    | 100  | 120  |
|--------------------------------|------|-----|-----|-------|------|------|
| **Elongations (centimeters)**  | 2.6  | 5.4 | 8.2 | 10.8  | 13.4 | 16.1 |

To calculate the spring constants (k), we use the formula:
$$k = \frac{mg}{x}$$
By applying this formula to each mass-extension pair, we obtain a set of spring constants.
​After analyzing the experimental data, we calculate the spring constants, resulting in values such as:

7546.15,7266.67,7178.05,7266.67,7320.90,7311.80 dyne/cm

on average we obtain 7298.34 dyne/cm as a spring constant.

## Hooke's Law Validation:

We aim to validate Hooke's law, which predicts that the relationship between mass and elongation should yield a straight line on a graph. In our case, we plot a graph of mass (in grams) vs. elongation (in centimeters).
![best-fit-graph](https://github.com/s4il3sh/23-Homework3G3/assets/144289804/b1679bd9-b539-4450-a299-54aed1d31e3a)

## Computational Work
- We used the lambda function to calculate the spring constants from the given data of masses and elongation.
- We plotted the graph using Matplotlib and drew a best-fit line using polyfit from the numpy library.
- We separated our algorithm and created a file named - python spring_const_graph.py
- Also, we made main_run.py using our own modules (spring_const_graph.py) and ran the file using our experimental data into it.
  
Here is the code of main_run.py file.
```python
import spring_const_graph as scg

# Example data
masses = [20, 40, 60, 80, 100, 120]  # Masses in grams
positions = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1] # Extensions in cm
elongations = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1]  # Extensions in cm

scg.plot_mass_vs_extension_with_trendline(masses, elongations)
scg.calculate_spring_constants(masses, elongations)
```

Here is our module file spring_const_graph.py
```python
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
    
    avg = np.average(spring_constants)
    output = print(f"The spring constant of a given spring is {avg:.2f} dyne/cm")

    return output 

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
```

### References:
1. [Hooke's Law](https://en.wikipedia.org/wiki/Hooke%27s_law)
2. [ChatGPT](https://chat.openai.com/)
3. [Bard](https://bard.google.com)
4. [Tutorial from Python](https://docs.python.org/3/tutorial/)
