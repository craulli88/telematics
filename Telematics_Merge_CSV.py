import os
import timeit
import csv

start = timeit.default_timer()

rootdir = 'C:\\Users\\p97244\Documents\\Python Scripts\\'
array = []
for subdir, dirs, files in os.walk(rootdir):
	subdir = subdir[41:]
	array.append(subdir)
array = array[1:]
int_array = [int(numeric_string) for numeric_string in array]

pos = 0

#Add columns to output with driver number and trip
for item in array:
	for num in range(1,201):
		with open("C:\\Users\\p97244\\Documents\\Python Scripts\\"+str(item)+"\\"+str(num)+".csv",'r') as csvinput:
			with open("C:\\Users\\p97244\\Documents\\Python Scripts\\"+str(item)+"\\"+str(num)+".csv",'w') as csvoutput:
				writer = csv.writer(csvoutput, lineterminator='\n')
				reader = csv.reader(csvinput)
				all = []
				row = next(reader)
				row.extend(['driver','trip'])
				all.append(row)
				for row in reader:
					row.extend([array[num],str(num)])
					all.append(row)
				writer.writerows(all)

#Loop through each folder to stack
for item in array:
	os.chdir("C:\\Users\\p97244\\Documents\\Python Scripts\\"+array[pos])
	fout=open("out.csv","a")
	# first file in folder:
	for line in open("1.csv"):
		fout.write(line)
	# now the rest of the files:    
	for num in range(2,201):	
		f = open(str(num)+".csv")
		for line in f:
			if "x" not in line:
				fout.write(line)
		f.close() # not really needed
	fout.close()

	pos = pos + 1
	
#Print out Success statement and run time.
stop = timeit.default_timer()
seconds = (stop - start)
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print('Merged CSV files in ' + str(pos) + ' folders successfully and the run time was ' + "%d:%02d:%02d" % (h, m, s) + '.')