import streamlit as st
import pandas as pd
import numpy as np

# To run streamlit application execute streamlit run app.py
st.title("Hello Streamlit")

# display simple text
st.write("Simple text")

# work with data frame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write("Here is the dataframe")
st.write(df)

# create line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
