from fastapi import FastAPI

from schema.request_data import RequestDataBDP, RequestDataBDH
from utility.helper import async_xbbg

app = FastAPI()

@app.post("/read-bdp-data")
async def read_bdp_data(request_body: RequestDataBDP):
    try:
        body_data = request_body
        response = await async_xbbg(body_data.tickers_name,body_data.fields_name,'bdp', None, None)
        return response
    except Exception as e:
        print(e)

@app.post("/read-bdh-data")
async def read_bdh_data(request_body: RequestDataBDH):
    try:
        body_data = request_body
        print(body_data)
        response = await async_xbbg(body_data.tickers_name,body_data.fields_name,'bdh',body_data.start_date, body_data.end_date)
        return response
    except Exception as e:
        print(e)


