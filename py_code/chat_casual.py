from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

#model_name = "microsoft/DialoGPT-large"
model_name = "microsoft/DialoGPT-medium"
#model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def casual_chat(text, chat_history_ids =None):

    
    # encode the input and add end of string token
    input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
    
    # concatenate new user input with chat history (if there is one)
    if chat_history_ids != None:
        bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1)
    else:
        bot_input_ids = input_ids
    
    # generate a bot response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        do_sample=True,
        top_p=0.95,
        top_k=0,
        temperature=0.75,
        pad_token_id=tokenizer.eos_token_id
    )
    
    #print the output
    output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    #print('Step:', step)
    #if step > 5:
    #    print('Are sure you want information, or just want a chat?')
    return output, chat_history_ids