import streamlit as st
import pandas as pd
import numpy as np
from utils import plot_country

#-------------------------------------------------------------------------
st.title("Plotting COVID-19 Data")


#-------------------------------------------------------------------------
data_path = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/'

confirmed_csv = data_path + 'time_series_covid19_confirmed_global.csv'
recovered_csv = data_path + 'time_series_19-covid-Recovered.csv'
death_csv = data_path + 'time_series_covid19_deaths_global.csv'

#------------------------------------------------------------------------------
case = st.selectbox("Which case would you like to view? ", ("confirmed","recovered","death"))

if(case == "confirmed"):
    csv_path = confirmed_csv    
if(case == "recovered"):
    csv_path = recovered_csv
if(case == "death"):
    csv_path = death_csv

st.text("Loading the Dataset..")
df = pd.read_csv(csv_path)

st.dataframe(df)

countries = np.unique(df['Country/Region'].values)

# Selectbox
country = st.selectbox("Please select the country you want to view: ", countries)
plot_country(df, country, case)
st.pyplot()