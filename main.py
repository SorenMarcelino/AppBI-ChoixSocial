import csv
import os
import shutil
import sys
import random

from driver_mapper_in_dict_dnf import driver_mapper_in_dict_dnf
from format_soc_to_csv import *
from driver_mapper_in_existing_csv import *
from difference_between_dicts import *
from voteUnTour import *
from voteDeuxTours import *
from borda import *
from condorcet import *
from alternative import *
from coombs import *
from kemenyYoung import *
from copeland import *
import pandas as pd
from Statistiques import *
from analyse_merge_tours_results import *

# data_vote = pd.read_csv(filepath_or_buffer='data_web_season/2019.csv', delimiter=',', header=None)
# data_vote = pd.read_csv(filepath_or_buffer='data_web_season/2019.csv', delimiter=',', header=None)

data_vote = None
dossiers = ['data_web_season', 'data_web_races/soc_files']

chemins_dossiers = ['data_web_races/csv_files/', 'fig_alternative/', 'fig_borda', 'fig_condorcet/matrice_condorcet',
                    'fig_condorcet/results_condorcet', 'fig_coombs', 'fig_copeland', 'fig_voteDeuxTours',
                    'fig_voteUnTour', 'res_txt', 'classements_des_saisons_en_fonction_des_methodes_sur_les_courses',
                    'data_web_races_mapped']
driver_list_reference_dict = {}

# Parcourir chaque chemin de dossier et supprimer son contenu
for chemin in chemins_dossiers:
    # Parcourir les fichiers et dossiers dans le dossier
    for element in os.listdir(chemin):
        element_path = os.path.join(chemin, element)
        print(f"Nettoyage de {element_path}...")
        # Vérifier si l'élément est un dossier
        if os.path.isdir(element_path):
            # Récursivement supprimer le contenu du dossier
            shutil.rmtree(element_path)
        else:
            # Supprimer le fichier
            os.remove(element_path)

