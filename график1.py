#Группировка по возрасту
def group_age(age):
   for i in range(10, 76, 8):
       if i <= age <= i + 8:
           return f"{i}-{i+8}"
  
userdata["grouped_age"] = userdata["age"].apply(group_age)
#Мерджим userdata и interactiondata по userid
merged_df = pd.merge(userdata, interactiondata, left_on="userid", right_on="UserId")
#Определим, какая возрастная категория заказывает чаще
df = merged_df.groupby('grouped_age')['avg_purchases_count'].sum().reset_index()
sns.barplot(x="grouped_age", y="avg_purchases_count", data=df)
plt.xlabel('Age group')
plt.ylabel('Avarage count purchases')
plt.title('Purchases per age')
plt.show()
