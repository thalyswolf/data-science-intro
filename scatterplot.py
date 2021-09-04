import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 330, 100]

title = "Scatterplot"
x_axis = "X Axis"
y_axis = "Y Axis"


# Legendas
plt.title(title)
plt.xlabel(x_axis)
plt.ylabel(y_axis)

plt.scatter(x, y, label="Points", 
            color="k", marker='.', s=z)

plt.plot(x, y, color='k', linestyle='-.')

plt.legend()

# plt.show()
plt.savefig(".output/fig.png", dpi=1200)