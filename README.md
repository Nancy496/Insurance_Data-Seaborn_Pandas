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
     
## Display the column using the head_for quick testing return the first N rows ##
       df.head()
     Gender	Insurance
    0	Male	Insurance
    1	Female	No_Insurance
    2	Male	Insurance
    3	Female	No_Insurance
    4	Male	Insurance
 ## Print/Display the column Information
    
     df.info()
     <class 'pandas.core.frame.DataFrame'>
     RangeIndex: 49 entries, 0 to 48
    Data columns (total 2 columns):
    #   Column     Non-Null Count  Dtype 
    ---  ------     --------------  ----- 
    0   Gender     49 non-null     object
    1   Insurance  49 non-null     object
    dtypes: object(2)
    memory usage: 912.0+ bytes
## Generate a seaborn count plot of the other Gender##
     Text(0.5, 1.0, 'Categories for Gender difference in Health')
     ![image](https://user-images.githubusercontent.com/75600702/113417655-41049c80-939a-11eb-83fe-39b35406a210.png)
## Generates a count plot for insurance ##
    #Adding the title to the Chart
 gender_count.set_title("Category for Insurance")
 Text(0.5, 1.0, 'Category for Insurance')
## Contingency Table showing correlation between Gender and Insurance ##
    #Generate a count for Insurance
    gender_count = njoki.DataFrame(df)
    gender_count = sbn.countplot(x="Insurance", data=df)
    #Adding appropriate Chart Title
    gender_count.set_title("Categories for Gender difference in Health")
## Visualize categorical variables gender and insurance with heatmaps ##
    Create a heatmap fo the contingency cross table
    gender_count = sbn.heatmap(emily)
    gender_count.set(title='Insurance (M/F)', xlabel='Insurance Results', ylabel='Gender')
    ![image](https://user-images.githubusercontent.com/75600702/113418937-d43ed180-939c-11eb-99b3-
  
    8e67af231b61.png)
## See visually the contingency tables using seaborn heatmaps ##
    #Examples with Matplotlib
    #import the necessary packages
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    #prepare the data
    nancy = np.linspace(0, 10, 100)
    #Plot the data
    plt.plot(nancy, nancy, label='linear')
    ![image](https://user-images.githubusercontent.com/75600702/113419164-4adbcf00-939d-11eb-854f-
    49dbaf43a1c3.png)
    
   



