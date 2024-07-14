grouped_date_order = [
    '05.11 - 05.18', '05.18 - 05.25', '05.25 - 06.01', '06.01 - 06.08', '06.08 - 06.15', 
    '06.15 - 06.22', '06.22 - 06.29', '06.29 - 07.06', '07.06 - 07.13'
]

interactiondata['grouped_date'] = pd.Categorical(interactiondata['grouped_date'], categories=grouped_date_order, ordered=True)
interactiondata = interactiondata.sort_values('grouped_date')
sns.countplot(data=interactiondata, x="grouped_date", palette='viridis')
plt.xlabel('Last order date')
plt.ylabel('Count last orders')
plt.title('Last order per date')
plt.xticks(rotation=45)
plt.show()
