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
    "marketing_company_outcome_5": "ad_5",
