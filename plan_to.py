import csv, os, sys, requests


def row_to_list(row):
    # переводит ряды в список 
    big_row = []
    delete = "'[]"
    for row in reader:
        row = str(row)
        row = row[2:-2]
        big_row.append(str(row))
    for i in big_row:
        requests.post(i)
    

if __name__ == "__main__":

    csv_path = "c:/Users/masyuk_as/projects/work/plans.csv"
    csv_path = os.path.join(os.path.dirname(__file__), 'plans.csv')
    
    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        row_to_list(reader)

        