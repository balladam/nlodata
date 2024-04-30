import sys
import numpy as np
import pandas as pd
import textwrap
from datetime import datetime

import ipywidgets as widgets
from ipywidgets import interact, interact_manual

import IPython.display
from IPython.display import display, clear_output

# import plotly.graph_objects as go

# Globals
input_file_path = "INPUT/Table5B_For_Search.xlsx"
output_file_path = "OUTPUT/OUTPUTFILE.xlsx"

search_text = ""

# helper methods
def get_data_frame():
    try:
        data_frame = pd.read_excel(input_file_path, engine="openpyxl")
        return data_frame
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

def build_columns_for_search():
    print(f"OpticsFunctions.build_columns_for_search()")
    # print(f"OpticsFunctions --> __name__ -->" + __name__)
    
    df = get_data_frame()
    
    # Make the options dynamic to the columns of the data table
    dataColumns = list(df.columns)
    dataColumns.insert(0, "< Any Column >")
    
    return dataColumns

def search_column_selected(val):
    print(val)
    
def search_text_entered(entered_text):
    search_text = entered_text
    perform_search()
    
def perform_search(selected_column, entered_text ):
    #entered_text = search_text.get()

    data_frame = get_data_frame()
    #selected_column = selected_option.get()

    # print(f"Worksheet contains the following data types: {data_frame.dtypes}")
    
    # collect data types
    print(f"Search column contains the following data types: {data_frame[selected_column].dtypes}")

    try:
        result_df = data_frame[data_frame[selected_column].str.contains(entered_text, case=False)]
    except Exception as e:
        print(f"Unable to run text query: {e}")
        print("reverting to basic query that will work for numbers")

        # generate our query (if column names have whitespace we must wrap in back ticks)
        query_to_run = f"`{selected_column}` == {entered_text}"

        print(f"running query -> {query_to_run}")

        # TODO: might be better to do all this with inplace=True but would require reworking
        result_df = data_frame.query(query_to_run, inplace=False)
    
    print(result_df)
    
def export_to_csv(target_data):
    print(f"OpticsFunctions.export_to_csv()")
    
    file_name = 'OUTPUT/' + datetime.now().strftime("OpticsExport__%d-%m-%Y_%H-%M-%S")+".csv"
    target_data.to_csv(file_name, index=False)  

    print(f"CSV exported to " + file_name)

def main():
    print(f"starting...")
    
    df = get_data_frame()

    # Check the type
    # print(type(df))

    # print(df)
    return df

    print(f"main exiting...")

if __name__ == "__main__":
    print(f"calling main...")
    main()
    print(f"simply.py exiting...")
