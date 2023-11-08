import asyncio
from xbbg import blp

async def async_xbbg(tickers,flds):
    data = await asyncio.to_thread(get_bdp_data, tickers,flds)
    return data

def get_bdp_data(tickers,flds):
    requested_data = blp.bdp(tickers=tickers, flds=flds)
    return requested_data
