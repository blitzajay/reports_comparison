import streamlit as st
import pandas as pd
import os

def load_file(uploaded_file):
    _, ext = os.path.splitext(uploaded_file.name)
    if ext.lower() == ".csv":
        return pd.read_csv(uploaded_file)
    elif ext.lower() == ".xlsx":
        return pd.read_excel(uploaded_file, engine='openpyxl')
    elif ext.lower() == ".xls":
        return pd.read_excel(uploaded_file, engine='xlrd')
    else:
        st.error("Unsupported file format.")
        return None

st.title("🔍 Report Comparison Tool")

file1 = st.file_uploader("Upload First Report", type=["csv", "xls", "xlsx"])
file2 = st.file_uploader("Upload Second Report", type=["csv", "xls", "xlsx"])

if file1 and file2:
    df1 = load_file(file1)
    df2 = load_file(file2)

    if df1 is not None and df2 is not None:
        df1 = df1.reset_index(drop=True)
        df2 = df2.reset_index(drop=True)

        if list(df1.columns) != list(df2.columns):
            st.error("❌ Column mismatch!")
            st.write("File 1 columns:", list(df1.columns))
            st.write("File 2 columns:", list(df2.columns))
        elif len(df1) != len(df2):
            st.error(f"❌ Row count mismatch: {len(df1)} vs {len(df2)}")
        else:
            mismatches = []
            for idx in range(len(df1)):
                for col in df1.columns:
                    val1 = df1.at[idx, col]
                    val2 = df2.at[idx, col]
                    if pd.isnull(val1) and pd.isnull(val2):
                        continue
                    if val1 != val2:
                        mismatches.append({
                            "RowNumber": idx + 1,
                            "Column": col,
                            "File1_Value": val1,
                            "File2_Value": val2
                        })

            if mismatches:
                mismatch_df = pd.DataFrame(mismatches)
                st.warning(f"❌ {len(mismatches)} mismatches found.")
                st.dataframe(mismatch_df.head(10))
                csv = mismatch_df.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Download Mismatches CSV", csv, "mismatches_output.csv", "text/csv")
            else:
                st.success("✅ Files match perfectly!")
