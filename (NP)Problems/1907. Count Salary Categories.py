import pandas as pd

def category(income):
    if income < 20000:
        return "Low Salary"
    elif 20000 <= income <= 50000:
        return "Average Salary"
    elif income > 50000:
        return "High Salary"

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    #accounts['category']=accounts['income'].apply(lambda x: category(x))
    accounts['category'] = accounts['income'].apply(category)
    final = accounts.groupby('category')['account_id'].count().reset_index()
    final.columns = ['category', 'accounts_count']
     # Ensure all categories are present in the output, even if their count is 0
    
    # # Ensure all categories are present in the output, even if their count is 0
    # all_categories = pd.DataFrame({
    #     'category': ['Low Salary', 'Average Salary', 'High Salary']
    # })
    # final = all_categories.merge(final, on='category', how='left').fillna(0)
    # final['accounts_count'] = final['accounts_count'].astype(int)

    # VS 

    all_categories = ['Low Salary', 'Average Salary', 'High Salary']
    #This reindexes the DataFrame to include all the categories specified in all_categories, which is ['Low Salary', 'Average Salary', 'High Salary']. If any category is missing, it will be added with a count of 0 (fill_value=0).
    final = final.set_index('category').reindex(all_categories, fill_value=0).reset_index()
    return final
