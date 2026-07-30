"""
Functions responsible for cleaning financial metrics
retrieved from the SEC Company Facts API.
"""

import pandas as pd

def clean_flow(df,tag_name):
    """
    Clean annual flow metrics such as Revenue and Net Income.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw metric dataframe.

    tag_name : str
        Name of the financial metric.
    """


    #convert start and end column to datetype
    df['start'] = pd.to_datetime(df['start'])
    df['end'] = pd.to_datetime(df['end'])

    #calculate the duration
    df['duration']= df['end']-df['start']

    #keep annual rows only
    annual_rows= df[df['duration']>  pd.Timedelta(days=360)]

    #sort by filled date
    sort= annual_rows.sort_values(by="filed")

    #removing duplicates
    removal = sort.drop_duplicates(subset=['start','end'], keep='first')

    #sort by chronological
    clean= removal.sort_values('start')

    #rename col
    better_df= clean[['start', 'end', 'val', 'filed']].rename(columns={'val': tag_name})
    return better_df



def clean_snapshot(df,tag_name):
    """
Clean annual flow metrics who does not contain start date

Parameters
    ----------
    df : pandas.DataFrame
        Raw metric dataframe.

    tag_name : str
        Name of the financial metric.
"""

#convert start and end column to datetype
    df['end']=pd.to_datetime(df['end'])

#sorting the df by jan1st day 31 and form 10-k
    snap_sorting= df[ (df['end'].dt.month ==1) &
                        (df['end'].dt.day ==31) &
                        (df['form'] == '10-K')]

#sorting by filled date
    sort_filed= snap_sorting.sort_values(by="filed")

#dropping duplicates
    removal_2= sort_filed.drop_duplicates(subset=['end'], keep='first')

    better_df2 = removal_2[['end','val','filed','form']].rename(columns={'val': tag_name})
    return better_df2

# final build 23 jul 26