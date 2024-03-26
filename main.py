import os
import sys

from format_soc_to_csv import *
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

#data_vote = pd.read_csv(filepath_or_buffer='data_web_season/2019.csv', delimiter=',', header=None)
#data_vote = pd.read_csv(filepath_or_buffer='data_web_season/2019.csv', delimiter=',', header=None)

data_vote = None
dossier = "data_web_races/soc_files"
for fichier in os.listdir(dossier):
    if fichier.endswith('.soc'):  # Assurez-vous que le fichier est un fichier CSV
        chemin_fichier = os.path.join(dossier, fichier)

        # Appel de votre méthode avec le dataframe en tant qu'argument
        csv_file, title = format_soc_to_csv(chemin_fichier)
        print("chemin : " + csv_file)

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
            voteUnTour(data_vote, title)
            '''
            Fin Vote à 1 tour
            '''

            '''
            Vote à 2 tours
            '''
            print("---------- Vote 2 Tours ----------")
            voteDeuxTours(data_vote, title)
            '''
            Fin Vote à 2 tours
            '''

            '''
            Borda
            '''
            print("---------- Vote Borda ----------")
            classementBorda(methodeBorda(frq_val))
            print(vainqueurBorda(methodeBorda(frq_val)))
            plot_borda(frq_val, title)
            '''
            Fin Borda
            '''

            '''
            Alternatif
            '''
            print("---------- Vote alternatif ----------")
            print(vote_alternatif(data_vote, dim[1]))
            print(vote_alternatif_classement(data_vote, title))
            '''
            Fin Alternatif
            '''

            # -------------------
            # Coombs
            # -------------------
            print("---------- Vote Coombs ----------")
            print(vote_alternatif_coombs(data_vote, dim[1]))
            print(vote_alternatif_classement_coombs(data_vote, title))

            # -------------------
            # Condorcet
            # -------------------
            print("---------- Vote Condorcet ----------")
            condorcet(data_vote, title)

            # -------------------
            # Kemeny-Young
            # -------------------
            # print("---------- Vote Kemeny-Young ----------")
            # print(kemeny_young(data_vote))

            # -------------------
            # Copeland
            # -------------------
            print("---------- Vote Copeland ----------")
            copeland(data_vote, title)

            # Restaurer la sortie standard
            sys.stdout = sys.__stdout__
