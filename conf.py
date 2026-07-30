"""this file contains header and base url
base_url contains the website url
headers contain info that is required to connect with website without headers website refuses to connect
"""
headers= {"User-Agent": "Kaustubh <Add own email>.com"}
base_url= "https://data.sec.gov/api/xbrl/companyfacts/CIK0000104169.json"

json_path= "data/raw/companyfacts.json"

'''
FLOW_METRICS = [
    "Revenues",
    "NetIncomeLoss",
    "NetCashProvidedByUsedInOperatingActivities",
    "PaymentsToAcquirePropertyPlantAndEquipment"
]

SNAPSHOT_METRICS = [
    "Assets",
    "StockholdersEquity"
]

SNAPSHOT_METRICS2= ["EarningsPerShareDiluted"]
'''


# final build 23 jul 26
FLOW_METRICS = {
    "Revenues": "USD",
    "NetIncomeLoss": "USD",
    "NetCashProvidedByUsedInOperatingActivities": "USD",
    "PaymentsToAcquirePropertyPlantAndEquipment": "USD",
    "EarningsPerShareDiluted": "USD/shares"
}

SNAPSHOT_METRICS = {
    "Assets": "USD",
    "StockholdersEquity": "USD"
}