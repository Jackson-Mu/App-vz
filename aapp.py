# Streamlit is an open-source app framework for Machine Learning and Data Science projects.
import streamlit as st

# Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and data manipulation Python library.
import pandas as pd

# NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions.
import numpy as np

# Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
import matplotlib.pyplot as plt

# Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
import seaborn as sns

# Plotly Express is a terse, consistent, high-level API for creating figures with Plotly.py.
import plotly.express as px

# (Note: Streamlit is imported twice in the provided code, which is redundant.)
import streamlit as st

# Python's built-in library for generating random numbers.
import random

# PIL (Python Imaging Library) is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.
from PIL import Image


# Load the NYU logo image >>>>>>>>>>>>
image_nyu = Image.open('nyu.png')
# Display the NYU logo on the Streamlit app
st.image(image_nyu, width=100)

# Set the title for the Streamlit app >>>>>>>>>>>>
st.title("Linear Regression Example")

# Create a sidebar header and a separator
st.sidebar.header("Dashboard")
st.sidebar.markdown("---")

df = pd.read_csv("wine_quality_red.csv")
#df = pd.read_csv("df_spotify_final.csv")


## Description of Dataset

num = st.number_input('No of Rows',5,10)
st.dataframe(df.head(num))

### Description of the dataset

st.dataframe(df.describe())

if st.button("Show Describe Code"):
        code = '''df.describe()'''
        st.code(code, language='python')

if st.button("Generate Report"):
  import streamlit as st
  import streamlit.components.v1 as components

  # Title for your app
  st.title('Sweetviz Report in Streamlit')

  # Display the Sweetviz report
  report_path = 'report.html'
  HtmlFile = open(report_path, 'r', encoding='utf-8')
  source_code = HtmlFile.read()
  components.html(source_code, height=1000,width=1000)


list_variables = df.columns

# Display a header for the Visualization section
st.markdown("## Visualization")
symbols = st.multiselect("Select two variables", list_variables, ["quality", "citric acid"])


quality_min, quality_max = st.sidebar.slider('Select Quality Range', min_value=int(df['quality'].min()), max_value=int(df['quality'].max()), value=(int(df['quality'].min()), int(df['quality'].max())))
citric_acid_min, citric_acid_max = st.sidebar.slider('Select Citric Acid Range', min_value=float(df['citric acid'].min()), max_value=float(df['citric acid'].max()), value=(float(df['citric acid'].min()), float(df['citric acid'].max())))

# Filtering the dataframe based on the slider values
filtered_df = df[(df['quality'] >= quality_min) & (df['quality'] <= quality_max) & (df['citric acid'] >= citric_acid_min) & (df['citric acid'] <= citric_acid_max)]


tab1, tab2 = st.tabs(["Line Chart", "Bar Chart"])

tab1.subheader("Line Chart")
# Display a line chart for the selected variables
tab1.line_chart(data=filtered_df, x=symbols[0], y=symbols[1], width=0, height=0, use_container_width=True)

tab2.subheader("Bar Chart")
# Display a bar chart for the selected variables
tab2.bar_chart(data=filtered_df, x=symbols[0], y=symbols[1], use_container_width=True)

