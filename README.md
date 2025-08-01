# ATRAP
Scripts relating to project ATRAP 
Use the rematch_CS_code_Standard_ID.py on three CSV files: Congo_original, CS_ID_name_UNIQUE, and DRC_data_complete_cluster_pop_dw. 

The goal was to link the ID of Congo_original to the unique CS_code per unique citizen in CS_ID_name_UNIQUE. Then, use that to replace the Standard_ID in DRC_data_complete_cluster_pop_dw (our final dataset) so it has the proper citizen assigned to each sampling 

The CSV citizen_scientist_timeline gives information on when citizens changed based on Congo_original 

-2 CS IDs in final filtered data have multiple individuals: DRC-CS002 and DRC-CS007 

-DRC-CS002 is clearly replaced sometime in January 2021, but there is a slight overlap of 16 days (leave as is?) 

-DRC-CS007 is replaced in October 2020; but in March 2022 – August 2022, a generic code was used (no name – will assume it is the same replacement citizen – manually replaced and added _7.csv at the end) 
