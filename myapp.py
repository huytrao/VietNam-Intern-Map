import streamlit as st
import leafmap.kepler as leafmap
import pandas as pd

#hiển thị độ rộng của bản đồ 
st.set_page_config(layout="wide")
df = pd.read_csv("./data/job_ex.csv")
st.dataframe(df)
st.title("leafmap streamlit demo")
job = st.text_input("Job Intern you want to find:")  # Use st.text_input to get user input

"## Create a 3D map using Kepler.gl"
# # ghim map ở thành phố hồ chí minh
m = leafmap.Map(center=[10.785160732570825, 106.69416733524045], zoom=1)
# m = leafmap.Map(center=[37.7621, -122.4143], zoom=12)
in_csv = "./data/job_ex.csv"
config = "./configmaps/hex_config.json"
m.add_csv(in_csv, layer_name="job_data", config=config)
m.to_streamlit()
