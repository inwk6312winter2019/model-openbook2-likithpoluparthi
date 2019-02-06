fin= open("Street_Centrelines.csv","r")
str_name=[]
full_name=[]
from_str=[]
to_str=[]
for line in fin:
  line=line.split(",")
  str_name.append(line[2])
  full_name.append(line[4])
  from_str.append(line[6])
  to_str.append(line[7])
task1=zip(str_name,full_name,from_str,to_str)
print(task1)
