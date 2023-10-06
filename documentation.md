# <ins>**Spring Constant**</ins>
The spring constant, denoted as "**k**," is a fundamental property of a spring that quantifies its stiffness or rigidity. It defines the relationship between the force applied to a spring and the amount of deformation (either compression or extension) the spring undergoes in response to that force. In mathematical terms, the spring constant is described by Hooke's Law:
$$F = -kx$$
Where:
- F represents the force applied to the spring, measured in Newtons (N).
- k is the spring constant, measured in Newtons per meter (N/m).
- x is the deformation or displacement of the spring from its equilibrium position, measured in meters (m).

The negative sign indicates that the force exerted by the spring is in the opposite direction of the displacement.

## <ins>Experimental Overview:</ins>
In this experiment, we use a spring to investigate the relationship between mass and extension, aiming to determine the spring constants and validate Hooke's law.

We placed various masses on the spring and noted its elongations. We collected experimental data with two main variables:

| **Masses (grams)**             | 20   | 40  | 60  | 80    | 100  | 120  |
|--------------------------------|------|-----|-----|-------|------|------|
| **Elongations (centimeters)**  | 2.6  | 5.4 | 8.2 | 10.8  | 13.4 | 16.1 |

To calculate the spring constants (k), we use the formula:
$$k = \frac{mg}{x}$$
By applying this formula to each mass-extension pair, we obtain a set of spring constants.
​After analyzing the experimental data, we calculate the spring constants, resulting in values such as:

7.55.15,7.27,7.18,7.23,7.32,7.31 N/m which in 7.32 N/m on average.

## <ins>Hooke's Law Validation:</ins>

We aim to validate Hooke's law, which predicts that the relationship between mass and elongation should yield a straight line on a graph. In our case, we plot a graph of mass (in grams) vs. elongation (in centimeters).
![best-fit-graph](https://github.com/s4il3sh/23-Homework3G3/assets/144289804/b1679bd9-b539-4450-a299-54aed1d31e3a)

## <ins>Computational Work</ins>
- We used the lambda function along with map and list concepts to calculate the spring constants from the given data of masses and elongation.
- We plotted the graph using Matplotlib and drew a best-fit line using polyfit from the numpy library.
- We separated our algorithm and created a file named - python spring_const_graph.py
- Also, we made main.py using our own modules (spring_const_graph.py) and ran the file using our experimental data into it.

### (i) lambda function, list, and map
We use lambda function mass (m) and elongation (x) as inputs to determine the spring constant (k). Also, we used list and map to obtain all the values of spring constants for respective masses.

### (ii) New module created
We created a new module named sping_const_graph.py that contains two functions - calculate_spring_constants() and plot_mass_vs_extension_with_trendline(). 

#### a. calculate_spring_constants()
This is the main function that integrates the lambda function. It takes two inputs -- masses and elongations and returns spring constants of respective masses.

#### b. plot_mass_vs_extension_with_trendline()
This function also takes two inputs -- masses and elongations and creates a scatter plot representing the relationship between mass and elongation. Additionally, it adds a best-fit trendline to the plot.

### New python file created
The file (main.py) uses the created module spring_const_graph and imports it to run our given data and gives us the output i.e. spring constant and a graph showing the relation between mass and its respective elongation.

### Output of pycodestyle main.py file
```python
%reload_ext pycodestyle_magic
```


```python
%%pycodestyle

import spring_const_graph as scg

# Example data
masses = [20, 40, 60, 80, 100, 120]  # Masses in grams
positions = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1] # Extensions in cm
elongations = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1]  # Extensions in cm

scg.plot_mass_vs_extension_with_trendline(masses, elongations)
scg.calculate_spring_constants(masses, elongations)
```

    7:46: E261 at least two spaces before inline comment
    12:1: W391 blank line at end of file

### Output of pycodestyle spring_const_graph.py file
```python
%%pycodestyle

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
    output = print("The spring constant of a given spring is", '{:.2e}'.format(float(avg)), "N/m")
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

    6:1: E302 expected 2 blank lines, found 1
    11:80: E501 line too long (92 > 79 characters)
    16:80: E501 line too long (110 > 79 characters)
    21:80: E501 line too long (115 > 79 characters)
    32:5: E731 do not assign a lambda expression, use a def
    37:1: W293 blank line contains whitespace
    39:80: E501 line too long (98 > 79 characters)
    40:18: W291 trailing whitespace
    42:1: E302 expected 2 blank lines, found 1
    46:80: E501 line too long (106 > 79 characters)
    47:80: E501 line too long (88 > 79 characters)
    67:80: E501 line too long (88 > 79 characters)
    75:80: E501 line too long (83 > 79 characters)
    78:80: E501 line too long (94 > 79 characters)
    88:80: E501 line too long (102 > 79 characters)
    92:1: W391 blank line at end of file
    
## <ins>References:</ins>
1. [Hooke's Law from Wikipedia](https://en.wikipedia.org/wiki/Hooke%27s_law)
2. [Tutorial from Python](https://docs.python.org/3/tutorial/)
3. [ChatGPT](https://chat.openai.com/)
4. [Bard](https://bard.google.com)
