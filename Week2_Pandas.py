import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(pd.__version__)
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])
a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print(myvar["y"])
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df.loc[0])
print(df.loc[[0, 1]])
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(pd.options.display.max_rows)
df = pd.read_json('data.json')

print(df.to_string())
df = pd.read_json('data.json')

print(df.to_string())
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)
df = pd.read_csv('data.csv')

print(df.head(10))
df = pd.read_csv('data.csv')

print(df.head())
print(df.tail())
print(df.info())
df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())
df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())
df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)
df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)
df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)
df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)
df = pd.read_csv('dirtydata.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())
df.dropna(subset=['Date'], inplace = True)
df.loc[7, 'Duration'] = 45
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
    for x in df.index:
      if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)
print(df.duplicated())
df.drop_duplicates(inplace = True)
df = pd.read_csv('data.csv')

print(df.corr())
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()
import matplotlib

print(matplotlib.__version__)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()
df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()
df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()
df["Duration"].plot(kind = 'hist')