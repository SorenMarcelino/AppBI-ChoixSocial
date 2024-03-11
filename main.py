from voteUnTour import *
import pandas as pd

data_vote = pd.read_csv(filepath_or_buffer='data/exo2.csv', delimiter=',', )

voteUnTour(data_vote)