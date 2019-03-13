import csv

#TODO: Scrub the data, there's a lot of redundant values
#TODO: Split the dataset into Training and Test sets

def main ( ):
    with open ( "..\dataset.csv", 'r' ) as f:
        reader = csv.reader ( f )
        for row in reader:
            print ( "# ROW %d %s\n" % ( reader.line_num, row ) )

main ( )
