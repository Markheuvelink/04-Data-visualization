# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:52:10 2024

@author: rbaia
"""

# Exercise runner energy consumption
# The script below provides an example of plotting a function
# Modify this code to plot the function

import matplotlib.pyplot as plt
import numpy as np

# Define the full energy expenditure function
def y(x):
    return 5*x+(0.2*(x**3))
# Generate datapoints for plotting 
x_values = np.linspace(0, 10, 500)    # Generate values of x (500 values of x between 0 and 10)
y_values = y(x_values)                # Compute the y values for the x values generated


# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r"$5x+0.2x^3$")   # Giving a label that appears in the legend (if printed)
plt.title('Energy consumption') #Title of the plot
plt.xlabel("Minutes")                            # Name of the x-axis
plt.ylabel("Calories")                        # Name of the y-axis
plt.xlim([0,5])                                     # Range of x-axis
plt.ylim([0,50])                                    # Range of y-axis
plt.grid(True)                                      # Plotting gridlines
plt.legend(loc='upper left')                        # Plot the legend in the upper left corner
plt.show()
