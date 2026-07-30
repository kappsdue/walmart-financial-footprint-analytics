"""
this module helps in extracting the data from the JSON file.
user has to pass two arguments


Functions in this module only extract the data and convert it into pandas dataframe.
"""

import pandas as pd
def get_metric(data,tag_name,unit):
    """
data: path of data file or variable containing data
tag_name: str
        us-gaap tag to extract.
        Example:
            "Revenues"
            "NetIncomeLoss"
            "Assets"

unit: str in Capital only
        example: "USD", "USD/shares"
    """
    try:
        metric= data['facts']["us-gaap"][tag_name]["units"][unit]
        return pd.DataFrame(metric)

    except KeyError:
        raise KeyError(f"{tag_name} not found in sec company facts")


# final build 23 jul 26