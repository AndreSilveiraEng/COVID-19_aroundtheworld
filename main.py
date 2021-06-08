import pandas as pd
import numpy as np
import os

pwd = os.getcwd()

covid_data = pd.read_csv(pwd + '\\datasets\\owid-covid-data_kaggler.csv')
covid_survey = pd.read_csv(pwd + '\\datasets\\covid_google_forms.csv')

cd = covid_data.copy()
cs = covid_survey.copy()

cd = cd.rename(columns={'location': 'country'})

cd.to_csv('COVID_19_overview.csv')
cs.to_csv('COVID-19_survey.csv')