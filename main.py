from voteUnTour import *
from borda import *
from alternative import *
import pandas as pd
from Statistiques import *

data_vote = pd.read_csv(filepath_or_buffer='data/exo1_bis.csv', delimiter=',', header=None)

'''
STAT
'''

# Get size of dataset
print(data_vote)
dim = size_of_dataset(data_vote)
print(dim)
print("Le dataset contient " + str(dim[1]) + " classement(s) de " + str(dim[0]) + " critères")

#uniq_ranks = is_classement_uniq(data_vote)
#print(uniq_ranks)

#frq_val = frequency_per_ranks_per_crit(data_vote)

#plot_frequency(frq_val)

'''
Fin STAT
'''

'''
Vote à X tour(s)
'''

#voteUnTour(data_vote)

'''
Vote à X tour(s)
'''


'''
Borda
'''
#classementBorda(methodeBorda(frq_val))
#print(vainqueurBorda(methodeBorda(frq_val)))
'''
Fin Borda
'''

'''
Alternatif
'''
print(vote_alternatif(data_vote, dim[1]))
print(vote_alternatif_classement(data_vote))
'''
Fin Alternatif
'''
