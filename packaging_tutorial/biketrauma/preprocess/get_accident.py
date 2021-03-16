import  pandas as pd
import numpy as np


def get_accident(df_bikes, log_scale=True):
  gd = df_bikes.groupby(['departement']).size()
  if log_scale:
    gd = np.log(gd)
  return gd

# on a le lien 
#url = https://github.com/bcharlier/HMMA238/blob/master/Courses/Python-modules/modules_files/get_accident.py
#path_target = get_accident.py 
