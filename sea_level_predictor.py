import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv', index_col='Year')

  # Create scatter plot
  fig, ax = plt.subplots()

  ax.scatter(df.index, df['CSIRO Adjusted Sea Level'], s=2)
  ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

  # Create first line of best fit
  start_year = df.index[0]
  x1 = range(start_year, 2050)
  slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df.index, df['CSIRO Adjusted Sea Level'])
  ax.plot(x1, intercept1 + slope1 * x1, 'g', label='Best fit ' + str(start_year) + '-2050')

  # Create second line of best fit
  df_2000 = df.loc[2000:]

  x2 = range(2000, 2050)
  slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_2000.index, df_2000['CSIRO Adjusted Sea Level'])
  ax.plot(x2, intercept2 + slope2 * x2, 'r', label='Best fit 2000-2050')


  # Add labels and title
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.set_title('Rise in Sea Level')
  ax.legend()
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()