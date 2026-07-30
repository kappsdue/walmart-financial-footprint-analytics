import pandas as pd
import os
"""
this module helps in saving the dataframe to csv for reporting and further processing
"""

def save(df,tag_name):
    """
   Parameters
    ----------
    df : pandas.DataFrame
        cleaned metric dataframe.

    tag_name : str
        Name of the financial metric.
    """
    df.to_csv(f'data/processed/{tag_name}.csv',index=False)

def save_master(master):
    master.to_csv(f'data/processed/master.csv',index=False)