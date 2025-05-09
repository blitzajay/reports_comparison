import pandas as pd
import os

def load_file(filepath):
    _, ext = os.path.splitext(filepath)
    if ext.lower() == ".csv":
        return pd.read_csv(filepath)
    elif ext.lower() == ".xlsx":
        return pd.read_excel(filepath, engine='openpyxl')
    elif ext.lower() == ".xls":
        return pd.read_excel(filepath, engine='xlrd')
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def compare_files(file1, file2, output_csv='mismatches_output.csv'):
    df1 = load_file(file1)
    df2 = load_file(file2)

    print("\n✅ Files loaded successfully.")

    # Check column match
    if list(df1.columns) != list(df2.columns):
        print("❌ Column mismatch detected:")
        print("File 1 columns:", list(df1.columns))
        print("File 2 columns:", list(df2.columns))
        return

    print("✅ Column names match.")

    # Check row count match
    if len(df1) != len(df2):
        print(f"❌ Row count mismatch: File 1 = {len(df1)} rows, File 2 = {len(df2)} rows")
        return

    print("✅ Row count matches.")

    # Compare content row by row
    mismatches = []
    for idx in range(len(df1)):
        for col in df1.columns:
            val1 = df1.at[idx, col]
            val2 = df2.at[idx, col]

            if pd.isnull(val1) and pd.isnull(val2):
                continue  # both empty, considered equal

            if val1 != val2:
                mismatches.append({
                    "RowNumber": idx + 1,
                    "Column": col,
                    "File1_Value": val1,
                    "File2_Value": val2
                })

    if mismatches:
        mismatch_df = pd.DataFrame(mismatches)
        mismatch_df.to_csv(output_csv, index=False)
        print(f"❌ {len(mismatches)} mismatches found. Saved to '{output_csv}'")

        print("\n🔍 Sample mismatches (up to 5 shown):")
        print(mismatch_df.head())
    else:
        print("✅ Data content matches across all rows.")

if __name__ == "__main__":
    file1 = "Consumption_report_9000.csv"  # replace with your actual file
    file2 = "Consumption_report_2500.csv"   # replace with your actual file
    compare_files(file1, file2)
