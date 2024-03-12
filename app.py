import streamlit as st
import pickle
from utils import set_background, predict

set_background('./nba_rookie1.jpg')

# Project Title
st.title('NBA Career Longevity Prediction')

st.header('Enter Player Statistics')

# Data
name = st.text_input('Enter Player Name')
col1, col2, col3 = st.columns(3)
GP = col1.slider('Enter Games Played', 0, 100)
MIN = col1.number_input('Enter Minutes Played')
TOV = col1.number_input('Enter Player turnovers')
REB = col2.number_input('Enter Player rebounds')
OREB = col2.number_input('Enter Player Offensive rebounds')
DREB = col2.number_input('Input Player Defensive rebounds')
AST = col1.number_input('Enter Player assists')
BLK = col1.number_input('Enter Player blocks')
STL = col1.number_input('Enter Player steals')
FTM = col3.number_input('Enter Number of Free Throws made')
FTA = col3.number_input('Enter Number of Free Throws attempts')
FT_PERCENT = col3.slider('Enter Free Throws success percentage', 0, 100)
ThreePTSMade = col2.number_input('Enter Number of 3 Points made')
ThreePA = col2.number_input('Enter Number of 3 Points attempts')
ThreeP_PERCENT = col2.slider('Enter 3 Pointer success percentage', 0, 100)
FGM = col3.number_input('Enter Number of Field Goals made')
FGA = col3.number_input('Enter Number of Field Goals attempts')
FG_PERCENT = col3.slider('Enter Field Goals success percentage', 0, 100)
PTS = col2.number_input('Enter Number of Points per game')

# Classifier
with open("./model/rf.pkl", 'rb') as model_file:
    model = pickle.load(model_file)

row = [GP, MIN, PTS, FGM, FGA, FG_PERCENT, ThreePTSMade, ThreePA, ThreeP_PERCENT,
       FTM, FTA, FT_PERCENT, OREB, DREB, REB, AST, STL, BLK, TOV]

prediction = predict(row, model)

toggle = st.button('Predict', on_click=prediction)
if toggle:
    if name is '' or name.isdigit() or name.replace('.', '', 1).isdigit():
        st.write('Enter a Player\'s name')
    else:
        if prediction == 1:
            st.success(f'{name} will flourish in the NBA')
        else:
            st.error(f'{name} will not flourish in the NBA')
