import pandas as pd

df = pd.read_csv(r"C:\Users\DELL\Desktop\data sets\BMW\BMW sales.csv")

print('original data:')
print(df.head())

print("\nData Summary Before Cleaning:")
print(df.info())

df.duplicated()
df = df.drop_duplicates()
print(df)


print("\nCleaned Data:")
print(df.head())

df.to_csv('C:\\Users\DELL\Desktop\data sets\cleaned_data.csv', index=False)

print("\nCleaned data has been exported as 'CLEANED_DATA.csv'")

































