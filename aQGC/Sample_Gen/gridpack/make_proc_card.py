import sys

input_text="""import model QCKM_5_Aug21v2

define nu = ve vm ve~ vm~
define w = w+ w-
define l = e+ mu+ e- mu-
generate p p > w z a NP=1, w > l nu, z > l+ l-
output FM0_"""+sys.argv[1]+"""_"""+sys.argv[2]+""" -nojpeg"""

inputfile = open("../FM0/FM0_{0}_{1}/FM0_{0}_{1}_proc_card.dat".format(sys.argv[1],sys.argv[2]),"w")
inputfile.write(input_text)
inputfile.close()
