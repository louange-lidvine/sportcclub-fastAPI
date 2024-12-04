# import pandas as pd
#
# def perform_analysis(input_path, output_path):
#     """Perform analysis and create features."""
#     df = pd.read_csv(input_path)
#     # Feature Engineering
#     df['user_event_difference'] = pd.to_datetime(df['created_at_event']) - pd.to_datetime(df['created_at_user'])
#     df['user_event_difference'] = df['user_event_difference'].dt.total_seconds() / 3600  # Convert to hours
#     df['is_active'] = df['event_id'].apply(lambda x: 1 if pd.notnull(x) else 0)
#     # Save results
#     df.to_csv(output_path, index=False)
#     return output_path
#
import pandas as pd


def perform_analysis(input_path, output_path):
    """Perform analysis and create features."""
    # Read the input CSV data
    df = pd.read_csv(input_path)

    # Feature Engineering
    df['user_event_difference'] = pd.to_datetime(df['created_at_event']) - pd.to_datetime(df['created_at_user'])
    df['user_event_difference'] = df['user_event_difference'].dt.total_seconds() / 3600  # Convert to hours

    # Create a new column to mark activity based on event_id
    df['is_active'] = df['event_id'].apply(lambda x: 1 if pd.notnull(x) else 0)

    # Display some useful information about the dataset
    print("Data Head (first 5 rows):")
    print(df.head())  # Display first few rows

    print("\nData Info:")
    print(df.info())  # Display column types, non-null counts, etc.

    print("\nSummary Statistics:")
    print(df.describe())  # Display statistical summary

    # Save results to the output path
    df.to_csv(output_path, index=False)

    # Return the output file path
    return output_path
