#Импорт библиотек

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.barplot(data=df_long_grouped, x='grouped_age', y='count', hue='ad_type')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Count useful actions by age group')
plt.legend(title='Advertisement Type', loc='upper right')
plt.show()
