import csv
import re
import pandas as pd
import matplotlib.pyplot as plt

def main(): 
    formattedFile = format("mock-data\HeadbandData - Raw.csv") # parses the raw data into a formatted csv file
    df = pd.read_csv(formattedFile, header=None, names=["PackNum", "Marker", "O1", "O2", "T3", "T4"])
    
    df.drop("PackNum", axis=1, inplace=True) # drops the PackNum column bc messes up graph
    df.drop("Marker", axis=1, inplace=True) # drops the Marker column bc messes up graph
    df.drop(index=df.index[:1000], inplace=True) # drops the first 1000 rows bc messes up graph
    
    idxOfMins = df.idxmin()
    print(idxOfMins)
    for i in range(len(idxOfMins)):
        subdf = df.iloc[idxOfMins[i]-500:idxOfMins[i]+500]
        
        name = idxOfMins.index[i]
        low = subdf[name].min()
        idxlow = subdf[name].idxmin()
        high = subdf[name].max()
        idxhigh = subdf[name].idxmax()
        
        print(f'{name} low: {low} @ {idxlow}, high: {high} @ {idxhigh}')
    
    df.plot()
    plt.show()

# Formats the data in the csv file to a proper CSV file
# Returns the name of the new file
def format(file):
    print(f"formatting {file}")
    
    with open(file, 'r') as f:
        reader = csv.reader(f)
        
        with open(str(file) + "-formatted", 'w', newline='') as outF:
            print(f"writing to {str(file) + '-formatted'}")
            writer = csv.writer(outF, delimiter=',')
            
            for row in reader:
                line = re.split("[,\(\)=]", row[0]) # regex matching on commaas, parantheses, and equals sign
                
                packNum = line[2] # first instance of packNum
                marker = line[4] # first instance of marker
                o1 = line[6] # first instance of o1
                o2 = line[8] # first instance of o2
                t3 = line[10] # first instance of t3
                t4 = line[12] # first instance of t4
                
                writer.writerow([packNum, marker, o1, o2, t3, t4])
    
    return str(file) + "-formatted"
                    
main()