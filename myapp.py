import streamlit as st  # khai báo thư viện
import pandas as pd
import numpy as np
import pandas as pd
# hàm nhập tên biến ở việt nam
ten = st.text_input("Nhập tên ngành nghề bạn muốn đi thực tập ở việt nam")

df = pd.DataFrame()
data = { 
        'name'
        'lat': [-73.96727182919946],
        'lon': [40.750214150000005]}
df = pd.DataFrame(data)
df
st.map(df)
