import time

# from xbbg import blp
from fastapi import FastAPI

from schema.request_data import RequestBody
from utility.helper import async_xbbg


app = FastAPI()



@app.post("/read-bdp data")
async def read_bdp_data(request_body: RequestBody):
    try:
        body_data = request_body
        response = await async_xbbg(body_data.tickers_name,body_data.fields_name)
        return response
    except Exception as e:
        print(e)

