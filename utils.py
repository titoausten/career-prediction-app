import pandas as pd
import streamlit as st
import base64
import numpy as np

columns = ['GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG_PERCENT', 'ThreePTSMade', 'ThreePA', 'ThreeP_PERCENT',
           'FTM', 'FTA', 'FT_PERCENT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV']


def set_background(image_file):
    with open(image_file, "rb") as f:
        image_data = f.read()
    b64_encoded = base64.b64encode(image_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


# Predict
def predict(row: list, model):
    row = np.array(row)
    features = pd.DataFrame([row], columns=columns)
    model.predict(features)
