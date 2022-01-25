from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import torch


# Load the values
data=pd.read_csv("./py_code/data/categories.csv", index_col='id' )
dict = data.T.to_dict('list')

# load the model
tokenizer = AutoTokenizer.from_pretrained('./hf_training/botcamp-bert-base-uncased')
model =  AutoModelForSequenceClassification.from_pretrained('./hf_training/botcamp-bert-base-uncased')



def get_clf(text):
    # prepare our text into tokenized sequence
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    # perform inference to our model
    outputs = model(**inputs)
    probs = outputs[0].softmax(1)
    i = (probs.argmax()).item()
    pr = probs[0][i]
    i = (probs.argmax())
    res = dict[i.item()], pr.item()
        
    return res

text = "where are my courses "
t, p = get_clf(text)

print(t[0])