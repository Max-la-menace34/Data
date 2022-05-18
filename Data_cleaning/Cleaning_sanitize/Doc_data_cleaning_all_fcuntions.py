import pandas as pd
import re
import numpy as np

#Remove Non float value, if you have a char in a float , you will just the float

def removeNonFloat(value=[]):
    new_list = [re.sub('[^0-9.-]', "", str(val)) for val in value]
    return new_list

#Convert number into float 
def convertFloat(value=[]):
    value = [float(val) if val !='' else np.nan for val in value]
    return value

#Convert to int
def convertInt(df,colname):
    df[colname]=np.floor(pd.to_numeric(df[colname], errors='coerce')).astype('Int64')
    return df
#Concatenation of the above functions.

def format_age(df,colname):
    """Format the age column of the DataFrame

    Args: 
        -df: DataFrame
        -non positional argument colname: name of the column (ie. age)
    
    Return:
        -df formatted"""
        
    df[colname] = np.array([re.sub('[^0-9.-]', "", str(val)) for val in df[colname]])
    df[colname] = np.array([float(val) if val !='' else np.nan for val in df[colname]])
    df[colname]=np.floor(pd.to_numeric(df[colname], errors='coerce')).astype('Int64')

    return df
#Format into floats:

def format_price(df,colname):
    """Format the price column of the DataFrame

    Args: 
        -df: DataFrame
        -non positional argument colname: name of the column (ie. price)
    
    Return:
        -df formatted"""
        
    df[colname] = np.array([re.sub('[^0-9.-]', "", str(val)) for val in df[colname]])
    df[colname] = np.array([float(val) if val !='' else np.nan for val in df[colname]])
    return df

# Fill and respect a certain patern
def format_zipcode(df,colname,total_number_to_fill):
    """Format the zipcode column of the DataFrame

    Args: 
        -df: DataFrame
        -non positional argument colname: name of the column (ie. zipcode)
    
    Return:
        -df formatted"""

    df[colname] = np.array([re.sub('[^0-9]', "", str(val)) for val in df[colname]])
    df[colname]=  np.array([str(val).zfill(total_number_to_fill) if (len(str(val))<total_number_to_fill) else str(val) for val in df[colname]])
    df[colname] = np.array([val if val !='00000' else np.nan for val in df[colname]])


    return df

#Format the date into date_time
def format_date(df,colname):
    """Format the date column of the DataFrame

    Args: 
        -df: DataFrame
        -non positional argument colname: name of the column (ie. zipcode)
    
    Return:
        -df formatted"""
    df[colname]=pd.to_datetime(df[colname], errors='coerce')
    return df

#Split into two columns
def splitGps(df,colname):
    df['latitude']=np.array([val[0] if isinstance(val,list) else np.nan for val in df[colname]])
    df['longitude']=np.array([val[1] if isinstance(val,list) else np.nan for val in df[colname]])
    return df

#Keep a number between two numbers
def sanitize_age(dataframe, age_column_label, age_range=(18, 90)):
    age_to_keep_mask = dataframe[age_column_label].between(age_range[0], age_range[1])
    dataframe.loc[age_to_keep_mask == False, age_column_label] = np.nan
    return dataframe

#Between two dates
def sanitize_date(dataframe, date_column_label, date_range=(pd.to_datetime('1/1/1990'), pd.to_datetime('today'))):
    date_to_keep_mask = dataframe[date_column_label].between(date_range[0], date_range[1])
    dataframe.loc[date_to_keep_mask == False, date_column_label] = np.nan    
    return dataframe