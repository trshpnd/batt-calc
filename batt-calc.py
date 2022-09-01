import pandas as pd
import tkinter as tk
from tkinter import filedialog
import numpy as np

root = tk.Tk()
root.withdraw()

# função de integração
def integrate(x, y):
    return np.trapz(y=y, x=x)

# Índice das colunas de interesse no arquivo .csv
col_time_index = 0          # Coluna timestamp
col_current_index = 1       # Coluna corrente

file_dir = filedialog.askopenfilename()

df = pd.read_csv(file_dir)

# Aquisição do título das colunas para uso com loc
col_time_label = df.columns[col_time_index]
col_current_label = df.columns[col_current_index]

df = df.loc[(df[col_current_label] >= 0) & (df[col_time_label] >= 67.0)]        # remoção de valores inconsistentes
df = df.loc[:,[col_time_label,col_current_label]]                               # remoção de colunas irrelevantes

time = df[col_time_label].values
current = df[col_current_label].values

energy = integrate(time, current)
energy = energy * 0.2778

print(energy, "mAh")
print(df[col_current_label].sum()/3600, "mAh")

#df.to_csv('output.csv', index=False)        # Salva o .csv sem os valores irrelevantes na pasta do script.
