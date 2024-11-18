import pandas as pd

def save_results_to_csv(data, output_file):
    """Save data to a CSV file."""
    data.to_csv(output_file, index=False)

def load_csv_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)
