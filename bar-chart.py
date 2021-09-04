import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

title = "Bar chart"
x_axis = "X Axis"
y_axis = "Y Axis"


plt.title(title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)


plt.bar(x, y)
plt.show()
