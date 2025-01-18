import numpy as np
import pandas as pd
import matplotlib
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.backends.registry

data = pd.read_csv('covid_data.csv')
data = data[['Povince_State', 'Country_Region', 'Last Update', 'Lat', 'Long', 'Confirmed', 'Recovered', 'Death', 'Active']]
data.columns = ['State', 'Country', 'Last Update', 'Lat', 'Long', 'Confirmed', 'Recovered', 'Deaths', 'Active']

data["State"].fillna(value='', inplace=True)

top10_confirmed = data.groupby('Country')['Recovered'].sum().nlargest(10).reset_index()
fig3 = px.bar(top10_recovered, x='Country', y='Recovered', height = 400, color='Recovered', title='Top 10 Recovered Cases Countries', color_continuous_scale=px.colors.sequential.Virdis)
fig3.write_html('fig3.html', auto_open=True)

def analyze_country(country_name):
  country_data = data[data['Country'] == country_name]

  if country_data.empty:
    print("No data available for {country_name}.")
    return

top_states = country_data.nlargest(5, 'Confirmed')

fig = go.Figure()

fig.add_trace(go.Bar(name='Confirmed Cases', x=top_states['State'], y=top_states['Confirmed'], marker_color='blue'))
fig.add_trace(go.Bar(name='Death Cases', x=top_states['State'], y=top_states['Deaths'], marker_color='red'))
fig.add_trace(go.Bar(name='Death Cases', x=top_states['State'], y=top_states['Recovered'], marker_color='green'))

fig.update_layout(title=f'Most affected states in{country_name}', barmode='stack', height=600)
fig.write_html(f'Fig_{country_name}.html', auto_open=True)

analyze_country('US')
analyze_country('Brazil')
analyze_country('India')
analyze_country('Russia')