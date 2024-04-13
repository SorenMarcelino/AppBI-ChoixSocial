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


def analyse_merge_tours_results():
    # data_vote = pd.read_csv(filepath_or_buffer='data_web_season/2019.csv', delimiter=',', header=None)
    # data_vote = pd.read_csv(filepath_or_buffer='data_web_season/2019.csv', delimiter=',', header=None)

    data_vote = None
    dossiers = ['classements_des_saisons_en_fonction_des_methodes_sur_les_courses/']

    for dossier in dossiers:
        for fichier in os.listdir(dossier):
            if fichier.endswith('.csv'):  # Assurez-vous que le fichier est un fichier CSV
                chemin_fichier = os.path.join(dossier, fichier)

                # print(f"{title}_season : {driver_list_reference_dict}")
                # print(f"{title}_course : {driver_list_course_dict}")
                print("oui: ", chemin_fichier)

                data_vote = pd.read_csv(filepath_or_buffer=chemin_fichier, delimiter=',', header=None)

                # Ouvrir un fichier en mode écriture
                with open(f'res_txt/{fichier}.txt', 'w') as f:
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
                    voteUnTour(data_vote, fichier, True)
                    '''
                    Fin Vote à 1 tour
                    '''

                    '''
                    Vote à 2 tours
                    '''
                    print("---------- Vote 2 Tours ----------")
                    voteDeuxTours(data_vote, fichier, True)
                    '''
                    Fin Vote à 2 tours
                    '''

                    '''
                    Borda
                    '''
                    print("---------- Vote Borda ----------")
                    classementBorda(methodeBorda(frq_val), fichier, True)
                    sys.stdout = f
                    print(vainqueurBorda(methodeBorda(frq_val)))
                    plot_borda(frq_val, fichier, True)
                    '''
                    Fin Borda
                    '''

                    '''
                    Alternatif
                    '''
                    print("---------- Vote alternatif ----------")
                    print(vote_alternatif(data_vote, dim[1]))
                    classement_vote_alternatif = vote_alternatif_classement(data_vote, fichier, True)
                    print(classement_vote_alternatif)

                    '''
                    Fin Alternatif
                    '''

                    # -------------------
                    # Coombs
                    # -------------------
                    print("---------- Vote Coombs ----------")
                    print(vote_alternatif_coombs(data_vote, dim[1]))
                    classement_vote_coombs = vote_alternatif_classement_coombs(data_vote, fichier, True)
                    print(classement_vote_coombs)

                    # -------------------
                    # Condorcet
                    # -------------------
                    print("---------- Vote Condorcet ----------")
                    condorcet(data_vote, fichier, True)

                    # -------------------
                    # Kemeny-Young
                    # -------------------
                    # print("---------- Vote Kemeny-Young ----------")
                    # print(kemenyYoung(data_vote))

                    # -------------------
                    # Copeland
                    # -------------------
                    print("---------- Vote Copeland ----------")
                    copeland(data_vote, fichier, True)

                    # Restaurer la sortie standard
                    sys.stdout = sys.__stdout__
