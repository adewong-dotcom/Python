import pandas as pd

""" with open('Pandas_Testing\weather_data.csv') as file:
    content = file.read()

print(content) """

""" df = pd.read_csv('Pandas_Testing\weather_data.csv')
list_of_rows = [list(row) for row in df.values]

temp = df['temp']
average = temp.mean()
print(f"Average: {average}")
max = temp.max()
print(f"Max value: {max}")

def celsius_to_farenheit(celsius):
    farenheit = celsius * (9/5)
    farenheit += 32
    return farenheit

print(df[df.temp == max])
max_farenheit = celsius_to_farenheit(max)
print(f"Farenheit Max: {max_farenheit}")

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv") """

squirrel_df = pd.read_csv('Pandas_Testing/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#print(squirrel_df.columns)

coats = squirrel_df["Primary Fur Color"].dropna()

print(coats.unique())

coats = coats.value_counts().reset_index()
coats.columns = ["Color", "Count"]

print(coats.value_counts())
coats.to_csv("Pandas_Testing/squirrel_count.csv")

