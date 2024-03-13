from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import config

def read_model():
    if os.path.isdir(config.model_path) and os.path.isdir(config.tokenizer_path):
        tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_path, device_map=config.device)
        model = AutoModelForCausalLM.from_pretrained(config.model_path, device_map=config.device)
    else:
        tokenizer = AutoTokenizer.from_pretrained(config.model_name, device_map=config.device)
        model = AutoModelForCausalLM.from_pretrained(config.model_name, device_map=config.device)
        tokenizer.save_pretrained(config.tokenizer_path)
        model.save_pretrained(config.model_path)
    return tokenizer, model