import asyncio
import pandas as pd
from xbbg import blp

async def bdp_async(tickers_name,flds):
    return await asyncio.to_thread(get_bdp_data, tickers_name,flds)
    
async def bdh_async(tickers_name,flds, start_date, end_date, adjust):
    return await asyncio.to_thread(get_bdh_data, tickers_name,flds, start_date, end_date, adjust)
    
async def bds_async(tickers_name,flds, start_date, end_date):
    return await asyncio.to_thread(get_bds_data, tickers_name,flds, start_date, end_date)
    
async def bdib_async(ticker_name,session, query, date):
    return await asyncio.to_thread(get_bdib_data, ticker_name,session, query, date)
    
async def earning_async(ticker_name,by, query, currency,level, date, period):
    return await asyncio.to_thread(get_earning_data, ticker_name, by, query, currency,level, date, period)

async def dividend_async(tickers_name, start_date, end_date, query):
    return await asyncio.to_thread(get_dividend_data, tickers_name, start_date, end_date,query)
    


#to access xbbg specific function based custom paramters
def get_bdp_data(tickers,flds):
    requested_data = blp.bdp(tickers=tickers, flds=flds)
    return requested_data

def get_bdh_data(tickers,flds,start_date,end_date, adjust):
    if adjust == "-" or None:
        requested_data = blp.bdh(tickers=tickers, flds=flds, start_date=start_date, end_date=end_date)
    else:
         requested_data = blp.bdh(tickers=tickers, flds=flds, start_date=start_date, end_date=end_date,adjust=adjust)
         
    return requested_data.to_json()


def get_bds_data(tickers,flds,start_date,end_date):
    requested_data = blp.bds(tickers=tickers, flds=flds, DVD_Start_Dt=start_date, DVD_End_Dt=end_date)
    
    return requested_data.to_json()



def get_bdib_data(ticker_name,session,query,date):
    if session == None and query == None: 
        requested_data = blp.bdib(ticker=ticker_name, dt=date)
    elif session and query: 
        requested_data = blp.bdib(ticker=ticker_name, dt=date, session=session, typ=query)
    elif session: 
        requested_data = blp.bdib(ticker=ticker_name, dt=date, session=session)
    elif query: 
        requested_data = blp.bdib(ticker=ticker_name, dt=date, session=session)
    
    return requested_data.to_json()



def get_earning_data(ticker_name,by,query,currency,level, date , period):
    if currency == None and level == None and date == None and period == None: 
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query)
    elif currency and level and date and period: 
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Eqy_Fund_Year=date, level= level, ccy= currency, Number_Of_Periods= period)
    elif currency and level and date and period:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Eqy_Fund_Year=date, level=level, ccy=currency, Number_Of_Periods=period)
    elif currency and level and date:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Eqy_Fund_Year=date, level=level, ccy=currency)
    elif currency and level and period:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, level=level, ccy=currency, Number_Of_Periods=period)
    elif currency and date and period:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Eqy_Fund_Year=date, ccy=currency, Number_Of_Periods=period)
    elif level and date and period:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Eqy_Fund_Year=date, level=level, Number_Of_Periods=period)
    elif currency and level:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, level=level, ccy=currency)
    elif currency and date:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Eqy_Fund_Year=date, ccy=currency)
    elif currency and period:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, ccy=currency, Number_Of_Periods=period)
    elif level and date:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Eqy_Fund_Year=date, level=level)
    elif level and period:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, level=level, Number_Of_Periods=period)
    elif date and period:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Eqy_Fund_Year=date, Number_Of_Periods=period)
    elif currency:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, ccy=currency)
    elif level:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, level=level)
    elif date:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Eqy_Fund_Year=date)
    elif period:
        requested_data = blp.bdib(ticker=ticker_name, by=by, typ=query, Number_Of_Periods=period)
    
    return requested_data.to_json()


def get_dividend_data(tickers,flds,start_date,end_date, query):
    if query == "all" or None:
        requested_data = blp.dividend(tickers=tickers, start_date=start_date, end_date=end_date)
    else:
         requested_data = blp.dividend(tickers=tickers, start_date=start_date, end_date=end_date,typ=query)
    
    return requested_data.to_json()
