# Aluminium Industry Data Processing and Streamlit App

## Overview

This project involves extracting relevant data from the aluminium industry, converting the data to vector embeddings, and deploying a Streamlit application to visualize the embeddings.

## Steps

### Step 1: Extract Data

- **Objective:** Extract relevant data from the aluminium industry.
- **Data Fields:**
  - **Title:** The title of the data entry.
  - **Summary:** A brief summary of the data entry.
  - **Date:** The date of the data entry.

### Step 2: Convert Data to Vector Embeddings

- **Objective:** Convert the extracted scrap data to vector embeddings.
- **Method:** Utilized `text-embedding-ada-002` model to generate vector embeddings from the text data.

### Step 3: Streamlit Application

- **Objective:** Create a Streamlit application that loads and displays the vector embeddings.
- **Functionality:**
  - Load vector embeddings.
  - Provide a user interface to interact with the data.
  - Visualize the embeddings effectively.

### Step 4: Deployment

- **Objective:** Deploy the Streamlit application for public access.
- **Deployment Details:** The application is publicly accessible at [https://actalystai.streamlit.app/](https://actalystai.streamlit.app/).

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- OpenAI API for `text-embedding-ada-002`

### Installation

1. **Clone the Repository:**
   ```bash
   git clone [(https://github.com/Akashkalasagond/Actalyst_AI)]
2. **Navigate to the Project Directory:**
   ```bash
   cd [Actalyst_AI]
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Deployment**
   ```bash
   streamlit run app.py

