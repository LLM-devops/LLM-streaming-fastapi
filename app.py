from fastapi import FastAPI
from queue import Queue
from fastapi.responses import StreamingResponse
import os
from generator import Generator
from streamer import CustomStreamer
from utils import read_model
import config


# Fast API
app = FastAPI()

# Reading model
tokenizer, model = read_model() 

# Streamer 
streamer_queue = Queue()
streamer = CustomStreamer(streamer_queue, tokenizer, True)

# Generator
generator = Generator(model = model,
                      tokenizer = tokenizer,
                      streamer = streamer,
                      streamer_queue = streamer_queue)
@app.get("/")
async def root():
    return {"message": "Embedding model is online."}

@app.get('/query-stream/')
async def stream(query: str):
    return StreamingResponse(generator.response_generator(query), media_type='text/event-stream')


