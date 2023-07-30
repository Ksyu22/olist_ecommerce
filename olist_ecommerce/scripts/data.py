import os
import pandas as pd


class Olist_Data:
    def get_data_from_csv(self):
        """
        Returns data dictionnary which consisites of :
        key - name of dataset
        value - df withn all the data from .csv file
        """
        # getting the path with data
        data_path = os.path.join('..' , 'raw_data')
        # names of files inside the path
        file_name_list = os.listdir(data_path)
        file_name_list

        # creating the list names of datasets
        datasets_names = []

        for n in file_name_list:
            name = n.replace('.csv','').replace('_dataset','').replace('olist_', '')
            datasets_names.append(name)

        # whole datasets in one dictionnary
        data_dict = {}

        for (file, name) in zip(file_name_list, datasets_names):
            data_dict[name] = pd.read_csv(os.path.join(data_path, file))

        return data_dict
