# Import Library
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")

# Title
image = Image.open('NBA_Logo.jpg')
st.image(image, use_column_width=True)
st.markdown("<h1 style='text-align:center'>🏀 NBA Basketball Player Stats Explorer 🏀</h1>",
            unsafe_allow_html=True)

# Source of Data : https://www.basketball-reference.com/leagues/NBA_2021_per_game.html

col1, col2 = st.beta_columns(2)


# Meaning of Features
data = {
    'Data': ['Pos', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'],
    'Description': ['Position of Player in the Team', 'Team', 'Games', 'Game Started', 'Minutes Played Per Game', 'Field Goals Per Game', 'Field Goal Attempts Per Game', 'Field Goal Percentage', '3 Point Field Goals Per Game', '3 Point Field Goal Attempts Per Game', '3 Point Field Percentage', '2 Point Field Goals Per Game', '2 Point Firld Goal Attempts Per Game', '2 Point Field Percentage', 'Effective Field Goal Percentage', 'Free Throw Per Game', 'Free Throw Attempts Per Game', 'Free Throw Percentage', 'Offensive Rebounds Per Game', 'Defensive Rebounds Per Game', 'Total Rebounds Per Game', 'Assists Per Game', 'Steals Per Game', 'Blocks Per Game', 'Turnovers Per Game', 'Personal Fouls Per Game', 'Points Per Game']
}

description = pd.DataFrame(data)

# Sidebar
st.sidebar.header('Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(2010, 2021))))


@ st.cache  # Web Scraping of NBA Player Stats
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + \
        str(year) + "_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    # Deletes Repeated Headers in Content
    raw = df.drop(df[df['Age'] == 'Age'].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)  # Rank Column
    return playerstats


playerstats = load_data(selected_year)

# Sidebar - Team Selection
sorted_unique_team = sorted(playerstats['Tm'].unique())
selected_team = st.sidebar.multiselect(
    'Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position Selection
unique_position = ['C', 'PF', 'SF', 'PG', 'SG']
selected_position = st.sidebar.multiselect(
    'Position', unique_position, unique_position)

# Filtering Data
df_selected_team = playerstats[(playerstats['Tm'].isin(
    selected_team)) & (playerstats['Pos'].isin(selected_position))]

col1.subheader('Display Player Stats of Selected Team(s)')
col1.write('Data Dimension : ' + str(df_selected_team.shape[0]) + ' Rows and ' + str(
    df_selected_team.shape[1]) + ' Columns.')
col1.dataframe(df_selected_team)


col2.subheader('Data Description(s)')
col2.write('Description of Each Feature')
col2.write(description)


def download(df):  # Download Player Stats Data
    csv = df.to_csv(index=False)
    # Strings - Bytes Conversion
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="NBA Basketball Player Stats.csv">Download</a>'
    return href


col2.markdown(download(df_selected_team), unsafe_allow_html=True)

# Heatmap
if col1.button('Intercorrelation Heatmap'):
    col1.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('NBA'+str(selected_year)+'.csv', index=False)
    df = pd.read_csv('NBA'+str(selected_year)+'.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    col1.pyplot(f)
