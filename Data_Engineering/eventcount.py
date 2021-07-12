import glob
import uproot3

file_list = glob.glob("/x4/cms/dylee/Delphes/data/condor/condorplace/ttbarG/condorDelPyOut/*.root")

def counter(f_list):
	sum=0
	empty=0
	trash_files=[]
	for cnt,f in enumerate(f_list):
		dat = uproot3.open(f)
		events = dat['Delphes']
		Nevt = events.numentries
		sum += Nevt
		print(cnt+1,f,Nevt)
	
		if Nevt == 0:
			empty += 1
			trash_files.append(f)

	return cnt,sum,empty,trash_files

cnt,sum,empty,trash_files = counter(file_list)

print("##"*22)
print(" Total {0} evts {1} files ".format(sum,cnt+1))
print(" There are {0} number of zero files".format(empty))
for i in trash_files:
	print(i)
print("##"*22)
