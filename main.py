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

data_vote = pd.read_csv(filepath_or_buffer='data/profil2.csv', delimiter=',', header=None)
#data_vote = pd.read_csv(filepath_or_buffer='data_web/2019.csv', delimiter=',', header=None)

format_soc_to_csv()

'''
STAT
'''

# Get size of dataset
#print(data_vote)
dim = size_of_dataset(data_vote)
#print(dim)
#print("Le dataset contient " + str(dim[1]) + " votants et " + str(dim[0]) + " candidats.")

#uniq_ranks = is_classement_uniq(data_vote)
#print(uniq_ranks)

frq_val = frequency_per_ranks_per_crit(data_vote)

#plot_frequency(frq_val)

'''
Fin STAT
'''

'''
Vote à 1 tour
'''
print("---------- Vote 1 Tour ----------")
voteUnTour(data_vote)
'''
Fin Vote à 1 tour
'''

'''
Vote à 2 tours
'''
print("---------- Vote 2 Tours ----------")
voteDeuxTours(data_vote)
'''
Fin Vote à 2 tours
'''

'''
Borda
'''
print("---------- Vote Borda ----------")
classementBorda(methodeBorda(frq_val))
print(vainqueurBorda(methodeBorda(frq_val)))
plot_borda(frq_val)
'''
Fin Borda
'''


'''
Alternatif
'''
print("---------- Vote alternatif ----------")
print(vote_alternatif(data_vote, dim[1]))
print(vote_alternatif_classement(data_vote))
'''
Fin Alternatif
'''


# -------------------
# Coombs
# -------------------
print("---------- Vote Coombs ----------")
print(vote_alternatif_coombs(data_vote, dim[1]))
print(vote_alternatif_classement_coombs(data_vote))

# -------------------
# Condorcet
# -------------------
print("---------- Vote Condorcet ----------")
condorcet(data_vote)


# -------------------
# Kemeny-Young
# -------------------
#print("---------- Vote Kemeny-Young ----------")
#(top_kemenyYoung, rank_kemenyYoung) = kemenyYoung(data_vote)

# -------------------
# Copeland
# -------------------
print("---------- Vote Copeland ----------")
copeland(data_vote)


