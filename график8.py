#Импорт библиотек

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = interactiondata.groupby('grouped_date')['complain_count'].sum().reset_index()
sns.barplot(x='grouped_date', y='complain_count', data=df)
plt.xlabel('Last order date')
plt.ylabel('Complains count')
plt.title('Complain counts by last order date')
plt.xticks(rotation=45)
plt.show()
