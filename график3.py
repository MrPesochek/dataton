orderdata = orderdata.pivot_table(index="userId", columns='category', values="avg_bill", fill_value=0).reset_index()

merge_df = pd.merge(left=userdata, right=orderdata, left_on="userid", right_on="userId")

grouped_avg = merge_df.groupby('grouped_age').mean(numeric_only=True).reset_index()

df_long = grouped_avg.melt(id_vars=['grouped_age'], value_vars=['alcohol', 'fish', 'fruits', 'meat', 'other', 'sweets', 'vegetables'],
                          var_name='category', value_name='average_spent')

age_order = ['10-18', '18-26', '34-42', '42-50', '50-58', '58-66', '66-74']

plt.figure(figsize=(12, 8))
sns.barplot(data=df_long, x='grouped_age', y='average_spent', hue='category', order=age_order)
plt.xlabel('Age Group')
plt.ylabel('Average Spent')
plt.title('Average Spending by Age Group and Category')
plt.legend(title='Category', loc='upper right')
plt.xticks(rotation=45)
plt.show()
