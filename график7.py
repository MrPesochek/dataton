#определим, какая категория людей возрастов чаще всего откликается на рекламу

df = merged_df.groupby("grouped_age")["clicks"].sum().reset_index()
sns.barplot(x="grouped_age", y="clicks", data=df)
plt.xlabel('Age group')
plt.ylabel('Marketing influence')
plt.title('Marketing influence per age')
plt.show()
#Переименуем рекламные компании

merged_df = merged_df.rename(columns={
    "marketing_company_outcome_1": "ad_1",
    "marketing_company_outcome_2": "ad_2",
    "marketing_company_outcome_3": "ad_3",
    "marketing_company_outcome_4": "ad_4",
    "marketing_company_outcome_5": "ad_5",})
new_df = merged_df[["grouped_age", "ad_1", "ad_2", "ad_3", "ad_4", "ad_5"]]
df_grouped = new_df.groupby('grouped_age').sum().reset_index()
df_long_grouped = df_grouped.melt(id_vars=['grouped_age'], value_vars=['ad_1', 'ad_2', 'ad_3', 'ad_4', 'ad_5'], 
                                  var_name='ad_type', value_name='count')
plt.figure(figsize=(10, 6))
sns.barplot(data=df_long_grouped, x='grouped_age', y='count', hue='ad_type')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Advertisement Counts by Age Group')
plt.legend(title='Advertisement Type', loc='upper right')
plt.show()
