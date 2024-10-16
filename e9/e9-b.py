import pandas as pd


def pandas_csv_demo(file_path):
    # Step 1: Reading the CSV file using pandas
    df = pd.read_csv(file_path)
    print("Original DataFrame:")
    print(df)

    # Step 2: Display basic information about the dataset
    print("\nBasic information about the DataFrame:")
    print(df.info())

    # Step 3: Display summary statistics for numerical columns
    print("\nSummary statistics for numerical columns:")
    print(df.describe())

    # Step 4: Display the first 5 rows using head()
    print("\nFirst 5 rows of the DataFrame using head():")
    print(df.head())

    # Step 5: Display the last 5 rows using tail()
    print("\nLast 5 rows of the DataFrame using tail():")
    print(df.tail())

    # Step 6: Handling missing data by filling NaN values with a default value
    print("\nHandling missing values (if any) by filling NaN with default values:")
    df_filled = df.fillna(
        {
            "total_bedrooms": df[
                "total_bedrooms"
            ].mean(),  # Fill missing total_bedrooms with the mean
        }
    )
    print(df_filled)

    # Step 7: Dropping rows with missing values in critical columns
    print("\nDropping rows with missing 'longitude' or 'latitude':")
    df_dropped = df.dropna(subset=["longitude", "latitude"])
    print(df_dropped)

    # Step 8: Filtering the data based on a condition
    print(
        "\nFiltering rows where 'median_income' is greater than 5 and 'median_house_value' is above 200000:"
    )
    filtered_df = df[(df["median_income"] > 5) & (df["median_house_value"] > 200000)]
    print(filtered_df)

    # Step 9: Adding a new column (e.g., 'Rooms per Household')
    print(
        "\nAdding a new column 'Rooms per Household' (total_rooms divided by households):"
    )
    df["Rooms per Household"] = df["total_rooms"] / df["households"].replace(
        0, 1
    )  # Prevent division by zero
    print(df)

    # Step 10: Renaming a column
    print("\nRenaming the column 'median_house_value' to 'House Value':")
    df_renamed = df.rename(columns={"median_house_value": "House Value"})
    print(df_renamed)

    # Step 11: Saving the modified DataFrame back to a CSV file
    output_file_path = "modified_housing_data.csv"
    df.to_csv(output_file_path, index=False)
    print(f"\nModified DataFrame saved to {output_file_path}.")


# Example usage
file_path = "housing.csv"  # Replace this with your actual CSV file path
pandas_csv_demo(file_path)
