import pandas as pd
from tabulate import tabulate
import plotly.express as px
import plotly.io as pio

us_regions_df = pd.read_csv(r'data/us_regions.csv')
mw_df = pd.read_csv(r'data/mw.csv', encoding='latin')

merged_us_regions_df = us_regions_df.merge(mw_df, how="left", on="State")

merged_us_regions_df.to_csv('data/merged_us_regions.csv')
# print(print(tabulate(merged_us_regions_df.head(10), headers='keys', tablefmt='psql')))

fig = px.choropleth(merged_us_regions_df,
                    title='Effective Minimum Wage in 2020 Dollars Over the Years',
                    locations='State Code',
                    color='Effective.Minimum.Wage.2020.Dollars',
                    color_continuous_scale='spectral_r',
                    hover_name='State',
                    locationmode='USA-states',
                    labels={'Minimum Wage': 'Effective.Minimum.Wage.2020.Dollars'},
                    scope='usa',
                    animation_frame='Year',
                    template="plotly_dark",
                    range_color=[0, 15]
                    )


pio.write_html(fig, file='index.html', auto_open=True)
# fig.show()