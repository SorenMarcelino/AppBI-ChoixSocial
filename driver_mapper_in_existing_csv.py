import pandas as pd


def driver_mapper_in_existing_csv(csv, title, driver_list_reference_dict, driver_list_course_dict):
    df = pd.read_csv(csv, delimiter=',', header=None)

    for index, row in df.iterrows():
        for column, key in row.items():
            course_value_csv_dict = driver_list_course_dict[key]
            for cle, valeur in driver_list_reference_dict.items():
                if valeur == course_value_csv_dict:
                    # Remplace la valeur de la cellule du csv par cle
                    df.at[index, column] = cle
    df.to_csv(csv, index=False, header=False)
