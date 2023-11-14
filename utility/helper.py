
import json
import pickle
import hashlib

def hash_object(obj):
    # Serialize the object to a byte stream using pickle
    obj_bytes = pickle.dumps(obj)

    # Calculate the hash of the byte stream
    obj_hash = hashlib.sha256(obj_bytes).hexdigest()

    return obj_hash



async def set_array_as_redis_key(redis, key, array):
    # Serialize the array to JSON before storing it in Redis
    serialized_array = json.dumps(array)
    await redis.set(key, serialized_array)
    await redis.expire(key, 7200)

async def get_array_from_redis_key(redis, key):
    # Retrieve the serialized array from Redis
    serialized_array = await redis.get(key)

    # Deserialize the array from JSON
    if serialized_array:
        array = json.loads(serialized_array)
        return array
    else:
        return []