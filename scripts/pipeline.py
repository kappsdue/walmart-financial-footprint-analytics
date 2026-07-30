from conf import SNAPSHOT_METRICS,FLOW_METRICS
from sec_api import get_data,load_json
from extract import get_metric
from cleaning import clean_flow, clean_snapshot
from save import save





def run_pipeline():
    """
    Executes the tasks step by step
    1. Load data  [we can configure it to download data also]
    2. extracting each financial metric
    3. cleaning the extracted data
    4. saving the cleaned data in csv file


    Returns
    -------
    None
    """

    print('loading SEC Data')

    data1= load_json()
    # i already had data, hence no need to use getdata and savejson function from sec_api

    print('data loaded successfully')

    for tag,unit in FLOW_METRICS.items():
        df= get_metric(data1,tag,unit)
        df= clean_flow(df,tag)
        save(df,tag)

        print(f'saved cleaned {tag} metric')

    for tag,unit in SNAPSHOT_METRICS.items():
        df= get_metric(data1,tag,unit)
        df= clean_snapshot(df,tag)
        save(df,tag)

        print(f'saved cleaned {tag} metric')


    print('Pipeline finished')

