import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


def ohe_list_col(df, df_col, prefix='f_'):
    """Take in a dataframe and column with a list of values, return same dataframe with OHE columns"""
    
    # Create dataframe with list values
    data = df[df_col].str.split(',').tolist()
    cat_df = pd.DataFrame(data, index=df.index).stack()

    cat_df = cat_df.reset_index()

    cat_df = cat_df.drop('level_1', axis=1)

    cat_df.columns = ['id', df_col]
    
    # Perform One Hot Encoding on values dataframe
    encoder = OneHotEncoder(categories="auto").fit(cat_df[[df_col]])
    
    ohe = pd.DataFrame(encoder.transform(cat_df[[df_col]]).toarray(),
                   columns=encoder.get_feature_names([prefix]))

    ohe_df = pd.concat([cat_df.drop(df_col, axis=1), ohe], axis=1)
    
    # Remove duplicate rows and merge back to single row for each 
    dedup = ohe_df.groupby('id')[ohe.columns].agg("sum").reset_index()
    dedup = dedup.drop('id', axis=1)
    
    # Combine original dataframe with new One Hot Encoded columns and remove original column
    df_complete = pd.concat([df, dedup], axis=1)
    df_complete = df_complete.drop(df_col, axis=1)
    
    return df_complete