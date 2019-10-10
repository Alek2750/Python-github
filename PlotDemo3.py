import matplotlib.pyplot as plt
plt.figure()
x_values = range(1,6)
y_values = [x**2 for x in x_values]
print('Points to be plotted {}'.format(list(zip(x_values,y_values))))

plt.scatter(x_values,y_values, s=100)
plt.show()