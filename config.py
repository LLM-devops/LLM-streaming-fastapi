# Model hub name
model_name = "venkycs/phi-2-instruct"
# Model local path
model_path = model_name.split('/')[1] + '-model'
# Tokenizer local path
tokenizer_path = model_name.split('/')[1] + '-tokenizer'

# Prompte template 
prompt_template = """
                    # You are assistant that behaves very professionally. 
                    # You will only provide the answer if you know the answer. If you do not know the answer, you will say I dont know. 
                    
                    # ###Human: {instruction},
                    # ###Assistant: 
                  """
# CPU or cuda ?
device = "cuda"

# Token access


# Maximum number of tokens
max_token = 1000