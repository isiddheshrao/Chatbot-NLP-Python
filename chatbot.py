# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:55:27 2019

@author: Siddhesh Rao
"""

# Building a chatbot with DeepNLP
#importing Libraries

import numpy as np
import tensorflow as tf
import re
import time
# Data_Preprocessing
lines = open("movie_lines.txt", encoding="utf-8", errors = "ignore").read().split("\n")
conversations = open("movie_conversations.txt", encoding="utf-8", errors = "ignore").read().split("\n")
#creating dictionary. mapping line to id
id2line={}
for line in lines:
    _line = line.split(" +++$+++ ")
    if len(_line)==5:
        id2line[_line[0]] = _line[4]
#creating list of all conversations
conversations_ids = []
for conversation in conversations[:-1]:
    _conversation = conversation.split(" +++$+++ ")[-1][1:-1].replace("'","").replace(" ","")
    conversations_ids.append(_conversation.split(","))
#getting questions and answers seperately
questions = []
answers = []
for conversation in conversations_ids:
    for i in range(len(conversation)-1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])
#doing cleaning of texts- first
def clean_text(text):
    text = text.lower()
    text = re.sub(r"i,m", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"\'ll", "will", text)
    text = re.sub(r"\'ve", "have", text)
    text = re.sub(r"\'re", "are", text)
    text = re.sub(r"\'d", "would", text)
    text = re.sub(r"wont", "will not", text)
    text = re.sub(r"[-()\"#/@:;<>{}+=~|.?,]", "", text)
    return text
#cleaning questions
clean_questions = []
for question in questions:
    clean_questions.append(clean_text(question))
#cleaning answers
clean_answers = []
for answer in answers:
    clean_answers.append(clean_text(answer))
#dictionary to map each word based on its occurances
word2count = {}
for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1