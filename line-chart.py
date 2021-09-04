import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

plt.title('Line chart')

# Eixos
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.plot(x, y)
plt.show()