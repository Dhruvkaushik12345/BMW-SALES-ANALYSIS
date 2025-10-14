import pandas as pd

df = pd.read_csv(r"C:\Users\DELL\Desktop\datasets\BMW sales.csv")

print('original data:')
print(df.head())

print("\n🔹 Data Summary Before Cleaning:")
print(df.info())

df = df.drop_duplicates()
print(df)


print("\nCleaned Data:")
print(df.head())

df.to_csv("CLEANED_DATA.CSV")

print("\nCleaned data has been exported as 'CLEANED_DATA.csv'")

































