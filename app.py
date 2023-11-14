from fastapi import FastAPI
import pandas as pd
from schema.request_data import RequestDataBDP, RequestDataBDH, RequestDataBDIB, RequestDataBDS, RequestDataDividend, RequestDataEarning
from utility.blp_helper import bdh_async, bdib_async, bdp_async, bds_async, earning_async, get_dividend_data
from fastapi.responses import JSONResponse
import aioredis

from utility.helper import get_array_from_redis_key, hash_object, set_array_as_redis_key
app = FastAPI()
redis = aioredis.from_url("redis://localhost", decode_responses=True)


@app.post("/read-bdp-data")
async def read_bdp_data(request_body: RequestDataBDP):
    try:
        body_data = request_body
        
        cache_hash_key = hash_object(body_data)
        bdh_cache_data = await get_array_from_redis_key(redis, "bdp")
        
        if not bdh_cache_data or cache_hash_key not in bdh_cache_data:
            bdh_cache_data.append(cache_hash_key)
            response = await bdh_async(body_data.tickers_name,body_data.fields_name,body_data.start_date, body_data.end_date, request_body.adjust)
            await set_array_as_redis_key(redis, "bdp", bdh_cache_data)
            await redis.set(cache_hash_key, response)
            return JSONResponse(content=response, media_type="application/json")
                    
        if cache_hash_key in bdh_cache_data:
            return JSONResponse(content=await redis.get(cache_hash_key), media_type="application/json")
    except Exception as e:
        print(e)

@app.post("/read-bdh-data")
async def read_bdh_data(request_body: RequestDataBDH):
    try:
        body_data = request_body
        
        cache_hash_key = hash_object(body_data)
        bdh_cache_data = await get_array_from_redis_key(redis, "bdh")
        
        if not bdh_cache_data or cache_hash_key not in bdh_cache_data:
            bdh_cache_data.append(cache_hash_key)
            response = await bdh_async(body_data.tickers_name,body_data.fields_name,body_data.start_date, body_data.end_date, request_body.adjust)
            await set_array_as_redis_key(redis, "bdh", bdh_cache_data)
            await redis.set(cache_hash_key, response)
            return JSONResponse(content=response, media_type="application/json")
                    
        if cache_hash_key in bdh_cache_data:
            return JSONResponse(content=await redis.get(cache_hash_key), media_type="application/json")

    except Exception as e:
        print(e)

        
@app.post("/read-bds-data")
async def read_bds_data(request_body: RequestDataBDS):
    try:
        body_data = request_body
        
        cache_hash_key = hash_object(body_data)
        bdh_cache_data = await get_array_from_redis_key(redis, "bds")
        
        if not bdh_cache_data or cache_hash_key not in bdh_cache_data:
            bdh_cache_data.append(cache_hash_key)
            response = await bdh_async(body_data.tickers_name,body_data.fields_name,body_data.start_date, body_data.end_date, request_body.adjust)
            await set_array_as_redis_key(redis, "bds", bdh_cache_data)
            await redis.set(cache_hash_key, response)
            return JSONResponse(content=response, media_type="application/json")
                    
        if cache_hash_key in bdh_cache_data:
            return JSONResponse(content=await redis.get(cache_hash_key), media_type="application/json")

    except Exception as e:
        print(e)
        
@app.post("/read-bdib-data")
async def read_bdib_data(request_body: RequestDataBDIB):
    try:

        body_data = request_body
        
        cache_hash_key = hash_object(body_data)
        bdh_cache_data = await get_array_from_redis_key(redis, "bdib")
        
        if not bdh_cache_data or cache_hash_key not in bdh_cache_data:
            bdh_cache_data.append(cache_hash_key)
            response = await bdh_async(body_data.tickers_name,body_data.fields_name,body_data.start_date, body_data.end_date, request_body.adjust)
            await set_array_as_redis_key(redis, "bdib", bdh_cache_data)
            await redis.set(cache_hash_key, response)
            return JSONResponse(content=response, media_type="application/json")
                    
        if cache_hash_key in bdh_cache_data:
            return JSONResponse(content=await redis.get(cache_hash_key), media_type="application/json")
        
    except Exception as e:
        print(e)
        
@app.post("/read-earning-data")
async def read_earning_data(request_body: RequestDataEarning):
    try:
    
        body_data = request_body
        
        cache_hash_key = hash_object(body_data)
        bdh_cache_data = await get_array_from_redis_key(redis, "earning")
        
        if not bdh_cache_data or cache_hash_key not in bdh_cache_data:
            bdh_cache_data.append(cache_hash_key)
            response = await bdh_async(body_data.tickers_name,body_data.fields_name,body_data.start_date, body_data.end_date, request_body.adjust)
            await set_array_as_redis_key(redis, "earning", bdh_cache_data)
            await redis.set(cache_hash_key, response)
            return JSONResponse(content=response, media_type="application/json")
                    
        if cache_hash_key in bdh_cache_data:
            return JSONResponse(content=await redis.get(cache_hash_key), media_type="application/json")
        
    except Exception as e:
        print(e)
        
        
@app.post("/read-dividend-data")
async def read_earning_data(request_body: RequestDataDividend):
    try:
        
        body_data = request_body
        
        cache_hash_key = hash_object(body_data)
        bdh_cache_data = await get_array_from_redis_key(redis, "dividend")
        
        if not bdh_cache_data or cache_hash_key not in bdh_cache_data:
            bdh_cache_data.append(cache_hash_key)
            response = await bdh_async(body_data.tickers_name,body_data.fields_name,body_data.start_date, body_data.end_date, request_body.adjust)
            await set_array_as_redis_key(redis, "dividend", bdh_cache_data)
            await redis.set(cache_hash_key, response)
            return JSONResponse(content=response, media_type="application/json")
                    
        if cache_hash_key in bdh_cache_data:
            return JSONResponse(content=await redis.get(cache_hash_key), media_type="application/json")
    except Exception as e:
        print(e)




