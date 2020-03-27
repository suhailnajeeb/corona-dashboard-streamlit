import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

data_path = 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/'

confirmed_csv = data_path + 'time_series_covid19_confirmed_global.csv'
recovered_csv = data_path + 'time_series_19-covid-Recovered.csv'
death_csv = data_path + 'time_series_covid19_deaths_global.csv'


df = pd.read_csv(confirmed_csv)


def plot_country(df, country):
    country_df = df[df['Country/Region'] == country]
    dates = country_df.columns[4:]
    dates = [datetime.strptime(d, "%m/%d/%y").date() for d in dates]
    patients = country_df.sum(axis=0, skipna=True)[4:]
    patients = [p for p in patients]
    #patients = country_df.values[0][4:]
    plt.figure(figsize=(20, 5))
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.bar(dates, patients)
    plt.title('No of confirmed cases for : ' + country)
    plt.show()


def plot_world(df, case):
    dates = df.columns[4:]
    dates = [datetime.strptime(d, "%m/%d/%y").date() for d in dates]
    patients = df.sum(axis=0, skipna=True)[2:]
    patients = [p for p in patients]
    plt.figure(figsize=(20, 5))
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.bar(dates, patients)
    plt.title('No of ' + case + ' cases acroos the globe')
    plt.show()

def plot_state(df, state, case):
    state_df = df[df['Province/State'] == state]
    dates = state_df.columns[4:]
    dates = [datetime.strptime(d, "%m/%d/%y").date() for d in dates]
    patients = state_df.sum(axis=0, skipna=True)[4:]
    patients = [p for p in patients]
    #patients = country_df.values[0][4:]
    plt.figure(figsize=(20, 5))
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.bar(dates, patients)
    plt.title('No of ' + case + ' cases for : ' + state)
    plt.show()

countries = np.unique(df['Country/Region'].values)
country = countries[0]

statewala = []
for country in countries:
    country_df = df[df['Country/Region'] == country]
    if not(country_df.shape[0] == 1):
        statewala.append(country)

country_df = df[df['Country/Region'] == 'US']

plot_state(country_df, state = 'Hebei', case = 'confirmed')
#plot_country(df, 'Bangladesh')
#plot_world(df, "confirmed")