from threading import Thread
import asyncio
import os
import config

class Generator:
    
    def __init__(self,  model, tokenizer, streamer, streamer_queue):
        self.model = model
        self.tokenizer = tokenizer
        self.streamer = streamer
        self.streamer_queue = streamer_queue
    
    def start_generation(self, query):
    
        # Custom prompt template, can be replaced based on the use case
        prompt = config.prompt_template.format(instruction=query)
        # Converting the inputs to tokens for prediction
        inputs = self.tokenizer([prompt], return_tensors="pt").to(config.device)
        
        # key word arguments that are provided to the model.generate()function
        # Includes, inputs, max_tokens, streamer, temparature
        generation_kwargs = dict(inputs, streamer=self.streamer, max_new_tokens=config.max_token, temperature=0.1)
        
        # Starting the thread with the stream
        thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
        thread.start()
        
    async def response_generator(self, query):
        
        # Starting the generation process
        self.start_generation(query)
    
        # Infinite loop
        while True:
    
            # Retreiving the value from the queue
            value = self.streamer_queue.get()
    
            # Breaks if a stop signal is encountered
            if value == None:
                break
    
            # yields the value
            yield value
    
            # provides a task_done signal once value yielded
            self.streamer_queue.task_done()
    
            # guard to make sure we are not extracting anything from 
            # empty queue
            await asyncio.sleep(0.1)