import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Hello, streamlit")


# display simple text
st.text("Lorem ipsum dolor sit amet")

# simple pd dataframe
df = pd.DataFrame({"fc": [1, 2, 3, 4, 5, 6], "sc": ["q", "w", "e", "r", "t", "y"]})
st.write("Here is the dataframe")
st.write(df)