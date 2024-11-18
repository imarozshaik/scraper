# scraper (Assessment for AI Agent Project)


_**scraper**_ is an AI-driven web scraping agent designed to automate the extraction of important insights from various web resources based on the user's prompts. 

## Tech Stack
> **Dashboard/UI:** Streamlit

> **Data Handling:** pandas for CSV files

> **Search API:** SerpAPI

> **LLM API:** OpenAI’s GPT API

> **Backend:** Python

## Setup Guide
Install all the required libraries. They are listed in requirements.txt file.

### Method 1: Using a Virtual Environment (Recommended)

1. Create and activate a virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
### Method 2: Without a Virtual Environment

1. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```
## Setup Environment Variables

This project uses `.env` file to store sensitive API keys. Follow these steps to set up the environment variables:

(Make sure you have an account created already in SerpAPI and OpenAPI -- if you want to create one, follow these links [SerpAPI](https://serpapi.com/) and [OpenAPI](https://platform.openai.com/)

1. Create a `.env` file in the root directory:

    ```
    touch .env
    ```
2. Add these to your `.env` file:

    ```
    SERP_API_KEY = your_serp_api_key
    OPENAI_API_KEY = your_openai_api_key
    ```



## Usage Guide
1. Run the Streamlit app once all files are setup. Use the command
```
streamlit run app/main.py
```
2. Just follow through the prompts in the app UI.
3. First, upload the CSV file you need your data from.
4. Then, select a column of your choice from the dataset.
5. Finally, enter your custom prompt in the textbox provided (replace {entity} with a placeholder) and click on Start Search button. For example, 
```
Search for health risks associated with age {entity}
```
6. The results obtained are displayed as a table. You can also download the results as a CSV file.

## Third-Party Tools Used

1. SerpAPI (Search API)

   >Used to fetch search results from Google and other search engines. It handles all the web scraping and data gathering.

2. OpenAI (GPT API)

   >Used to parse the search results and extract meaningful insights based on the user's query.

3. Streamlit

   >Python library for creating interactive web applications.
   
