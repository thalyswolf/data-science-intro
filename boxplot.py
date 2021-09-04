# Boxplot - Box Diagram

import matplotlib.pyplot as plt
import random

vector = []

for i in range(10):
    random_number = random.randint(0, 10500)
    vector.append(random_number)


plt.boxplot(vector)
plt.title("Boxplot")
plt.show()
