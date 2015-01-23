import os
import timeit
import csv

rootdir = 'C:\\Users\\p97244\Documents\\Python Scripts\\'
array = []
for subdir, dirs, files in os.walk(rootdir):
	subdir = subdir[41:]
	array.append(subdir)
array = array[1:]
int_array = [int(numeric_string) for numeric_string in array]

pos = 0

#Add columns to output with driver number and trip

with open("C:\\Users\\p97244\\Documents\\Python Scripts\\"+str(item)+"\\"+str(num)+".csv",'r') as csvinput:
    with open("C:\\Users\\p97244\\Documents\\Python Scripts\\3\\out.csv", 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.extend(['driver','trip'])
        all.append(row)

        for row in reader:
            row.extend([array[1],str(2)])
            all.append(row)

        writer.writerows(all)
		
