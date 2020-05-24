import pandas as pd
import re
import numpy as np
import nltk

def process_sentences(sentence):
    #convert sentence to string else return ''
    try:
        sentence = str(sentence)
        #remove links (words containing 'http')
        sentence = ' '.join([x for x in sentence.split(' ') if 'http' not in x])
        #keep only letters and change to lower case
        sentence = re.sub('[^a-zA-Z ]+', '', sentence).lower()
        return sentence
    except: 
        return ''