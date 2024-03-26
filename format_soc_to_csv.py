import re
import pandas as pd


def format_soc_to_csv(chemin_soc_file):
    title = None
    alternative_names = []
    lines = []
    with open(chemin_soc_file, "r") as file:
        # Parcourir chaque ligne du fichier
        for line in file:
            # Utiliser une expression régulière pour trouver les lignes commençant par "TITLE"
            if line.startswith("# TITLE"):
                title = re.match("# TITLE: (.+)", line)
                if title:
                    title = title.group(1)
            if line.startswith("# ALTERNATIVE NAME"):
                # Extraire le nom de l'alternative en utilisant une expression régulière
                alternative_name = re.match(r'# ALTERNATIVE NAME (\d+): (.+)', line)
                # Ajouter le nom de l'alternative à la liste
                if alternative_name:
                    alternative_names.append(alternative_name.group(2))
            lines.append(line)
        if "data_web_season" in chemin_soc_file:
            print("oui")
            with open('data_web_season/' + title + '.csv', 'w') as f_out:
                # Parcourir chaque ligne du fichier d'entrée
                for line in lines:
                    # Vérifier si la ligne ne commence pas par "#"
                    if not line.startswith('#'):
                        # Écrire la ligne dans le fichier de sortie
                        line = line.split(":", 1)[-1]
                        f_out.write(line)

            df = pd.read_csv("data_web_season/" + title + ".csv", header=None)
            df_transposed = df.transpose()
            df_transposed.to_csv("data_web_season/" + title + ".csv", index=False, header=False)

            # Afficher la liste des noms d'alternatives
            print(title)
            print(alternative_names)
            return f"data_web_season/{title}.csv", title

        elif "data_web_races/soc_files/" in chemin_soc_file:
            print("non")
            with open('data_web_races/csv_files/' + title + '.csv', 'w') as f_out:
                # Parcourir chaque ligne du fichier d'entrée
                for line in lines:
                    # Vérifier si la ligne ne commence pas par "#"
                    if not line.startswith('#'):
                        # Écrire la ligne dans le fichier de sortie
                        line = line.split(":", 1)[-1]
                        f_out.write(line)

            df = pd.read_csv("data_web_races/csv_files/" + title + ".csv", header=None)
            df_transposed = df.transpose()
            df_transposed.to_csv("data_web_races/csv_files/" + title + ".csv", index=False, header=False)

            # Afficher la liste des noms d'alternatives
            print(title)
            print(alternative_names)
            return f"data_web_races/csv_files/{title}.csv", title
