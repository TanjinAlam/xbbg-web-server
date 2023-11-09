from fastapi import FastAPI

from schema.request_data import RequestDataBDP, RequestDataBDH, RequestDataBDIB, RequestDataBDS, RequestDataDividend, RequestDataEarning
from utility.helper import async_xbbg, bdh_async, bdib_async, bdp_async, bds_async, earning_async, get_dividend_data

app = FastAPI()

@app.post("/read-bdp-data")
async def read_bdp_data(request_body: RequestDataBDP):
    try:
        body_data = request_body
        response = await bdp_async(body_data.tickers_name,body_data.fields_name)
        return response
    except Exception as e:
        print(e)

@app.post("/read-bdh-data")
async def read_bdh_data(request_body: RequestDataBDH):
    try:
        body_data = request_body
        response = await bdh_async(body_data.tickers_name,body_data.fields_name,body_data.start_date, body_data.end_date, request_body.adjust)
        return response
    except Exception as e:
        print(e)
        
        
@app.post("/read-bds-data")
async def read_bds_data(request_body: RequestDataBDS):
    try:
        body_data = request_body
        response = await bds_async(body_data.tickers_name,body_data.fields_name,body_data.start_date, body_data.end_date)
        return response
    except Exception as e:
        print(e)
        
@app.post("/read-bdib-data")
async def read_bdib_data(request_body: RequestDataBDIB):
    try:
        body_data = request_body
        response = await bdib_async(body_data.ticker_name,body_data.session,body_data.query_type,body_data.date)
        return response
    except Exception as e:
        print(e)
        
@app.post("/read-earning-data")
async def read_earning_data(request_body: RequestDataEarning):
    try:
        body_data = request_body
        response = await earning_async(body_data.ticker_name,body_data.by, body_data.query_type, body_data.currency, body_data.level, body_data.date, body_data.period)
        return response
    except Exception as e:
        print(e)
        
        
@app.post("/read-dividend-data")
async def read_earning_data(request_body: RequestDataDividend):
    try:
        body_data = request_body
        response = await get_dividend_data(body_data.tickers_name,body_data.start_date, body_data.end_date, body_data.query_type)
        return response
    except Exception as e:
        print(e)




