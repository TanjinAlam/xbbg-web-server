import asyncio
import pandas as pd
from xbbg import blp

#wil have a switch case to iterate other xbbg function
async def async_xbbg(tickers,flds, function_type, start_date, end_date):
    
    if function_type == 'bdp':
        return await asyncio.to_thread(get_bdp_data, tickers,flds)
    elif function_type == 'bdh':
        return await asyncio.to_thread(get_bdh_data, tickers,flds, start_date, end_date)
    

#to access xbbg specific function based custom paramters
def get_bdp_data(tickers,flds):
    requested_data = blp.bdp(tickers=tickers, flds=flds)
    return requested_data

def get_bdh_data(tickers,flds,start_date,end_date):
    requested_data = blp.bdh(tickers=tickers, flds=flds, start_date=start_date, end_date=end_date)
    
    # Assuming requested_data is a Pandas DataFrame
    json_data = requested_data.to_json(orient="records")
    # Convert JSON data back to Pandas DataFrame
    df = pd.read_json(json_data, orient="records")
    
    return df.to_json(orient='records')
