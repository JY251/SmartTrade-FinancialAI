from transformers import BertTokenizer, BertForSequenceClassification, pipeline

import transformers
transformers.__version__

finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone', num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

nlp = pipeline('text-classification', model=finbert, tokenizer=tokenizer)

results = nlp("I am happy")

