import chart_studio
import pandas as pd
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.express as px
import plotly.graph_objects as go

username = 'Nickwn'
apiKey = '5rffa2u8FSD2aWNV9Llq'
merged_us_regions_df = pd.read_csv('data/merged_us_regions.csv')
chart_studio.tools.set_credentials_file(username, apiKey)

fig = px.choropleth(merged_us_regions_df,
                    title='Effective Minimum Wage in 2020 Dollars Over the Years',
                    locations='State Code',
                    color='Effective.Minimum.Wage.2020.Dollars',
                    color_continuous_scale='spectral_r',
                    # hover_name='State',
                    locationmode='USA-states',
                    labels={
                        'Effective.Minimum.Wage.2020.Dollars': 'Minimum Wage in 2020 Dollars'},
                    scope='usa',
                    animation_frame='Year',
                    template="plotly_dark",
                    range_color=[0, 15]
                    )



py.plot(fig, filename='usMinimumWage')
