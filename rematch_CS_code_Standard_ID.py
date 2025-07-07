# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 16:54:39 2025

@author: Larissa
"""

import pandas as pd

#Goal: Reassign the ATRAP DRC CS-codes to account for citizen changes throughout the project
    #merge congo_df with the corrected CS_code from cs_id_df
    #use the unique combination of latitude, longitude, and date from drc_df as a key to link it back to merged_congo_df
congo_df = pd.read_csv("C:/Users/Larissa/Downloads/Larissa_Final_Thesis_Data/Larissa_Final_Thesis_Data/Citizen science data (raw and processed)/FOR_CONGO_UGANDA_DRIVE/Paper3/Congo_original.csv")
drc_df = pd.read_csv("C:/Users/Larissa/Downloads/Larissa_Final_Thesis_Data/Larissa_Final_Thesis_Data/Citizen science data (raw and processed)/FOR_CONGO_UGANDA_DRIVE/Paper3/DRC_data_complete_cluster_pop_dw.csv")
cs_id_df = pd.read_csv("C:/Users/Larissa/Downloads/Larissa_Final_Thesis_Data/Larissa_Final_Thesis_Data/Citizen science data (raw and processed)/FOR_CONGO_UGANDA_DRIVE/Paper3/CS_ID_name_UNIQUE.csv")

# Normalize date formats
congo_df['today'] = pd.to_datetime(congo_df['today']).dt.date
drc_df['date'] = pd.to_datetime(drc_df['date']).dt.date

column_names = list(congo_df.columns)
print(column_names)

# Merge keys
congo_df['merge_key'] = congo_df['_Take a GPS point_latitude'].astype(str) + "_" + \
                        congo_df['_Take a GPS point_longitude'].astype(str) + "_" + \
                        congo_df['today'].astype(str)

drc_df['merge_key'] = drc_df['latitude'].astype(str) + "_" + \
                      drc_df['longitude'].astype(str) + "_" + \
                      drc_df['date'].astype(str)

# Merge congo_df with cs_id_df
congo_merged = congo_df.merge(cs_id_df, how='left', left_on='ID', right_on='CS_ID')

# Merge drc_df with the new CS_code using the merge_key
updated_drc = drc_df.merge(
    congo_merged[['merge_key', 'CS_code']],
    on='merge_key',
    how='left'
)

# Replace or add the updated CS_code as Standard_ID
updated_drc['Standard_ID'] = updated_drc['CS_code']

# Drop helper columns
updated_drc.drop(columns=['merge_key', 'CS_code'], inplace=True)

#output the fixed file
#updated_drc.to_csv("DRC_data_complete_cluster_pop_dw_CSFIXED.csv", index=False)


updated_drc['date'] = pd.to_datetime(updated_drc['date'])

# Extract root ID (e.g., DRC-CS007)
updated_drc['root_id'] = updated_drc['Standard_ID'].str.extract(r'^(DRC-CS\d{3})')

# Group by root_id and Standard_ID, and get min/max date per code
activity_periods = updated_drc.groupby(['root_id', 'Standard_ID'])['date'].agg(['min', 'max']).reset_index()
activity_periods = activity_periods.rename(columns={'min': 'start_date', 'max': 'end_date'})

# Sort to view replacements chronologically
activity_periods = activity_periods.sort_values(by=['root_id', 'start_date'])

#activity_periods.to_csv("citizen_scientist_timeline.csv", index=False)
