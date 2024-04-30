import numpy as np
import pandas as pd

urban_file = "data/Marylebone_AirQualityDataHourly_2018-2021_clean.csv"
rural_file = "Rochester_AirQualityDataHourly_2018-2021_clean.csv"

urban_df = pd.read_csv(urban_file)