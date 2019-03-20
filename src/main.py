import csv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

#TODO: Scrub the data, there's a lot of redundant values

#   Reads the contents of a dataset into the data array
def read_dataset ( filename ):
    with open ( filename, 'r' ) as f:
        reader = csv.reader ( f )
        data = list ( reader )
        data = np.array ( data, dtype=float )
        return data

def main ( ):
    dataset = read_dataset ( "..\dataset.csv" )

    X = dataset [ :, : 57 ]
    Y = dataset [ :, 57 ]

    knn = KNeighborsClassifier ( n_neighbors = 3 )

    from sklearn.model_selection import cross_val_score
    cvs = cross_val_score ( knn, X, Y, cv = 5 )
    print ( "# CV Accuracy Scores : ", cvs )
    print ( "# CV Accuracy Mean : ", cvs.mean ( ) )

main ( )
