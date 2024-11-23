import streamlit as st
import pandas as pd 
import numpy as np

database={
"noms":["abdou","sophie","bara","fatou","ami","omar"],
"Prenoms":["diop","fall","sow","ngom","sylla","gueye"]
}

database=pd.DataFrame(database)

st.write(database)


