import pandas as pd ## pandas is a Python Data Analysis Library (it helped me get the dataframe from the html and parse it to json), i installed it with pip install pandas.

calls_df, = pd.read_html("https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS", header=0)

cols = (['Junk'] + calls_df.columns.tolist())
del cols[-1]

calls_df.columns = cols
del calls_df['Junk']

print(calls_df.to_json(orient="records", date_format="iso"))

