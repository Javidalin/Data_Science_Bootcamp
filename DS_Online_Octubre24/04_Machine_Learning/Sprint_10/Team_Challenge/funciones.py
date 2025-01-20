import pandas as pd
import numpy as np

# Funcion: get_features_num_regression

def get_features_num_regression(df, target_col, umbral_corr, pvalue=None):
    