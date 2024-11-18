from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from search import perform_search
from gpt_parser import parse_with_gpt
from utils import save_results_to_csv

# Load environment variables from .env
load_dotenv()

# Retrieve API keys
SERP_API_KEY = os.getenv("SERP_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.title("AI Web Scraping Agent!")


uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
    
if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Dataset:")
        st.dataframe(data)
        
        # Column selection for search
        column_to_search = st.selectbox("Select a column for web search", data.columns)

        # Custom prompt input
        custom_prompt = st.text_area(
            "Enter your custom prompt (use {entity} as a placeholder):",
            value="Search for {entity}"
        )

        # Ensure custom prompt contains {entity}
        if "{entity}" not in custom_prompt:
            st.error("Your custom prompt must contain '{entity}' as a placeholder.")
        else:
            if st.button("Start Search"):
                search_results = []
                for entity in data[column_to_search]:
                    search_query = custom_prompt.replace("{entity}", str(entity))
                    search_data = perform_search(search_query, SERP_API_KEY)
                    gpt_output = parse_with_gpt(str(search_data), OPENAI_API_KEY)
                    search_results.append({"Entity": entity, "GPT Output": gpt_output})

                # Display and save results
                results_df = pd.DataFrame(search_results)
                st.write("Search Results:")
                st.dataframe(results_df)

                save_results_to_csv(results_df, "results/search_results.csv")
                st.success("Results saved to search_results.csv!")
