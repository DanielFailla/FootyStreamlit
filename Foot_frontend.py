## https://www.wheeloratings.com/afl_stats.html to download csv

import streamlit as st
import pandas as pd
#import plotly.express as px
import numpy as np


def Team1_2_desposals_range(Team1_Risk,lower_lim,upper_lim):
    Dsp = Team1_Risk[(Team1_Risk['Disposals'] >= lower_lim) & (Team1_Risk['Disposals'] < upper_lim)].sort_values('Disposals')
    tabel = Dsp[['Player', 'Disposals']]
    st.write(tabel)

def Team1_2_goals_range(Team1_Risk,lower_lim,upper_lim):
    Dsp = Team1_Risk[(Team1_Risk['Goals_Avg'] >= lower_lim) & (Team1_Risk['Goals_Avg'] < upper_lim)].sort_values('Goals_Avg')
    tabel = Dsp[['Player', 'Goals_Avg']]
    st.write(tabel)

st.header("🏉FOOTY BETTING🏉")

st.divider()
st.subheader('CSV DROPBOX 📦')
st.write("Click to find updated CSV files [link](https://www.wheeloratings.com/afl_stats.html)")
uploaded_file = st.file_uploader("Choose a file")
file_name = uploaded_file.name
# Read CSV file
data = pd.read_csv(file_name)

sorted_data = data.sort_values(by='Team', ascending=True)
# Display the contents of the DataFrame
#t.write(sorted_data)

## Input string e.g "Collingwood"
def sort_team(x):
    y = sorted_data[sorted_data['Team'] == x]
    return y


st.divider()
st.subheader('🤜HEAD TO HEAD🤛')
all_teams_list = ['Adelaide','Brisbane', 'Carlton', 'Collingwood','Essendon', 'Fremantle','Geelong', 
                  'Gold Coast', 'Greater Western Sydney' , 'Hawthorn', 'Melbourne' , 'North Melbourne', 
                  'Port Adelaide', 'Richmond', 'St Kilda', 'Sydney','West Coast', 'Western Bulldogs' ]

AFL_selection = st.multiselect(
    'CHOOSE TWO TEAMS',
    all_teams_list )

col1, col2 = st.columns(2)

with col1:
   st.subheader(AFL_selection[0])
   team1 = sort_team(AFL_selection[0])
   st.write(team1[['Player', 'Goals_Avg', 'Disposals']])



with col2:
   st.subheader(AFL_selection[1])
   team2 = sort_team(AFL_selection[1])
   st.write(team2[['Player', 'Goals_Avg', 'Disposals']])

st.divider()
##RISK SLIDER
st.subheader('Choose Risk Level ↕️')
Risk = st.select_slider(
    'Select your risk level',
    options=['Low', 'Normal', 'High', 'Mad'])

with st.expander("Explination on Risk Scores"):
    st.text("Goal Avg: Low= -1, Normal = -0.5, High = 0, Mad = +0.5")
    st.text("Disposal Avg: Low= -4, Normal = -2, High = 0, Mad = +2")
    st.write("⚠️Disclaimer⚠️")
    st.text("This is designed to improve your odds and not guarantee wins!")

tab1, tab2 = st.tabs([AFL_selection[0], AFL_selection[1]])
##RISK SLIDER


x = (len(team1))
z = (len(team2))
## GOALS: LOW = -1, NORMAL = -0.5, HIGH = 0, MAD = +0.5
## DISP: LOW = -4, NORMAL = -2, HIGH = 0, MAD = +2
GRF_team1= pd.DataFrame({'Low': np.full(x,-1),'Normal':np.full(x,-0.5),'High':np.full(x,0),"Mad":np.full(x,0.5)})
DRF_team1= pd.DataFrame({'Low': np.full(x,-4),'Normal':np.full(x,-2),'High':np.full(x,0),"Mad":np.full(x,2)})
GRF_team2= pd.DataFrame({'Low': np.full(z,-1),'Normal':np.full(z,-0.5),'High':np.full(z,0),"Mad":np.full(z,0.5)})
DRF_team2= pd.DataFrame({'Low': np.full(z,-4),'Normal':np.full(z,-2),'High':np.full(z,0),"Mad":np.full(z,2)})

Team1_Risk = pd.DataFrame({'Player':np.array(team1['Player']),
                           'Goals_Avg':np.array(team1['Goals_Avg'])+np.array(GRF_team1[Risk]),
                            'Disposals':np.array(team1['Disposals'])+np.array(DRF_team1[Risk])})

Team2_Risk = pd.DataFrame({'Player':np.array(team2['Player']),
                           'Goals_Avg':np.array(team2['Goals_Avg'])+np.array(GRF_team2[Risk]),
                            'Disposals':np.array(team2['Disposals'])+np.array(DRF_team2[Risk])})

word_1 = "Risk Selection: "
word_2 = Risk
combines_word = f'{word_1}{word_2}'

with tab1:
  
   st.subheader("Goal Averages")
   #st.bar_chart(data=Team1_Risk, x='Player', y='Goals_Avg', use_container_width=True)
   st.subheader("Disposals Average")
   #st.bar_chart(data=Team1_Risk, x='Player', y='Disposals', use_container_width=True)
   st.divider()
   st.subheader('     📚 Bet Slip Recomendations 📚')
   st.subheader(combines_word)
   col3, col4 = st.columns(2)

   with col3:
      st.subheader("15 to < 20 disposals")
      Team1_2_desposals_range(Team1_Risk,15,20)
      st.subheader("20 to < 25 disposals")
      Team1_2_desposals_range(Team1_Risk,20,25)
      st.subheader("25 or more disposals")
      Team1_2_desposals_range(Team1_Risk,25,40)

   with col4:
      st.subheader("1 or more goals")
      Team1_2_goals_range(Team1_Risk,1,10)
      st.subheader("2 or more goals")
      Team1_2_goals_range(Team1_Risk,2,10)
      
      

      
      
   

with tab2:
   
   st.subheader("Goal Averages")
   #st.bar_chart(data=Team2_Risk, x='Player', y='Goals_Avg', use_container_width=True)
   st.subheader("Disposals Average")
   #st.bar_chart(data=Team2_Risk, x='Player', y='Disposals', use_container_width=True)
   st.subheader('     📚 Bet Slip Recomendations 📚')
   st.subheader(combines_word)

   col5, col6 = st.columns(2)

   with col5:
      st.subheader("15 to < 20 disposals")
      Team1_2_desposals_range(Team2_Risk,15,20)
      st.subheader("20 to < 25 disposals")
      Team1_2_desposals_range(Team2_Risk,20,25)
      st.subheader("25 or more disposals")
      Team1_2_desposals_range(Team2_Risk,25,40)

   with col6:
      st.subheader("1 or more goals")
      Team1_2_goals_range(Team2_Risk,1,10)
      st.subheader("2 or more goals")
      Team1_2_goals_range(Team2_Risk,2,10)




