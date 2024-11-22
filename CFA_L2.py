import streamlit as st
import pandas as pd
from datetime import datetime, date
remaining = datetime(2025, 5, 25, 0, 0) - datetime.today()

st.title("CFA Level 2 - May'25")

# Inject custom CSS
st.markdown(
    """
    <style>
    .custom-font {
        font-size: 24px; /* Adjust font size */
        color: #4CAF50; /* Optional: Set font color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use the custom class
st.markdown('<p class="custom-font">Bring it home. <b>You got this.</b></p>', unsafe_allow_html=True)

st.subheader(f'Days Left for Exam: {remaining.days}', anchor=None, help=None, divider = 'red')

remaining = datetime(2025, 3, 31, 0, 0) - datetime.today()
st.subheader(f'Days Left To Complete Prep: {remaining.days}', anchor=None, help=None, divider = 'red')

df = pd.read_csv('Deadlines.csv')
df['End Date'] = pd.to_datetime(df['End Date'])
df['Today'] = datetime.today()
df['Remaining Days'] = (df['End Date'] - df['Today']).dt.days
df['Remaining Days'] = df['Remaining Days'].apply(lambda x: 'Deadline Passed' if x < 0 else x)
df = df[['Topic', 'Start Date', 'End Date', 'Days Allotted', 'Remaining Days']]

df['Start Date'] = pd.to_datetime(df['Start Date']).dt.strftime('%d-%b-%Y')
df['End Date'] = df['End Date'].dt.strftime('%d-%b-%Y')
st.dataframe(df, width = 1000, hide_index = True, use_container_width=True)
