import matplotlib.pyplot as plt
import os
import pandas as pd
from src.dataset_management import filemanager
from src.dataset_management import towfileseparator

from pathlib import Path

basePath = Path(__file__).parent.parent.parent.as_posix()
print(basePath)

path = basePath + "/Dataset/iskra/"
saving_path =  basePath + "/Dataset/csv_files/"
saving_path2 =  basePath + "/Dataset/csv_files_tagged/"

filemanager.get_all_csv(path)
towfileseparator.separate_tows(path, saving_path)

filenames = os.listdir(saving_path)
filenames.sort()
for csv in filenames:
    dataframe = pd.read_csv(saving_path + csv)
    if len(dataframe) > 1:
        print(csv)
        fig, axs = plt.subplots(2)
        axs[0].set_title("Apertura(m)")
        try:
            axs[0].plot(dataframe["Datos1(Fa)Estribor"])
        except:
            try:
                axs[0].plot(dataframe["Datos1(m)Estribor"])
            except:
                axs[0].plot(dataframe["Datos1(°)Estribor"])
        axs[0].set_ylim([0, None])
        axs[1].set_title("Profundidade(m)")
        #axs[1].set_ylim([0, None])
        axs[1].plot(dataframe["Escalas(m)Estribor"])
        plt.pause(0.05)
        bad_input = True
        while(bad_input):
            embarra = input("Embarra? ->")
            if embarra == "1" or embarra == "0":
                bad_input = False
                csv = csv + "-embarra=" + embarra + ".csv"
                dataframe.to_csv(saving_path2 + csv)
            elif embarra == "2":
                os.remove(saving_path + csv)
                print(saving_path + csv + " was removed")
                bad_input = False
            else:
                print("Wrong input")
        plt.show()
        plt.close()