for dossier in dossiers:
    for fichier in os.listdir(dossier):
        if fichier.endswith('.soc'):  # Assurez-vous que le fichier est un fichier CSV
            chemin_fichier = os.path.join(dossier, fichier)
            driver_list_course_dict = {}
            driver_list_course_dnf_dict = {}

            #print(f"dnf in {chemin_fichier} : {driver_list_course_dnf_dict}")
            # Appel de votre méthode avec le dataframe en tant qu'argument
            csv_file, title, driver_list_reference_dict, driver_list_course_dict = format_soc_to_csv(chemin_fichier, driver_list_reference_dict, driver_list_course_dict, driver_list_course_dnf_dict)
            #print(f"{title}_season : {driver_list_reference_dict}")
            #print(f"{title}_course : {driver_list_course_dict}")
            print("oui: ", csv_file)

            if "data_web_races/csv_files/" in csv_file:
                driver_list_course_dnf_dict = driver_mapper_in_dict_dnf(driver_list_course_dict,
                                                                        driver_list_course_dnf_dict)
                print("dnf_mappés :", driver_list_course_dnf_dict)
                # Charger le fichier CSV dans un DataFrame
                df = pd.read_csv(filepath_or_buffer='data_web_races/csv_files/' + title + '.csv', delimiter=',',
                                 header=None)
                # Créer un dictionnaire avec autant de virgules en valeur que de colonnes dans le DataFrame
                print("longueur :", len(driver_list_course_dnf_dict))


                # BEGIN : Met dans un dictionnaire de listes les classements des participants à chaque tour
                map_tours = {}
                nombre_de_lignes = len(df)
                print("nb lignes : ", nombre_de_lignes)
                key = 0

                for index, row in df.iterrows():
                    for col in df.columns:
                        map_tours[col] = []

                # Loop through every cell
                for index, row in df.iterrows():
                    for col in df.columns:
                        cell_value = row[col]
                        map_tours[col].append(cell_value)
                        # print(f"Row: {index}, Column: {col}, Value: {cell_value}")
                print(f"map_tour_{title} :", map_tours)
                # END: Met dans un dictionnaire de listes les classements des participants à chaque tour

                for i in range(0, len(driver_list_course_dnf_dict)):
                    for key, values in map_tours.items():
                        current_dnf_list = [x for x in list(driver_list_course_dnf_dict.keys()) if x not in values]
                        dnf_selected = random.choice(list(current_dnf_list))
                        map_tours[key].append(dnf_selected)
                print(f"map_tour_{title}_apres_fill_dnf :", map_tours)

                # Création d'un DataFrame à partir du dictionnaire
                df = pd.DataFrame(map_tours)
                # Écriture du DataFrame dans un fichier CSV
                df.to_csv('data_web_races/csv_files/' + title + '.csv', index=False, header=False)

            #print("dossier :", dossier)
            #print("chemin : " + csv_file)
            if "data_web_races/csv_files/" in csv_file:
                driver_mapper_in_existing_csv(csv_file, title, driver_list_reference_dict, driver_list_course_dict)

            #print("chemin : " + csv_file)
    
            data_vote = pd.read_csv(filepath_or_buffer=csv_file, delimiter=',', header=None)
    
            # Ouvrir un fichier en mode écriture
            with open(f'res_txt/{title}.txt', 'w') as f:
                # Rediriger la sortie standard vers le fichier
                sys.stdout = f
    
                '''
                STAT
                '''
    
                # Get size of dataset
                # print(data_vote)
                dim = size_of_dataset(data_vote)
                # print(dim)
                # print("Le dataset contient " + str(dim[1]) + " votants et " + str(dim[0]) + " candidats.")
    
                # uniq_ranks = is_classement_uniq(data_vote)
                # print(uniq_ranks)
    
                frq_val = frequency_per_ranks_per_crit(data_vote)
    
                # plot_frequency(frq_val)
    
                '''
                Fin STAT
                '''
    
                '''
                Vote à 1 tour
                '''
                print("---------- Vote 1 Tour ----------")
                voteUnTour(data_vote, title, False)
                '''
                Fin Vote à 1 tour
                '''
    
                '''
                Vote à 2 tours
                '''
                print("---------- Vote 2 Tours ----------")
                voteDeuxTours(data_vote, title, False)
                '''
                Fin Vote à 2 tours
                '''
    
                '''
                Borda
                '''
                print("---------- Vote Borda ----------")
                classementBorda(methodeBorda(frq_val), title, False)
                sys.stdout = f
                print(vainqueurBorda(methodeBorda(frq_val)))
                plot_borda(frq_val, title, False)
                '''
                Fin Borda
                '''
    
                '''
                Alternatif
                '''
                print("---------- Vote alternatif ----------")
                print(vote_alternatif(data_vote, dim[1]))
                classement_vote_alternatif = vote_alternatif_classement(data_vote, title, False)
                print(classement_vote_alternatif)
                with open(f'classements_des_saisons_en_fonction_des_methodes_sur_les_courses/classementAlternatif_SOCs_2019.csv',
                          'a') as alt:
                    sys.stdout = alt
                    filtered_data = re.sub(r'[^\d,\n]+', '', str(classement_vote_alternatif))
                    alt.write(filtered_data)
                    alt.write("\n")
                sys.stdout = f
    
                '''
                Fin Alternatif
                '''
    
                # -------------------
                # Coombs
                # -------------------
                print("---------- Vote Coombs ----------")
                print(vote_alternatif_coombs(data_vote, dim[1]))
                classement_vote_coombs = vote_alternatif_classement_coombs(data_vote, title, False)
                print(classement_vote_coombs)
                with open(f'classements_des_saisons_en_fonction_des_methodes_sur_les_courses/classementCoombs_SOCs_2019.csv',
                          'a') as coo:
                    sys.stdout = coo
                    filtered_data = re.sub(r'[^\d,\n]+', '', str(classement_vote_coombs))
                    coo.write(filtered_data)
                    coo.write("\n")
                sys.stdout = f
    
                # -------------------
                # Condorcet
                # -------------------
                print("---------- Vote Condorcet ----------")
                condorcet(data_vote, title, False)
    
                # -------------------
                # Kemeny-Young
                # -------------------
                # print("---------- Vote Kemeny-Young ----------")
                # print(kemenyYoung(data_vote))
    
                # -------------------
                # Copeland
                # -------------------
                print("---------- Vote Copeland ----------")
                copeland(data_vote, title, False)
    
                # Restaurer la sortie standard
                sys.stdout = sys.__stdout__
    
chemin_classements = "classements_des_saisons_en_fonction_des_methodes_sur_les_courses"
    
for classement_file in os.listdir(chemin_classements):
    print("Formattage de :", classement_file)
    df = pd.read_csv("classements_des_saisons_en_fonction_des_methodes_sur_les_courses/" + classement_file, header=None)
    df_transposed = df.transpose()
    df_transposed.to_csv("classements_des_saisons_en_fonction_des_methodes_sur_les_courses/" + classement_file, index=False, header=False)

analyse_merge_tours_results()