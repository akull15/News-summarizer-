#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load dataset
data = pd.read_json("News_Category_Dataset_v2.json", lines=True)

# Keep relevant columns
data = data[['headline', 'short_description', 'category']]

# Combine headline and description for summarization
data['text'] = data['headline'] + ". " + data['short_description']

# Preview dataset
print(data.head())


# In[3]:


from transformers import pipeline

# Load summarizer model (can take a minute)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Example: Summarize first article
article = data['text'][0]
summary = summarizer(article, max_length=60, min_length=15, do_sample=False)
print("Original:", article)
print("Summary:", summary[0]['summary_text'])


# In[4]:


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load sentence embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Compute embeddings for all articles (can take a few minutes)
corpus = data['text'].tolist()
corpus_embeddings = embedder.encode(corpus, show_progress_bar=True)

# Function to recommend similar articles
def get_similar_articles(input_text, top_n=3):
    input_embedding = embedder.encode([input_text])
    similarities = cosine_similarity(input_embedding, corpus_embeddings)[0]
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    return data.iloc[top_indices][['headline', 'short_description', 'category']]

# Example: Recommend articles similar to the first one
recommendations = get_similar_articles(article)
print(recommendations)


# In[ ]:


import gradio as gr
from transformers import pipeline

# Load the summarization pipeline using BART
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to generate the summary
def summarize(text):
    if not text.strip():
        return "Please enter some news article text to summarize."
    
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Create the Gradio interface
iface = gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(lines=15, placeholder="Paste your news article here...", label="News Article"),
    outputs=gr.Textbox(label="Summary"),
    title="📰 News Summarizer",
    description="Enter a news article, and this app will generate a concise summary using a Transformer-based model (BART).",
)

# Launch the app
iface.launch()

