import spring_const_graph as scg

# Example data
masses = [20, 40, 60, 80, 100, 120]  # Masses in grams
elongations = [2.6, 5.4, 8.2, 10.8, 13.4, 16.1]  # Extensions in cm

scg.plot_mass_vs_extension_with_trendline(masses, elongations, 'best-fit.png')
print("The spring constant of a given spring is", \
      '{:.2e}'.format(float(scg.calculate_spring_constants(masses, elongations))), "N/m")
