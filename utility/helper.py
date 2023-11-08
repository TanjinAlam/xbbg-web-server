import asyncio
from xbbg import blp

#wil have a switch case to iterate other xbbg function
async def async_xbbg(tickers,flds):
    data = await asyncio.to_thread(get_bdp_data, tickers,flds)
    return data

#to access xbbg specific function based custom paramters
def get_bdp_data(tickers,flds):
    requested_data = blp.bdp(tickers=tickers, flds=flds)
    return requested_data
