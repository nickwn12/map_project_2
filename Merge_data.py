import pandas as pd
from tabulate import tabulate
import plotly.express as px
import plotly.io as pio
import pickle

us_regions_df = pd.read_csv(r'data/us_regions.csv')
mw_df = pd.read_csv(r'data/mw.csv', encoding='latin')

merged_us_regions_df = us_regions_df.merge(mw_df, how="left", on="State")

merged_us_regions_df.to_csv('data/merged_us_regions.csv')

