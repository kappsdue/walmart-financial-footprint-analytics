
from extract import get_metric
import sec_api
import conf
from cleaning import clean_flow, clean_snapshot

#old code left 
'''get_info=sec_api.get_data()
sec_api.save_json(get_info)'''
'''
read=sec_api.load_json()
d=get_metric(read,"Revenues","USD")
cleaned =clean_flow(d,'Revenues')
print(cleaned)

'''


# final build 23 jul 26
from pipeline import run_pipeline
from merger import merge
from save import save_master

run_pipeline()

master = merge()

save_master(master)
