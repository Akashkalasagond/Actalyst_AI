import streamlit as st
import openai
import json
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

# API key setup
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load embeddings
with open('embeddings_with_metadata.json', 'r') as f:
    embeddings = json.load(f)

# Function to generate embeddings for the query
def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response['data'][0]['embedding']

# Function to get the most relevant information based on query
def get_relevant_info(query, top_n=2):
    query_embedding = get_embedding(query)
    similarities = [cosine_similarity([query_embedding], [np.array(e['embedding'])]) for e in embeddings]
    sorted_indices = np.argsort(similarities, axis=0)[-top_n:][::-1]
    return [embeddings[i] for i in sorted_indices.flatten()]

# Function to generate a response using GPT-4 chat model
def generate_response(query, relevant_infos):
    responses = []
    for relevant_info in relevant_infos:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following information:\nTitle: {relevant_info['title']}\nSummary: {relevant_info['summary']}\nDate: {relevant_info['date']}\n\nAnswer the following query: {query}"}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=150
        )
        responses.append(response.choices[0].message['content'])
    return responses

# Function to extract the number of articles requested from the query
def extract_number_from_query(query):
    match = re.search(r'(\d+)', query)
    if match:
        return int(match.group(1))
    return 1

# Streamlit UI
st.title("News Chatbot")
query = st.text_input("Enter your query:")
if st.button("Search"):
    if query:
        top_n = extract_number_from_query(query)
        relevant_infos = get_relevant_info(query, top_n)
        responses = generate_response(query, relevant_infos)
        for i, (relevant_info, response) in enumerate(zip(relevant_infos, responses)):
            st.write(f"### Article {i + 1}")
            st.write("Title:", relevant_info['title'])
            st.write("Summary:", relevant_info['summary'])
            st.write("Publication Date:", relevant_info['date'])
            st.write("Response:", response)
    else:
        st.write("Please enter a query.")
