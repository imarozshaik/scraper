import requests
import os

# Get the API key from environment variables
SERP_API_KEY = os.getenv("SERP_API_KEY")

import requests

import time
import requests

def perform_search(query, serp_api_key, retries=3, delay=2):
    """
    Performs a search using SerpAPI and handles errors, retries, and rate-limiting.
    
    Parameters:
        query (str): The search query to send to SerpAPI.
        serp_api_key (str): Your SerpAPI key.
        retries (int): Number of times to retry in case of failure. Default is 3.
        delay (int): Delay in seconds between retries. Default is 2 seconds.
    
    Returns:
        dict: The JSON response from SerpAPI with the search results.
    """
    url = f"https://serpapi.com/search?q={query}&api_key={serp_api_key}"
    
    for attempt in range(retries):
        try:
            # Send the request to SerpAPI
            response = requests.get(url)
            
            # If the response is successful, return the JSON data
            if response.status_code == 200:
                return response.json()
            else:
                # Handle the non-200 status code (rate limiting, server errors)
                raise Exception(f"Error: {response.status_code} - {response.text}")
        
        except requests.exceptions.RequestException as e:
            # Catch network-related errors and retry
            print(f"Network error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    
    # If all retries fail, raise an exception
    raise Exception("Failed to fetch search results after multiple retries.")




def search_web(entity, num_results=3):
    """
    Perform a web search using SerpAPI for a given entity.
    
    Args:
        entity (str): The term to search for.
        num_results (int): Number of search results to retrieve.
    
    Returns:
        list: A list of dictionaries containing search result data.
    """
    if not SERP_API_KEY:
        raise ValueError("API key for SerpAPI is not set. Add it to your .env file.")
    
    url = "https://serpapi.com/search"
    params = {
        "q": entity,
        "api_key": SERP_API_KEY,
        "num": num_results,
        "engine": "google"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error with search API: {response.status_code}, {response.text}")
    
    return response.json().get("organic_results", [])

def batch_search(entities, num_results=3):
    """
    Perform web searches for a batch of entities.
    
    Args:
        entities (list): List of entities to search for.
        num_results (int): Number of search results to retrieve for each entity.
    
    Returns:
        dict: A dictionary with entities as keys and search results as values.
    """
    results = {}
    for entity in entities:
        try:
            results[entity] = search_web(entity, num_results)
        except Exception as e:
            results[entity] = f"Error: {e}"
    return results
