import sys

input_text="""######################################################################
## PARAM_CARD AUTOMATICALY GENERATED BY MG5 FOLLOWING UFO MODEL   ####
######################################################################
##                                                                  ##
##  Width set on Auto will be computed following the information    ##
##        present in the decay.py files of the model.               ##
##        See  arXiv:1402.1178 for more details.                    ##
##                                                                  ##
######################################################################

###################################
## INFORMATION FOR ANOINPUTS
###################################
Block anoinputs 
    1 0.000000e-08 # FS0 
    2 0.000000e-08 # FS1 
    3 0.000000e-08 # FS2 
    4 """+sys.argv[1]+""".000000e-"""+sys.argv[2]+""" # FM0 
    5 0.000000e-08 # FM1 
    6 0.000000e-08 # FM2 
    7 0.000000e-08 # FM3 
    8 0.000000e-08 # FM4 
    9 0.000000e-08 # FM5 
   10 0.000000e-08 # FM6 
   11 0.000000e-08 # FM7 
   12 0.000000e-08 # FT0 
   13 0.000000e-08 # FT1 
   14 0.000000e-08 # FT2 
   15 0.000000e-08 # FT3 
   16 0.000000e-08 # FT4 
   17 0.000000e-08 # FT5 
   18 0.000000e-08 # FT6 
   19 0.000000e-08 # FT7 
   20 0.000000e-08 # FT8 
   21 0.000000e-08 # FT9 

###################################
## INFORMATION FOR CKMBLOCK
###################################
Block ckmblock 
    1 2.277360e-01 # cabi 

###################################
## INFORMATION FOR MASS
###################################
Block mass 
    6 1.720000e+02 # MT 
   13 1.056600e-01 # MMU 
   15 1.777000e+00 # MTA 
   23 9.118760e+01 # MZ 
   25 1.250000e+02 # MH 
## Dependent parameters, given by model restrictions.
## Those values should be edited following the 
## analytical expression. MG5 ignores those values 
## but they are important for interfacing the output of MG5
## to external program such as Pythia.
  1 0.000000e+00 # d : 0.0 
  2 0.000000e+00 # u : 0.0 
  3 0.000000e+00 # s : 0.0 
  4 0.000000e+00 # c : 0.0 
  5 0.000000e+00 # b : 0.0 
  11 0.000000e+00 # e- : 0.0 
  12 0.000000e+00 # ve : 0.0 
  14 0.000000e+00 # vm : 0.0 
  16 0.000000e+00 # vt : 0.0 
  21 0.000000e+00 # g : 0.0 
  22 0.000000e+00 # a : 0.0 
  24 7.982436e+01 # w+ : cmath.sqrt(MZ__exp__2/2. + cmath.sqrt(MZ__exp__4/4. - (aEW*cmath.pi*MZ__exp__2)/(Gf*sqrt__2))) 

###################################
## INFORMATION FOR SMINPUTS
###################################
Block sminputs 
    1 1.279000e+02 # aEWM1 
    2 1.166370e-05 # Gf 
    3 1.184000e-01 # aS 

###################################
## INFORMATION FOR YUKAWA
###################################
Block yukawa 
    6 1.720000e+02 # ymt 
   15 1.777000e+00 # ymtau 

###################################
## INFORMATION FOR DECAY
###################################
DECAY   6 1.508336e+00 # WT 
DECAY  23 2.495200e+00 # WZ 
DECAY  24 2.085000e+00 # WW 
DECAY  25 4.070000e-03 # WH 
## Dependent parameters, given by model restrictions.
## Those values should be edited following the 
## analytical expression. MG5 ignores those values 
## but they are important for interfacing the output of MG5
## to external program such as Pythia.
DECAY  1 0.000000e+00 # d : 0.0 
DECAY  2 0.000000e+00 # u : 0.0 
DECAY  3 0.000000e+00 # s : 0.0 
DECAY  4 0.000000e+00 # c : 0.0 
DECAY  5 0.000000e+00 # b : 0.0 
DECAY  11 0.000000e+00 # e- : 0.0 
DECAY  12 0.000000e+00 # ve : 0.0 
DECAY  13 0.000000e+00 # mu- : 0.0 
DECAY  14 0.000000e+00 # vm : 0.0 
DECAY  15 0.000000e+00 # ta- : 0.0 
DECAY  16 0.000000e+00 # vt : 0.0 
DECAY  21 0.000000e+00 # g : 0.0 
DECAY  22 0.000000e+00 # a : 0.0"""

inputfile = open("../FM0/FM0_{0}_{1}/FM0_{0}_{1}_param_card.dat".format(sys.argv[1],sys.argv[2]),"w")
inputfile.write(input_text)
inputfile.close()
