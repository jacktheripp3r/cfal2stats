import streamlit as st
import pandas as pd
from datetime import datetime, date
remaining = datetime(2025, 3, 31, 0, 0) - datetime.today()

st.title("Analytics")

df = pd.read_csv('https://docs.google.com/spreadsheets/d/11EUKLaoZQYvCi4ghibrDgTU14oaV6HBd7YYC0Pf9imc/gviz/tq?tqx=out:csv&sheet=Sheet1')
today_date = datetime.today().strftime('%Y-%m-%d')
db_index = df[df['Date'] == today_date].index[0]
df = df[:db_index]
del db_index


total = df['Minutes'].sum()
average = df['Minutes'].mean().round(2)
average_notzero = df[df['Minutes']!=0]['Minutes'].mean().round(2)

df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.strftime('%A')
hours_studied = round(total/60, 2)
hours_remaining = round(250 - hours_studied, 2)

st.write(f"Target: 250 Hours. Total Hours Studied: {round(total/60, 0)}.\n Hours Remaining: {hours_remaining}.")
st.write(f"You have to hit {round(hours_remaining/remaining.days, 2)} hours or {round((hours_remaining/remaining.days) * 60)} minutes everyday.")
st.write(f"Total Time Studied: {round(total/60, 2)} Hours or {total} minutes.")
st.write(f"Average Minutes Studied: {average}")
st.write(f"Average Minutes Studied On Days Actually Studied: {average_notzero}")

aggregate = df.groupby('Day')['Minutes'].agg(['sum', 'mean', 'median', 'std']).round().reset_index()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
aggregate['Day'] = pd.Categorical(aggregate['Day'], categories=day_order, ordered=True)
aggregate = aggregate.sort_values('Day')

st.write('Daily Data Analysis:')
st.dataframe(aggregate, hide_index = True)
st.bar_chart(aggregate, x = 'Day', y = ['sum', 'mean', 'median'])

df = df.sort_values('Date')
df['Cumulative Sum'] = df['Minutes'].cumsum()

st.line_chart(df, x = 'Date', y = 'Cumulative Sum', y_label = 'Minutes of Study', width = 500)