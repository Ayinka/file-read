import pandas as pd  # Ensure this line is present at the top of the script

def read_csv_file(file_path):
    
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully read {len(df)} rows from '{file_path}'.")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    return None


def process_data(df):
    
    if df is not None:
        try:
            df["Total Cost (with Tax)"] = df["Purchase Amount (USD)"] * 1.08
            print("Data successfully processed: Added 'Total Cost (with Tax)' column.")
            return df
        except KeyError:
            print("Error: 'Purchase Amount (USD)' column is missing from the dataset.")
        except Exception as e:
            print(f"An unexpected error occurred during processing: {e}")
    return None


def write_csv_file(df, output_file):
    """Writes a DataFrame to a CSV file."""
    if df is not None:
        try:
            df.to_csv(output_file, index=False)
            print(f"Data successfully written to '{output_file}'.")
        except PermissionError:
            print(f"Error: Permission denied to write to the file '{output_file}'.")
        except Exception as e:
            print(f"An unexpected error occurred while writing the file: {e}")


def main():
    # File paths
    input_file = "shopping_trends.csv"
    output_file = "modified_shopping_trends.csv"
    
    # Step 1: Read the data
    df = read_csv_file(input_file)
    
    # Step 2: Process the data
    processed_df = process_data(df)
    
    # Step 3: Write the modified data to a new CSV file
    write_csv_file(processed_df, output_file)


if __name__ == "__main__":
    main()
