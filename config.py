# Model hub name
model_name = "google/gemma-2b-it"
# Model local path
model_path = model_name.split('/')[1] + '-model'
# Tokenizer local path
tokenizer_path = model_name.split('/')[1] + '-tokenizer'

# Prompte template 
prompt_template = """
                    # You are assistant that behaves very professionally. 
                    # You will only provide the answer if you know the answer. If you do not know the answer, you will say I dont know. 
                    
                    Instruction: {instruction}
                    Answer: 
                  """
# CPU or cuda ?
device = "cuda"

# Maximum number of tokens
max_token = 512