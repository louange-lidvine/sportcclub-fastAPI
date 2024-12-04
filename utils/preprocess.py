# import pandas as pd
#
# def preprocess_data(input_path, output_path):
#     """Preprocess the dataset by handling missing values and duplicates."""
#     df = pd.read_csv(input_path)
#     # Replace null values
#     df.fillna("Unknown", inplace=True)
#     # Remove duplicates
#     df.drop_duplicates(inplace=True)
#     # Save processed data
#     df.to_csv(output_path, index=False)
#     return output_path
# print()

# import pandas as pd
#
#
# def preprocess_data(input_path, output_path):
#     """Preprocess the dataset by handling missing values and duplicates."""
#     # Load the dataset
#     df = pd.read_csv(input_path)
#
#     # Before processing, print the shape and basic info of the dataset
#     print("Before Preprocessing:")
#     print(f"Number of rows: {df.shape[0]}")
#     print(f"Number of columns: {df.shape[1]}")
#     print("Columns in the dataset:", df.columns.tolist())
#     print("Missing values before preprocessing:")
#     print(df.isnull().sum())
#
#     # Replace null values
#     df.fillna("Unknown", inplace=True)
#
#     # Remove duplicates
#     df.drop_duplicates(inplace=True)
#
#     # After preprocessing, print the new state of the dataset
#     print("\nAfter Preprocessing:")
#     print(f"Number of rows after removing duplicates: {df.shape[0]}")
#     print(f"Number of columns: {df.shape[1]}")
#     print("Missing values after preprocessing:")
#     print(df.isnull().sum())
#
#     # Print basic statistics of the dataset
#     print("\nDataset Summary:")
#     print(df.describe(include='all'))
#
#     # Display first few rows to check the result
#     print("\nFirst few rows of the processed data:")
#     print(df.head())
#
#     # Save processed data
#     df.to_csv(output_path, index=False)
#
#     # Return output path for reference
#     return output_path
#
#
# # Example usage of the function
# input_file = 'data/raw_data.csv'  # Adjust as needed
# output_file = 'data/processed_data.csv'  # Adjust as needed
#
# processed_file = preprocess_data(input_file, output_file)
# print(f"Processed data saved to: {processed_file}")

import pandas as pd
import os


def preprocess_data(input_path, output_path):
    """Preprocess the dataset by handling missing values and duplicates."""
    print("Starting the preprocessing...")

    # Check if the file exists
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found!")
        return

    # Load the dataset
    df = pd.read_csv(input_path)
    print("Data loaded successfully.")

    # Before processing
    print("Before Preprocessing:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("Columns:", df.columns.tolist())
    print("Missing values before preprocessing:", df.isnull().sum())

    # Replace null values
    df.fillna("Unknown", inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # After processing
    print("\nAfter Preprocessing:")
    print(f"Number of rows after removing duplicates: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("Missing values after preprocessing:", df.isnull().sum())

    # Print summary of dataset
    print("\nDataset Summary:")
    print(df.describe(include='all'))

    # Save the processed data
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to: {output_path}")
    return output_path

