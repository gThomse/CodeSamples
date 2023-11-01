import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import datetime
import findFile as ff
import threeMonths as tm

# import os
import re

month_no = 36
g_title = "Max T, Min T, and Rain since {}".format(format(tm.dayone_of_x_months(month_no)))

debugprint = "False"

excel_file = "Townsville Forecast.xlsm"
# excel_file = "7s.pdf"

# def dayone_of_x_months(mths):
#     today = datetime.date.today()
#     temp_date = today.replace(day=1)
#     days_offset = today - temp_date
#
#     for _ in range(mths):
#         # Next line - first day of the month - 1 day >> Last day of the previous month
#         previous_month = temp_date - datetime.timedelta(days=1)
#         # print(previous_month.strftime("%Y-%m-%d"))
#         # Next line sets the day of the date variable to the first.
#         temp_date = previous_month.replace(day=1)
#
#     temp_date = temp_date + days_offset
#     return temp_date

excel_path_n_file = ff.fle_find(excel_file, ff.find_doc_path(), 0)

# print(fle_path)

df = pd.read_excel(excel_path_n_file, sheet_name='Results')
# Setting Display format for Stats.
pd.options.display.float_format = "{:,.2f}".format

# print(df)
# Display dataset columns
if debugprint == False:
    for c in df.columns:
        print(c)

# Stripping ' mm' from Rain field for statistal analysis.
df['Rain'] = pd.to_numeric(df['Rain'].str.strip(" mm"))
# Next statement doesn't work before the line above. Fiddly ...

df['Rain'].fillna(0, inplace=True)

if debugprint == False:
    # Group by Example
    print(df.groupby('Forecast')[['Max °C', 'Min °C', 'Rain']].agg(['mean','count']))

    fld_set = df[['Forecast', 'Max °C', 'Min °C', 'Rain']]
    # Top only
    print(fld_set.head())

df['Date_of'] = pd.to_datetime(df['Forecast'].str.split(' ').str[0], dayfirst=True)

if debugprint == False:

    print("\n*  New Field 'Date_of'  head *")
    # Creating new field by splitting off the data from the day. Date_of is Date..

    print(df[['Date_of','Max °C', 'Min °C', 'Rain']].head() )

    print("\n  Date < 2022-01-01     -----")
    # filtered_df = df.query('date >= "2022-01-01" and date <= "2022-01-01"')

    print("It looks like the first few records have a stastical mean of NaN.")
    filtered_df = df.query('Date_of < "2022-01-01"')

if debugprint == False:
    print(filtered_df[['Date_of','Max °C', 'Min °C', 'Rain']].head())

# 3 Months from today's date.
recent_df = df.query('Date_of >= "{}"'.format(tm.dayone_of_x_months(month_no)))

if debugprint == False:
    print(recent_df['Rain'])
    print(recent_df.groupby('Date_of')[['Max °C', 'Min °C', 'Rain']].agg(['mean','count']).head())

mean_df = recent_df.groupby('Date_of')[['Max °C', 'Min °C', 'Rain']].mean()

if debugprint == False:
    print(mean_df.head())


try:
    # This didn't work
    mean_df.plot(x="Date_of", y=["Max °C", "Min °C", "Rain"], title=g_title)
except:
    # This did

    mean_df.plot(y=["Max °C", "Min °C", "Rain"], title=g_title)
    plt.xlabel('Date')

plt.show()


