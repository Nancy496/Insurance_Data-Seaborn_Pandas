# Insurance_Data-Seaborn_Pandas
# Imported the CSV file called *chidata_for_assignment_5* to Jupiter 
# Step 1:Imported Libraries 
    import pandas as njoki
    import seaborn as sbn
# Step 2:Create a DataFrame 
    df = njoki.read_csv('C:\\Users\\User\\Downloads\\chidata_for_assignment_5.csv')
    print(df)
## Output of the code ##
     Gender	Insurance
    0	Male	Insurance
    1	Female	No_Insurance
    2	Male	Insurance
    3	Female	No_Insurance
    4	Male	Insurance
    5	Male	Insurance
## Display DataFrame columns ##
     df.columns
     Index(['Gender', 'Insurance'], dtype='object')
     
