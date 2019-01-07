import pandas as pd

calls_df, = pd.read_html("https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS", header=0)

cols = (['Junk'] + calls_df.columns.tolist())
del cols[-1]

calls_df.columns = cols
del calls_df['Junk']

print(calls_df.to_json(orient="records", date_format="iso"))

