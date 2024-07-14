#Импорт библиотек

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.scatter(data=userdata, x="age", y="income", color='green', alpha=0.3)
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Scatter plot of Age vs Income")
plt.show()
