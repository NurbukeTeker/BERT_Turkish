# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer

# model = AutoModelForTokenClassification.from_pretrained("savasy/bert-base-turkish-ner-cased")
# tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-ner-cased")
# ner=pipeline('ner', model=model, tokenizer=tokenizer)
# ner("Mustafa Kemal Atatürk 19 Mayıs 1919'da Samsun'a ayak bastı.")

from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer


model = AutoModelForTokenClassification.from_pretrained("akdeniz27/bert-base-turkish-cased-ner")
tokenizer = AutoTokenizer.from_pretrained("akdeniz27/bert-base-turkish-cased-ner")
ner = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="first")
ner("Merhaba ben Ataürk2ü çok seviyorum . Ankara'dayım")
