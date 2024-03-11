import pandas as pd
from Statistiques import *

data_vote = pd.read_csv(filepath_or_buffer='data/profil2.csv', delimiter=',', header=None)

# Get size of dataset
print(data_vote)
dim = size_of_dataset(data_vote)
print(dim)
print("Le dataset contient " + str(dim[1]) + " classement(s) de " + str(dim[0]) + " critères")

uniq_ranks = is_classement_uniq(data_vote)
print(uniq_ranks)

frq_val = frequency_per_ranks_per_crit(data_vote)

plot_frequency(frq_val)