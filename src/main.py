import csv

#TODO: Scrub the data, there's a lot of redundant values
#TODO: Split the dataset into Training and Test sets

#   Reads the contents of a dataset into the data array
def read_dataset ( filename, training_set = [ ], test_set = [ ] ):
    with open ( filename, 'r' ) as f:
        reader = csv.reader ( f )
        data = list ( reader )
        training_set.append ( data [ 0:3680 ] )
        test_set.append ( data [ 3681:4600 ] )
        # print ( data )

def main ( ):
    training = [ ]  #   Contains Training Set
    test = [ ]      #   Contains Test Set

    read_dataset ( "..\dataset.csv", training, test )

    for row in training:
        print ( row )

main ( )
