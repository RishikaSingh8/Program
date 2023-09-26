import csv
file1=open("Input.csv","r")
read=csv.reader(file1)
file2=open("Output.csv","w")
write=csv.writer(file2)
write.writerows(read)
file1.close()
file2.close()
