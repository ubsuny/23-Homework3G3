# Define a list of forces (F) and displacements (x)
forces = [100, 150, 200, 250]
displacements = [0.1, 0.15, 0.2, 0.25]

# Use the map() function with a lambda function to calculate the spring constants
spring_constants = list(map(lambda force, displacement: force / displacement, forces, displacements))

# Print the calculated spring constants
print(spring_constants)

#Output [1000.0, 1000.0, 1000.0, 1000.0]

#Plot code
import matplotlib.pyplot as plt

# Define the data (forces, displacements, and spring constants)
forces = [100, 150, 200, 250]
displacements = [0.1, 0.15, 0.2, 0.25]
spring_constants = [force / displacement for force, displacement in zip(forces, displacements)]

# Create a plot
plt.plot(displacements, spring_constants, marker='o', linestyle='-')

# Add labels and a title
plt.xlabel('Displacement (m)')
plt.ylabel('Spring Constant (N/m)')
plt.title('Spring Constant vs. Displacement')

# Display the plot
plt.grid(True)
plt.show()



    
   
    
   
  
 
