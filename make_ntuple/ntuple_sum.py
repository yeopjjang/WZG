import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import awkward1 as ak

# Data path
WZG1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/signal_part1_emm.npy'
WZG2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/signal_part2_emm.npy'

#WG1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WG_part1_emm.npy'
WG1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WG_part1_emm.npy'

ZG1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/ZG_part1_emm.npy'
ZG2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/ZG_part2_emm.npy'

WW1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WW_part1_emm.npy'
WW2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WW_part2_emm.npy'

WZ1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WZ_part1_emm.npy'
WZ2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WZ_part2_emm.npy'

ZZ1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/ZZ_part1_emm.npy'
ZZ2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/ZZ_part2_emm.npy'

WWW1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WWW_part1_emm.npy'
WWW2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WWW_part2_emm.npy'

WWZ1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WWZ_part1_emm.npy'
WWZ2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WWZ_part2_emm.npy'

WZZ1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WZZ_part1_emm.npy'
WZZ2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/WZZ_part2_emm.npy'

ZZZ1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/ZZZ_part1_emm.npy'
ZZZ2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/ZZZ_part2_emm.npy'

ttbarG1 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/ttbar_part1_emm.npy'
ttbarG2 = '/x4/cms/dylee/Delphes/output_npy/jjinmak/condorOut_emm/ttbar_part2_emm.npy'

# Data load & Make array
WZG1_Ntuples = np.load(WZG1,allow_pickle=True)[()]
WZG2_Ntuples = np.load(WZG2,allow_pickle=True)[()]

#WG1_Ntuples = np.load(WG1,allow_pickle=True)[()]
WG1_Ntuples = np.load(WG1,allow_pickle=True)[()]

ZG1_Ntuples = np.load(ZG1,allow_pickle=True)[()]
ZG2_Ntuples = np.load(ZG2,allow_pickle=True)[()]

WW1_Ntuples = np.load(WW1,allow_pickle=True)[()]
WW2_Ntuples = np.load(WW2,allow_pickle=True)[()]

WZ1_Ntuples = np.load(WZ1,allow_pickle=True)[()]
WZ2_Ntuples = np.load(WZ2,allow_pickle=True)[()]

ZZ1_Ntuples = np.load(ZZ1,allow_pickle=True)[()]
ZZ2_Ntuples = np.load(ZZ2,allow_pickle=True)[()]

WWW1_Ntuples = np.load(WWW1,allow_pickle=True)[()]
WWW2_Ntuples = np.load(WWW2,allow_pickle=True)[()]

WWZ1_Ntuples = np.load(WWZ1,allow_pickle=True)[()]
WWZ2_Ntuples = np.load(WWZ2,allow_pickle=True)[()]

WZZ1_Ntuples = np.load(WZZ1,allow_pickle=True)[()]
WZZ2_Ntuples = np.load(WZZ2,allow_pickle=True)[()]

ZZZ1_Ntuples = np.load(ZZZ1,allow_pickle=True)[()]
ZZZ2_Ntuples = np.load(ZZZ2,allow_pickle=True)[()]

ttbarG1_Ntuples = np.load(ttbarG1,allow_pickle=True)[()]
ttbarG2_Ntuples = np.load(ttbarG2,allow_pickle=True)[()]

## Variable

# Dilep
WZG1_Dilep = WZG1_Ntuples['Dilep'].flatten()
WZG2_Dilep = WZG2_Ntuples['Dilep'].flatten()

#WG1_Dilep = WG1_Ntuples['Dilep'].flatten()
WG1_Dilep = WG1_Ntuples['Dilep'].flatten()

ZG1_Dilep = ZG1_Ntuples['Dilep'].flatten()
ZG2_Dilep = ZG2_Ntuples['Dilep'].flatten()

WW1_Dilep = WW1_Ntuples['Dilep'].flatten()
WW2_Dilep = WW2_Ntuples['Dilep'].flatten()

WZ1_Dilep = WZ1_Ntuples['Dilep'].flatten()
WZ2_Dilep = WZ2_Ntuples['Dilep'].flatten()

ZZ1_Dilep = ZZ1_Ntuples['Dilep'].flatten()
ZZ2_Dilep = ZZ2_Ntuples['Dilep'].flatten()

WWW1_Dilep = WWW1_Ntuples['Dilep'].flatten()
WWW2_Dilep = WWW2_Ntuples['Dilep'].flatten()

WWZ1_Dilep = WWZ1_Ntuples['Dilep'].flatten()
WWZ2_Dilep = WWZ2_Ntuples['Dilep'].flatten()

WZZ1_Dilep = WZZ1_Ntuples['Dilep'].flatten()
WZZ2_Dilep = WZZ2_Ntuples['Dilep'].flatten()

ZZZ1_Dilep = ZZZ1_Ntuples['Dilep'].flatten()
ZZZ2_Dilep = ZZZ2_Ntuples['Dilep'].flatten()

ttbarG1_Dilep = ttbarG1_Ntuples['Dilep'].flatten()
ttbarG2_Dilep = ttbarG2_Ntuples['Dilep'].flatten()

# Trilep
WZG1_Trilep = WZG1_Ntuples['Trilep'].flatten()
WZG2_Trilep = WZG2_Ntuples['Trilep'].flatten()

#WG1_Trilep = WG1_Ntuples['Trilep'].flatten()
WG1_Trilep = WG1_Ntuples['Trilep'].flatten()

ZG1_Trilep = ZG1_Ntuples['Trilep'].flatten()
ZG2_Trilep = ZG2_Ntuples['Trilep'].flatten()

WW1_Trilep = WW1_Ntuples['Trilep'].flatten()
WW2_Trilep = WW2_Ntuples['Trilep'].flatten()

WZ1_Trilep = WZ1_Ntuples['Trilep'].flatten()
WZ2_Trilep = WZ2_Ntuples['Trilep'].flatten()

ZZ1_Trilep = ZZ1_Ntuples['Trilep'].flatten()
ZZ2_Trilep = ZZ2_Ntuples['Trilep'].flatten()

WWW1_Trilep = WWW1_Ntuples['Trilep'].flatten()
WWW2_Trilep = WWW2_Ntuples['Trilep'].flatten()

WWZ1_Trilep = WWZ1_Ntuples['Trilep'].flatten()
WWZ2_Trilep = WWZ2_Ntuples['Trilep'].flatten()

WZZ1_Trilep = WZZ1_Ntuples['Trilep'].flatten()
WZZ2_Trilep = WZZ2_Ntuples['Trilep'].flatten()

ZZZ1_Trilep = ZZZ1_Ntuples['Trilep'].flatten()
ZZZ2_Trilep = ZZZ2_Ntuples['Trilep'].flatten()

ttbarG1_Trilep = ttbarG1_Ntuples['Trilep'].flatten()
ttbarG2_Trilep = ttbarG2_Ntuples['Trilep'].flatten()

# Trileppho
WZG1_Trileppho = WZG1_Ntuples['Trileppho'].flatten()
WZG2_Trileppho = WZG2_Ntuples['Trileppho'].flatten()

#WG1_Trileppho = WG1_Ntuples['Trileppho'].flatten()
WG1_Trileppho = WG1_Ntuples['Trileppho'].flatten()

ZG1_Trileppho = ZG1_Ntuples['Trileppho'].flatten()
ZG2_Trileppho = ZG2_Ntuples['Trileppho'].flatten()

WW1_Trileppho = WW1_Ntuples['Trileppho'].flatten()
WW2_Trileppho = WW2_Ntuples['Trileppho'].flatten()

WZ1_Trileppho = WZ1_Ntuples['Trileppho'].flatten()
WZ2_Trileppho = WZ2_Ntuples['Trileppho'].flatten()

ZZ1_Trileppho = ZZ1_Ntuples['Trileppho'].flatten()
ZZ2_Trileppho = ZZ2_Ntuples['Trileppho'].flatten()

WWW1_Trileppho = WWW1_Ntuples['Trileppho'].flatten()
WWW2_Trileppho = WWW2_Ntuples['Trileppho'].flatten()

WWZ1_Trileppho = WWZ1_Ntuples['Trileppho'].flatten()
WWZ2_Trileppho = WWZ2_Ntuples['Trileppho'].flatten()

WZZ1_Trileppho = WZZ1_Ntuples['Trileppho'].flatten()
WZZ2_Trileppho = WZZ2_Ntuples['Trileppho'].flatten()

ZZZ1_Trileppho = ZZZ1_Ntuples['Trileppho'].flatten()
ZZZ2_Trileppho = ZZZ2_Ntuples['Trileppho'].flatten()

ttbarG1_Trileppho = ttbarG1_Ntuples['Trileppho'].flatten()
ttbarG2_Trileppho = ttbarG2_Ntuples['Trileppho'].flatten()

# lep1
WZG1_lep1 = WZG1_Ntuples['lep1'].flatten()
WZG2_lep1 = WZG2_Ntuples['lep1'].flatten()

#WG1_lep1 = WG1_Ntuples['lep1'].flatten()
WG1_lep1 = WG1_Ntuples['lep1'].flatten()

ZG1_lep1 = ZG1_Ntuples['lep1'].flatten()
ZG2_lep1 = ZG2_Ntuples['lep1'].flatten()

WW1_lep1 = WW1_Ntuples['lep1'].flatten()
WW2_lep1 = WW2_Ntuples['lep1'].flatten()

WZ1_lep1 = WZ1_Ntuples['lep1'].flatten()
WZ2_lep1 = WZ2_Ntuples['lep1'].flatten()

ZZ1_lep1 = ZZ1_Ntuples['lep1'].flatten()
ZZ2_lep1 = ZZ2_Ntuples['lep1'].flatten()

WWW1_lep1 = WWW1_Ntuples['lep1'].flatten()
WWW2_lep1 = WWW2_Ntuples['lep1'].flatten()

WWZ1_lep1 = WWZ1_Ntuples['lep1'].flatten()
WWZ2_lep1 = WWZ2_Ntuples['lep1'].flatten()

WZZ1_lep1 = WZZ1_Ntuples['lep1'].flatten()
WZZ2_lep1 = WZZ2_Ntuples['lep1'].flatten()

ZZZ1_lep1 = ZZZ1_Ntuples['lep1'].flatten()
ZZZ2_lep1 = ZZZ2_Ntuples['lep1'].flatten()

ttbarG1_lep1 = ttbarG1_Ntuples['lep1'].flatten()
ttbarG2_lep1 = ttbarG2_Ntuples['lep1'].flatten()

# lep1 flavor
WZG1_lep1_Flav = WZG1_Ntuples['lep1_Flav'].flatten()
WZG2_lep1_Flav = WZG2_Ntuples['lep1_Flav'].flatten()

#WG1_lep1_Flav = WG1_Ntuples['lep1_Flav'].flatten()
WG1_lep1_Flav = WG1_Ntuples['lep1_Flav'].flatten()

ZG1_lep1_Flav = ZG1_Ntuples['lep1_Flav'].flatten()
ZG2_lep1_Flav = ZG2_Ntuples['lep1_Flav'].flatten()

WW1_lep1_Flav = WW1_Ntuples['lep1_Flav'].flatten()
WW2_lep1_Flav = WW2_Ntuples['lep1_Flav'].flatten()

WZ1_lep1_Flav = WZ1_Ntuples['lep1_Flav'].flatten()
WZ2_lep1_Flav = WZ2_Ntuples['lep1_Flav'].flatten()

ZZ1_lep1_Flav = ZZ1_Ntuples['lep1_Flav'].flatten()
ZZ2_lep1_Flav = ZZ2_Ntuples['lep1_Flav'].flatten()

WWW1_lep1_Flav = WWW1_Ntuples['lep1_Flav'].flatten()
WWW2_lep1_Flav = WWW2_Ntuples['lep1_Flav'].flatten()

WWZ1_lep1_Flav = WWZ1_Ntuples['lep1_Flav'].flatten()
WWZ2_lep1_Flav = WWZ2_Ntuples['lep1_Flav'].flatten()

WZZ1_lep1_Flav = WZZ1_Ntuples['lep1_Flav'].flatten()
WZZ2_lep1_Flav = WZZ2_Ntuples['lep1_Flav'].flatten()

ZZZ1_lep1_Flav = ZZZ1_Ntuples['lep1_Flav'].flatten()
ZZZ2_lep1_Flav = ZZZ2_Ntuples['lep1_Flav'].flatten()

ttbarG1_lep1_Flav = ttbarG1_Ntuples['lep1_Flav'].flatten()
ttbarG2_lep1_Flav = ttbarG2_Ntuples['lep1_Flav'].flatten()

# lep1 Charge
WZG1_lep1_C = WZG1_Ntuples['lep1_C']
WZG2_lep1_C = WZG2_Ntuples['lep1_C']

#WG1_lep1_C = WG1_Ntuples['lep1_C']
WG1_lep1_C = WG1_Ntuples['lep1_C']

ZG1_lep1_C = ZG1_Ntuples['lep1_C']
ZG2_lep1_C = ZG2_Ntuples['lep1_C']

WW1_lep1_C = WW1_Ntuples['lep1_C']
WW2_lep1_C = WW2_Ntuples['lep1_C']

WZ1_lep1_C = WZ1_Ntuples['lep1_C']
WZ2_lep1_C = WZ2_Ntuples['lep1_C']

ZZ1_lep1_C = ZZ1_Ntuples['lep1_C']
ZZ2_lep1_C = ZZ2_Ntuples['lep1_C']

WWW1_lep1_C = WWW1_Ntuples['lep1_C']
WWW2_lep1_C = WWW2_Ntuples['lep1_C']

WWZ1_lep1_C = WWZ1_Ntuples['lep1_C']
WWZ2_lep1_C = WWZ2_Ntuples['lep1_C']

WZZ1_lep1_C = WZZ1_Ntuples['lep1_C']
WZZ2_lep1_C = WZZ2_Ntuples['lep1_C']

ZZZ1_lep1_C = ZZZ1_Ntuples['lep1_C']
ZZZ2_lep1_C = ZZZ2_Ntuples['lep1_C']

ttbarG1_lep1_C = ttbarG1_Ntuples['lep1_C']
ttbarG2_lep1_C = ttbarG2_Ntuples['lep1_C']

# lep2
WZG1_lep2 = WZG1_Ntuples['lep2'].flatten()
WZG2_lep2 = WZG2_Ntuples['lep2'].flatten()

#WG1_lep2 = WG1_Ntuples['lep2'].flatten()
WG1_lep2 = WG1_Ntuples['lep2'].flatten()

ZG1_lep2 = ZG1_Ntuples['lep2'].flatten()
ZG2_lep2 = ZG2_Ntuples['lep2'].flatten()

WW1_lep2 = WW1_Ntuples['lep2'].flatten()
WW2_lep2 = WW2_Ntuples['lep2'].flatten()

WZ1_lep2 = WZ1_Ntuples['lep2'].flatten()
WZ2_lep2 = WZ2_Ntuples['lep2'].flatten()

ZZ1_lep2 = ZZ1_Ntuples['lep2'].flatten()
ZZ2_lep2 = ZZ2_Ntuples['lep2'].flatten()

WWW1_lep2 = WWW1_Ntuples['lep2'].flatten()
WWW2_lep2 = WWW2_Ntuples['lep2'].flatten()

WWZ1_lep2 = WWZ1_Ntuples['lep2'].flatten()
WWZ2_lep2 = WWZ2_Ntuples['lep2'].flatten()

WZZ1_lep2 = WZZ1_Ntuples['lep2'].flatten()
WZZ2_lep2 = WZZ2_Ntuples['lep2'].flatten()

ZZZ1_lep2 = ZZZ1_Ntuples['lep2'].flatten()
ZZZ2_lep2 = ZZZ2_Ntuples['lep2'].flatten()

ttbarG1_lep2 = ttbarG1_Ntuples['lep2'].flatten()
ttbarG2_lep2 = ttbarG2_Ntuples['lep2'].flatten()

# lep2 flavor
WZG1_lep2_Flav = WZG1_Ntuples['lep2_Flav'].flatten()
WZG2_lep2_Flav = WZG2_Ntuples['lep2_Flav'].flatten()

#WG1_lep2_Flav = WG1_Ntuples['lep2_Flav'].flatten()
WG1_lep2_Flav = WG1_Ntuples['lep2_Flav'].flatten()

ZG1_lep2_Flav = ZG1_Ntuples['lep2_Flav'].flatten()
ZG2_lep2_Flav = ZG2_Ntuples['lep2_Flav'].flatten()

WW1_lep2_Flav = WW1_Ntuples['lep2_Flav'].flatten()
WW2_lep2_Flav = WW2_Ntuples['lep2_Flav'].flatten()

WZ1_lep2_Flav = WZ1_Ntuples['lep2_Flav'].flatten()
WZ2_lep2_Flav = WZ2_Ntuples['lep2_Flav'].flatten()

ZZ1_lep2_Flav = ZZ1_Ntuples['lep2_Flav'].flatten()
ZZ2_lep2_Flav = ZZ2_Ntuples['lep2_Flav'].flatten()

WWW1_lep2_Flav = WWW1_Ntuples['lep2_Flav'].flatten()
WWW2_lep2_Flav = WWW2_Ntuples['lep2_Flav'].flatten()

WWZ1_lep2_Flav = WWZ1_Ntuples['lep2_Flav'].flatten()
WWZ2_lep2_Flav = WWZ2_Ntuples['lep2_Flav'].flatten()

WZZ1_lep2_Flav = WZZ1_Ntuples['lep2_Flav'].flatten()
WZZ2_lep2_Flav = WZZ2_Ntuples['lep2_Flav'].flatten()

ZZZ1_lep2_Flav = ZZZ1_Ntuples['lep2_Flav'].flatten()
ZZZ2_lep2_Flav = ZZZ2_Ntuples['lep2_Flav'].flatten()

ttbarG1_lep2_Flav = ttbarG1_Ntuples['lep2_Flav'].flatten()
ttbarG2_lep2_Flav = ttbarG2_Ntuples['lep2_Flav'].flatten()

#lep2 Charge
WZG1_lep2_C = WZG1_Ntuples['lep2_C']
WZG2_lep2_C = WZG2_Ntuples['lep2_C']

#WG1_lep2_C = WG1_Ntuples['lep2_C']
WG1_lep2_C = WG1_Ntuples['lep2_C']

ZG1_lep2_C = ZG1_Ntuples['lep2_C']
ZG2_lep2_C = ZG2_Ntuples['lep2_C']

WW1_lep2_C = WW1_Ntuples['lep2_C']
WW2_lep2_C = WW2_Ntuples['lep2_C']

WZ1_lep2_C = WZ1_Ntuples['lep2_C']
WZ2_lep2_C = WZ2_Ntuples['lep2_C']

ZZ1_lep2_C = ZZ1_Ntuples['lep2_C']
ZZ2_lep2_C = ZZ2_Ntuples['lep2_C']

WWW1_lep2_C = WWW1_Ntuples['lep2_C']
WWW2_lep2_C = WWW2_Ntuples['lep2_C']

WWZ1_lep2_C = WWZ1_Ntuples['lep2_C']
WWZ2_lep2_C = WWZ2_Ntuples['lep2_C']

WZZ1_lep2_C = WZZ1_Ntuples['lep2_C']
WZZ2_lep2_C = WZZ2_Ntuples['lep2_C']

ZZZ1_lep2_C = ZZZ1_Ntuples['lep2_C']
ZZZ2_lep2_C = ZZZ2_Ntuples['lep2_C']

ttbarG1_lep2_C = ttbarG1_Ntuples['lep2_C']
ttbarG2_lep2_C = ttbarG2_Ntuples['lep2_C']

# lep3
WZG1_lep3 = WZG1_Ntuples['lep3'].flatten()
WZG2_lep3 = WZG2_Ntuples['lep3'].flatten()

#WG1_lep3 = WG1_Ntuples['lep3'].flatten()
WG1_lep3 = WG1_Ntuples['lep3'].flatten()

ZG1_lep3 = ZG1_Ntuples['lep3'].flatten()
ZG2_lep3 = ZG2_Ntuples['lep3'].flatten()

WW1_lep3 = WW1_Ntuples['lep3'].flatten()
WW2_lep3 = WW2_Ntuples['lep3'].flatten()

WZ1_lep3 = WZ1_Ntuples['lep3'].flatten()
WZ2_lep3 = WZ2_Ntuples['lep3'].flatten()

ZZ1_lep3 = ZZ1_Ntuples['lep3'].flatten()
ZZ2_lep3 = ZZ2_Ntuples['lep3'].flatten()

WWW1_lep3 = WWW1_Ntuples['lep3'].flatten()
WWW2_lep3 = WWW2_Ntuples['lep3'].flatten()

WWZ1_lep3 = WWZ1_Ntuples['lep3'].flatten()
WWZ2_lep3 = WWZ2_Ntuples['lep3'].flatten()

WZZ1_lep3 = WZZ1_Ntuples['lep3'].flatten()
WZZ2_lep3 = WZZ2_Ntuples['lep3'].flatten()

ZZZ1_lep3 = ZZZ1_Ntuples['lep3'].flatten()
ZZZ2_lep3 = ZZZ2_Ntuples['lep3'].flatten()

ttbarG1_lep3 = ttbarG1_Ntuples['lep3'].flatten()
ttbarG2_lep3 = ttbarG2_Ntuples['lep3'].flatten()

# lep3 flavor
WZG1_lep3_Flav = WZG1_Ntuples['lep3_Flav'].flatten()
WZG2_lep3_Flav = WZG2_Ntuples['lep3_Flav'].flatten()

#WG1_lep3_Flav = WG1_Ntuples['lep3_Flav'].flatten()
WG1_lep3_Flav = WG1_Ntuples['lep3_Flav'].flatten()

ZG1_lep3_Flav = ZG1_Ntuples['lep3_Flav'].flatten()
ZG2_lep3_Flav = ZG2_Ntuples['lep3_Flav'].flatten()

WW1_lep3_Flav = WW1_Ntuples['lep3_Flav'].flatten()
WW2_lep3_Flav = WW2_Ntuples['lep3_Flav'].flatten()

WZ1_lep3_Flav = WZ1_Ntuples['lep3_Flav'].flatten()
WZ2_lep3_Flav = WZ2_Ntuples['lep3_Flav'].flatten()

ZZ1_lep3_Flav = ZZ1_Ntuples['lep3_Flav'].flatten()
ZZ2_lep3_Flav = ZZ2_Ntuples['lep3_Flav'].flatten()

WWW1_lep3_Flav = WWW1_Ntuples['lep3_Flav'].flatten()
WWW2_lep3_Flav = WWW2_Ntuples['lep3_Flav'].flatten()

WWZ1_lep3_Flav = WWZ1_Ntuples['lep3_Flav'].flatten()
WWZ2_lep3_Flav = WWZ2_Ntuples['lep3_Flav'].flatten()

WZZ1_lep3_Flav = WZZ1_Ntuples['lep3_Flav'].flatten()
WZZ2_lep3_Flav = WZZ2_Ntuples['lep3_Flav'].flatten()

ZZZ1_lep3_Flav = ZZZ1_Ntuples['lep3_Flav'].flatten()
ZZZ2_lep3_Flav = ZZZ2_Ntuples['lep3_Flav'].flatten()

ttbarG1_lep3_Flav = ttbarG1_Ntuples['lep3_Flav'].flatten()
ttbarG2_lep3_Flav = ttbarG2_Ntuples['lep3_Flav'].flatten()

# lep3 Charge
WZG1_lep3_C = WZG1_Ntuples['lep3_C']
WZG2_lep3_C = WZG2_Ntuples['lep3_C']

#WG1_lep3_C = WG1_Ntuples['lep3_C']
WG1_lep3_C = WG1_Ntuples['lep3_C']

ZG1_lep3_C = ZG1_Ntuples['lep3_C']
ZG2_lep3_C = ZG2_Ntuples['lep3_C']

WW1_lep3_C = WW1_Ntuples['lep3_C']
WW2_lep3_C = WW2_Ntuples['lep3_C']

WZ1_lep3_C = WZ1_Ntuples['lep3_C']
WZ2_lep3_C = WZ2_Ntuples['lep3_C']

ZZ1_lep3_C = ZZ1_Ntuples['lep3_C']
ZZ2_lep3_C = ZZ2_Ntuples['lep3_C']

WWW1_lep3_C = WWW1_Ntuples['lep3_C']
WWW2_lep3_C = WWW2_Ntuples['lep3_C']

WWZ1_lep3_C = WWZ1_Ntuples['lep3_C']
WWZ2_lep3_C = WWZ2_Ntuples['lep3_C']

WZZ1_lep3_C = WZZ1_Ntuples['lep3_C']
WZZ2_lep3_C = WZZ2_Ntuples['lep3_C']

ZZZ1_lep3_C = ZZZ1_Ntuples['lep3_C']
ZZZ2_lep3_C = ZZZ2_Ntuples['lep3_C']

ttbarG1_lep3_C = ttbarG1_Ntuples['lep3_C']
ttbarG2_lep3_C = ttbarG2_Ntuples['lep3_C']

# MET
WZG1_MET = WZG1_Ntuples['MET'].flatten()
WZG2_MET = WZG2_Ntuples['MET'].flatten()

#WG1_MET = WG1_Ntuples['MET'].flatten()
WG1_MET = WG1_Ntuples['MET'].flatten()

ZG1_MET = ZG1_Ntuples['MET'].flatten()
ZG2_MET = ZG2_Ntuples['MET'].flatten()

WW1_MET = WW1_Ntuples['MET'].flatten()
WW2_MET = WW2_Ntuples['MET'].flatten()

WZ1_MET = WZ1_Ntuples['MET'].flatten()
WZ2_MET = WZ2_Ntuples['MET'].flatten()

ZZ1_MET = ZZ1_Ntuples['MET'].flatten()
ZZ2_MET = ZZ2_Ntuples['MET'].flatten()

WWW1_MET = WWW1_Ntuples['MET'].flatten()
WWW2_MET = WWW2_Ntuples['MET'].flatten()

WWZ1_MET = WWZ1_Ntuples['MET'].flatten()
WWZ2_MET = WWZ2_Ntuples['MET'].flatten()

WZZ1_MET = WZZ1_Ntuples['MET'].flatten()
WZZ2_MET = WZZ2_Ntuples['MET'].flatten()

ZZZ1_MET = ZZZ1_Ntuples['MET'].flatten()
ZZZ2_MET = ZZZ2_Ntuples['MET'].flatten()

ttbarG1_MET = ttbarG1_Ntuples['MET'].flatten()
ttbarG2_MET = ttbarG2_Ntuples['MET'].flatten()

# Pho
WZG1_Pho = WZG1_Ntuples['Pho'].flatten()
WZG2_Pho = WZG2_Ntuples['Pho'].flatten()

#WG1_Pho = WG1_Ntuples['Pho'].flatten()
WG1_Pho = WG1_Ntuples['Pho'].flatten()

ZG1_Pho = ZG1_Ntuples['Pho'].flatten()
ZG2_Pho = ZG2_Ntuples['Pho'].flatten()

WW1_Pho = WW1_Ntuples['Pho'].flatten()
WW2_Pho = WW2_Ntuples['Pho'].flatten()

WZ1_Pho = WZ1_Ntuples['Pho'].flatten()
WZ2_Pho = WZ2_Ntuples['Pho'].flatten()

ZZ1_Pho = ZZ1_Ntuples['Pho'].flatten()
ZZ2_Pho = ZZ2_Ntuples['Pho'].flatten()

WWW1_Pho = WWW1_Ntuples['Pho'].flatten()
WWW2_Pho = WWW2_Ntuples['Pho'].flatten()

WWZ1_Pho = WWZ1_Ntuples['Pho'].flatten()
WWZ2_Pho = WWZ2_Ntuples['Pho'].flatten()

WZZ1_Pho = WZZ1_Ntuples['Pho'].flatten()
WZZ2_Pho = WZZ2_Ntuples['Pho'].flatten()

ZZZ1_Pho = ZZZ1_Ntuples['Pho'].flatten()
ZZZ2_Pho = ZZZ2_Ntuples['Pho'].flatten()

ttbarG1_Pho = ttbarG1_Ntuples['Pho'].flatten()
ttbarG2_Pho = ttbarG2_Ntuples['Pho'].flatten()

# MT
WZG1_MT = WZG1_Ntuples['MT'].flatten()
WZG2_MT = WZG2_Ntuples['MT'].flatten()

#WG1_MT = WG1_Ntuples['MT'].flatten()
WG1_MT = WG1_Ntuples['MT'].flatten()

ZG1_MT = ZG1_Ntuples['MT'].flatten()
ZG2_MT = ZG2_Ntuples['MT'].flatten()

WW1_MT = WW1_Ntuples['MT'].flatten()
WW2_MT = WW2_Ntuples['MT'].flatten()

WZ1_MT = WZ1_Ntuples['MT'].flatten()
WZ2_MT = WZ2_Ntuples['MT'].flatten()

ZZ1_MT = ZZ1_Ntuples['MT'].flatten()
ZZ2_MT = ZZ2_Ntuples['MT'].flatten()

WWW1_MT = WWW1_Ntuples['MT'].flatten()
WWW2_MT = WWW2_Ntuples['MT'].flatten()

WWZ1_MT = WWZ1_Ntuples['MT'].flatten()
WWZ2_MT = WWZ2_Ntuples['MT'].flatten()

WZZ1_MT = WZZ1_Ntuples['MT'].flatten()
WZZ2_MT = WZZ2_Ntuples['MT'].flatten()

ZZZ1_MT = ZZZ1_Ntuples['MT'].flatten()
ZZZ2_MT = ZZZ2_Ntuples['MT'].flatten()

ttbarG1_MT = ttbarG1_Ntuples['MT'].flatten()
ttbarG2_MT = ttbarG2_Ntuples['MT'].flatten()

# Dilepptsum
WZG1_Dilepptsum = WZG1_Ntuples['Dilepptsum'].flatten()
WZG2_Dilepptsum = WZG2_Ntuples['Dilepptsum'].flatten()

#WG1_Dilepptsum = WG1_Ntuples['Dilepptsum'].flatten()
WG1_Dilepptsum = WG1_Ntuples['Dilepptsum'].flatten()

ZG1_Dilepptsum = ZG1_Ntuples['Dilepptsum'].flatten()
ZG2_Dilepptsum = ZG2_Ntuples['Dilepptsum'].flatten()

WW1_Dilepptsum = WW1_Ntuples['Dilepptsum'].flatten()
WW2_Dilepptsum = WW2_Ntuples['Dilepptsum'].flatten()

WZ1_Dilepptsum = WZ1_Ntuples['Dilepptsum'].flatten()
WZ2_Dilepptsum = WZ2_Ntuples['Dilepptsum'].flatten()

ZZ1_Dilepptsum = ZZ1_Ntuples['Dilepptsum'].flatten()
ZZ2_Dilepptsum = ZZ2_Ntuples['Dilepptsum'].flatten()

WWW1_Dilepptsum = WWW1_Ntuples['Dilepptsum'].flatten()
WWW2_Dilepptsum = WWW2_Ntuples['Dilepptsum'].flatten()

WWZ1_Dilepptsum = WWZ1_Ntuples['Dilepptsum'].flatten()
WWZ2_Dilepptsum = WWZ2_Ntuples['Dilepptsum'].flatten()

WZZ1_Dilepptsum = WZZ1_Ntuples['Dilepptsum'].flatten()
WZZ2_Dilepptsum = WZZ2_Ntuples['Dilepptsum'].flatten()

ZZZ1_Dilepptsum = ZZZ1_Ntuples['Dilepptsum'].flatten()
ZZZ2_Dilepptsum = ZZZ2_Ntuples['Dilepptsum'].flatten()

ttbarG1_Dilepptsum = ttbarG1_Ntuples['Dilepptsum'].flatten()
ttbarG2_Dilepptsum = ttbarG2_Ntuples['Dilepptsum'].flatten()

# Trilepptsum
WZG1_Trilepptsum = WZG1_Ntuples['Trilepptsum'].flatten()
WZG2_Trilepptsum = WZG2_Ntuples['Trilepptsum'].flatten()

#WG1_Trilepptsum = WG1_Ntuples['Trilepptsum'].flatten()
WG1_Trilepptsum = WG1_Ntuples['Trilepptsum'].flatten()

ZG1_Trilepptsum = ZG1_Ntuples['Trilepptsum'].flatten()
ZG2_Trilepptsum = ZG2_Ntuples['Trilepptsum'].flatten()

WW1_Trilepptsum = WW1_Ntuples['Trilepptsum'].flatten()
WW2_Trilepptsum = WW2_Ntuples['Trilepptsum'].flatten()

WZ1_Trilepptsum = WZ1_Ntuples['Trilepptsum'].flatten()
WZ2_Trilepptsum = WZ2_Ntuples['Trilepptsum'].flatten()

ZZ1_Trilepptsum = ZZ1_Ntuples['Trilepptsum'].flatten()
ZZ2_Trilepptsum = ZZ2_Ntuples['Trilepptsum'].flatten()

WWW1_Trilepptsum = WWW1_Ntuples['Trilepptsum'].flatten()
WWW2_Trilepptsum = WWW2_Ntuples['Trilepptsum'].flatten()

WWZ1_Trilepptsum = WWZ1_Ntuples['Trilepptsum'].flatten()
WWZ2_Trilepptsum = WWZ2_Ntuples['Trilepptsum'].flatten()

WZZ1_Trilepptsum = WZZ1_Ntuples['Trilepptsum'].flatten()
WZZ2_Trilepptsum = WZZ2_Ntuples['Trilepptsum'].flatten()

ZZZ1_Trilepptsum = ZZZ1_Ntuples['Trilepptsum'].flatten()
ZZZ2_Trilepptsum = ZZZ2_Ntuples['Trilepptsum'].flatten()

ttbarG1_Trilepptsum = ttbarG1_Ntuples['Trilepptsum'].flatten()
ttbarG2_Trilepptsum = ttbarG2_Ntuples['Trilepptsum'].flatten()

# Trilepphoptsum
WZG1_Trilepphoptsum = WZG1_Ntuples['Trilepphoptsum'].flatten()
WZG2_Trilepphoptsum = WZG2_Ntuples['Trilepphoptsum'].flatten()

#WG1_Trilepphoptsum = WG1_Ntuples['Trilepphoptsum'].flatten()
WG1_Trilepphoptsum = WG1_Ntuples['Trilepphoptsum'].flatten()

ZG1_Trilepphoptsum = ZG1_Ntuples['Trilepphoptsum'].flatten()
ZG2_Trilepphoptsum = ZG2_Ntuples['Trilepphoptsum'].flatten()

WW1_Trilepphoptsum = WW1_Ntuples['Trilepphoptsum'].flatten()
WW2_Trilepphoptsum = WW2_Ntuples['Trilepphoptsum'].flatten()

WZ1_Trilepphoptsum = WZ1_Ntuples['Trilepphoptsum'].flatten()
WZ2_Trilepphoptsum = WZ2_Ntuples['Trilepphoptsum'].flatten()

ZZ1_Trilepphoptsum = ZZ1_Ntuples['Trilepphoptsum'].flatten()
ZZ2_Trilepphoptsum = ZZ2_Ntuples['Trilepphoptsum'].flatten()

WWW1_Trilepphoptsum = WWW1_Ntuples['Trilepphoptsum'].flatten()
WWW2_Trilepphoptsum = WWW2_Ntuples['Trilepphoptsum'].flatten()

WWZ1_Trilepphoptsum = WWZ1_Ntuples['Trilepphoptsum'].flatten()
WWZ2_Trilepphoptsum = WWZ2_Ntuples['Trilepphoptsum'].flatten()

WZZ1_Trilepphoptsum = WZZ1_Ntuples['Trilepphoptsum'].flatten()
WZZ2_Trilepphoptsum = WZZ2_Ntuples['Trilepphoptsum'].flatten()

ZZZ1_Trilepphoptsum = ZZZ1_Ntuples['Trilepphoptsum'].flatten()
ZZZ2_Trilepphoptsum = ZZZ2_Ntuples['Trilepphoptsum'].flatten()

ttbarG1_Trilepphoptsum = ttbarG1_Ntuples['Trilepphoptsum'].flatten()
ttbarG2_Trilepphoptsum = ttbarG2_Ntuples['Trilepphoptsum'].flatten()

# Sum array
WZG_Dilep_pt = np.concatenate((WZG1_Dilep.pt, WZG2_Dilep.pt), axis=0)
WG_Dilep_pt = WG1_Dilep.pt
ZG_Dilep_pt = np.concatenate((ZG1_Dilep.pt, ZG2_Dilep.pt), axis=0)
WW_Dilep_pt = np.concatenate((WW1_Dilep.pt, WW2_Dilep.pt), axis=0)
WZ_Dilep_pt = np.concatenate((WZ1_Dilep.pt, WZ2_Dilep.pt), axis=0)
ZZ_Dilep_pt = np.concatenate((ZZ1_Dilep.pt, ZZ2_Dilep.pt), axis=0)
WWW_Dilep_pt = np.concatenate((WWW1_Dilep.pt, WWW2_Dilep.pt), axis=0)
WWZ_Dilep_pt = np.concatenate((WWZ1_Dilep.pt, WWZ2_Dilep.pt), axis=0)
WZZ_Dilep_pt = np.concatenate((WZZ1_Dilep.pt, WZZ2_Dilep.pt), axis=0)
ZZZ_Dilep_pt = np.concatenate((ZZZ1_Dilep.pt, ZZZ2_Dilep.pt), axis=0)
ttbarG_Dilep_pt = np.concatenate((ttbarG1_Dilep.pt, ttbarG2_Dilep.pt), axis=0)

WZG_Dilep_mass = np.concatenate((WZG1_Dilep.mass, WZG2_Dilep.mass), axis=0)
WG_Dilep_mass = WG1_Dilep.mass
ZG_Dilep_mass = np.concatenate((ZG1_Dilep.mass, ZG2_Dilep.mass), axis=0)
WW_Dilep_mass = np.concatenate((WW1_Dilep.mass, WW2_Dilep.mass), axis=0)
WZ_Dilep_mass = np.concatenate((WZ1_Dilep.mass, WZ2_Dilep.mass), axis=0)
ZZ_Dilep_mass = np.concatenate((ZZ1_Dilep.mass, ZZ2_Dilep.mass), axis=0)
WWW_Dilep_mass = np.concatenate((WWW1_Dilep.mass, WWW2_Dilep.mass), axis=0)
WWZ_Dilep_mass = np.concatenate((WWZ1_Dilep.mass, WWZ2_Dilep.mass), axis=0)
WZZ_Dilep_mass = np.concatenate((WZZ1_Dilep.mass, WZZ2_Dilep.mass), axis=0)
ZZZ_Dilep_mass = np.concatenate((ZZZ1_Dilep.mass, ZZZ2_Dilep.mass), axis=0)
ttbarG_Dilep_mass = np.concatenate((ttbarG1_Dilep.mass, ttbarG2_Dilep.mass), axis=0)

WZG_Dilep_E = np.concatenate((WZG1_Dilep.E, WZG2_Dilep.E), axis=0)
WG_Dilep_E = WG1_Dilep.E
ZG_Dilep_E = np.concatenate((ZG1_Dilep.E, ZG2_Dilep.E), axis=0)
WW_Dilep_E = np.concatenate((WW1_Dilep.E, WW2_Dilep.E), axis=0)
WZ_Dilep_E = np.concatenate((WZ1_Dilep.E, WZ2_Dilep.E), axis=0)
ZZ_Dilep_E = np.concatenate((ZZ1_Dilep.E, ZZ2_Dilep.E), axis=0)
WWW_Dilep_E = np.concatenate((WWW1_Dilep.E, WWW2_Dilep.E), axis=0)
WWZ_Dilep_E = np.concatenate((WWZ1_Dilep.E, WWZ2_Dilep.E), axis=0)
WZZ_Dilep_E = np.concatenate((WZZ1_Dilep.E, WZZ2_Dilep.E), axis=0)
ZZZ_Dilep_E = np.concatenate((ZZZ1_Dilep.E, ZZZ2_Dilep.E), axis=0)
ttbarG_Dilep_E = np.concatenate((ttbarG1_Dilep.E, ttbarG2_Dilep.E), axis=0)

WZG_Trilep_pt = np.concatenate((WZG1_Trilep.pt, WZG2_Trilep.pt), axis=0)
WG_Trilep_pt = WG1_Trilep.pt
ZG_Trilep_pt = np.concatenate((ZG1_Trilep.pt, ZG2_Trilep.pt), axis=0)
WW_Trilep_pt = np.concatenate((WW1_Trilep.pt, WW2_Trilep.pt), axis=0)
WZ_Trilep_pt = np.concatenate((WZ1_Trilep.pt, WZ2_Trilep.pt), axis=0)
ZZ_Trilep_pt = np.concatenate((ZZ1_Trilep.pt, ZZ2_Trilep.pt), axis=0)
WWW_Trilep_pt = np.concatenate((WWW1_Trilep.pt, WWW2_Trilep.pt), axis=0)
WWZ_Trilep_pt = np.concatenate((WWZ1_Trilep.pt, WWZ2_Trilep.pt), axis=0)
WZZ_Trilep_pt = np.concatenate((WZZ1_Trilep.pt, WZZ2_Trilep.pt), axis=0)
ZZZ_Trilep_pt = np.concatenate((ZZZ1_Trilep.pt, ZZZ2_Trilep.pt), axis=0)
ttbarG_Trilep_pt = np.concatenate((ttbarG1_Trilep.pt, ttbarG2_Trilep.pt), axis=0)

WZG_Trilep_mass = np.concatenate((WZG1_Trilep.mass, WZG2_Trilep.mass), axis=0)
WG_Trilep_mass = WG1_Trilep.mass
ZG_Trilep_mass = np.concatenate((ZG1_Trilep.mass, ZG2_Trilep.mass), axis=0)
WW_Trilep_mass = np.concatenate((WW1_Trilep.mass, WW2_Trilep.mass), axis=0)
WZ_Trilep_mass = np.concatenate((WZ1_Trilep.mass, WZ2_Trilep.mass), axis=0)
ZZ_Trilep_mass = np.concatenate((ZZ1_Trilep.mass, ZZ2_Trilep.mass), axis=0)
WWW_Trilep_mass = np.concatenate((WWW1_Trilep.mass, WWW2_Trilep.mass), axis=0)
WWZ_Trilep_mass = np.concatenate((WWZ1_Trilep.mass, WWZ2_Trilep.mass), axis=0)
WZZ_Trilep_mass = np.concatenate((WZZ1_Trilep.mass, WZZ2_Trilep.mass), axis=0)
ZZZ_Trilep_mass = np.concatenate((ZZZ1_Trilep.mass, ZZZ2_Trilep.mass), axis=0)
ttbarG_Trilep_mass = np.concatenate((ttbarG1_Trilep.mass, ttbarG2_Trilep.mass), axis=0)

WZG_Trilep_E = np.concatenate((WZG1_Trilep.E, WZG2_Trilep.E), axis=0)
WG_Trilep_E = WG1_Trilep.E
ZG_Trilep_E = np.concatenate((ZG1_Trilep.E, ZG2_Trilep.E), axis=0)
WW_Trilep_E = np.concatenate((WW1_Trilep.E, WW2_Trilep.E), axis=0)
WZ_Trilep_E = np.concatenate((WZ1_Trilep.E, WZ2_Trilep.E), axis=0)
ZZ_Trilep_E = np.concatenate((ZZ1_Trilep.E, ZZ2_Trilep.E), axis=0)
WWW_Trilep_E = np.concatenate((WWW1_Trilep.E, WWW2_Trilep.E), axis=0)
WWZ_Trilep_E = np.concatenate((WWZ1_Trilep.E, WWZ2_Trilep.E), axis=0)
WZZ_Trilep_E = np.concatenate((WZZ1_Trilep.E, WZZ2_Trilep.E), axis=0)
ZZZ_Trilep_E = np.concatenate((ZZZ1_Trilep.E, ZZZ2_Trilep.E), axis=0)
ttbarG_Trilep_E = np.concatenate((ttbarG1_Trilep.E, ttbarG2_Trilep.E), axis=0)

WZG_Trileppho_pt = np.concatenate((WZG1_Trileppho.pt, WZG2_Trileppho.pt), axis=0)
WG_Trileppho_pt = WG1_Trileppho.pt
ZG_Trileppho_pt = np.concatenate((ZG1_Trileppho.pt, ZG2_Trileppho.pt), axis=0)
WW_Trileppho_pt = np.concatenate((WW1_Trileppho.pt, WW2_Trileppho.pt), axis=0)
WZ_Trileppho_pt = np.concatenate((WZ1_Trileppho.pt, WZ2_Trileppho.pt), axis=0)
ZZ_Trileppho_pt = np.concatenate((ZZ1_Trileppho.pt, ZZ2_Trileppho.pt), axis=0)
WWW_Trileppho_pt = np.concatenate((WWW1_Trileppho.pt, WWW2_Trileppho.pt), axis=0)
WWZ_Trileppho_pt = np.concatenate((WWZ1_Trileppho.pt, WWZ2_Trileppho.pt), axis=0)
WZZ_Trileppho_pt = np.concatenate((WZZ1_Trileppho.pt, WZZ2_Trileppho.pt), axis=0)
ZZZ_Trileppho_pt = np.concatenate((ZZZ1_Trileppho.pt, ZZZ2_Trileppho.pt), axis=0)
ttbarG_Trileppho_pt = np.concatenate((ttbarG1_Trileppho.pt, ttbarG2_Trileppho.pt), axis=0)

WZG_Trileppho_mass = np.concatenate((WZG1_Trileppho.mass, WZG2_Trileppho.mass), axis=0)
WG_Trileppho_mass = WG1_Trileppho.mass
ZG_Trileppho_mass = np.concatenate((ZG1_Trileppho.mass, ZG2_Trileppho.mass), axis=0)
WW_Trileppho_mass = np.concatenate((WW1_Trileppho.mass, WW2_Trileppho.mass), axis=0)
WZ_Trileppho_mass = np.concatenate((WZ1_Trileppho.mass, WZ2_Trileppho.mass), axis=0)
ZZ_Trileppho_mass = np.concatenate((ZZ1_Trileppho.mass, ZZ2_Trileppho.mass), axis=0)
WWW_Trileppho_mass = np.concatenate((WWW1_Trileppho.mass, WWW2_Trileppho.mass), axis=0)
WWZ_Trileppho_mass = np.concatenate((WWZ1_Trileppho.mass, WWZ2_Trileppho.mass), axis=0)
WZZ_Trileppho_mass = np.concatenate((WZZ1_Trileppho.mass, WZZ2_Trileppho.mass), axis=0)
ZZZ_Trileppho_mass = np.concatenate((ZZZ1_Trileppho.mass, ZZZ2_Trileppho.mass), axis=0)
ttbarG_Trileppho_mass = np.concatenate((ttbarG1_Trileppho.mass, ttbarG2_Trileppho.mass), axis=0)

WZG_Trileppho_E = np.concatenate((WZG1_Trileppho.E, WZG2_Trileppho.E), axis=0)
WG_Trileppho_E = WG1_Trileppho.E
ZG_Trileppho_E = np.concatenate((ZG1_Trileppho.E, ZG2_Trileppho.E), axis=0)
WW_Trileppho_E = np.concatenate((WW1_Trileppho.E, WW2_Trileppho.E), axis=0)
WZ_Trileppho_E = np.concatenate((WZ1_Trileppho.E, WZ2_Trileppho.E), axis=0)
ZZ_Trileppho_E = np.concatenate((ZZ1_Trileppho.E, ZZ2_Trileppho.E), axis=0)
WWW_Trileppho_E = np.concatenate((WWW1_Trileppho.E, WWW2_Trileppho.E), axis=0)
WWZ_Trileppho_E = np.concatenate((WWZ1_Trileppho.E, WWZ2_Trileppho.E), axis=0)
WZZ_Trileppho_E = np.concatenate((WZZ1_Trileppho.E, WZZ2_Trileppho.E), axis=0)
ZZZ_Trileppho_E = np.concatenate((ZZZ1_Trileppho.E, ZZZ2_Trileppho.E), axis=0)
ttbarG_Trileppho_E = np.concatenate((ttbarG1_Trileppho.E, ttbarG2_Trileppho.E), axis=0)

WZG_lep1_pt = np.concatenate((WZG1_lep1.pt, WZG2_lep1.pt), axis=0)
WG_lep1_pt = WG1_lep1.pt
ZG_lep1_pt = np.concatenate((ZG1_lep1.pt, ZG2_lep1.pt), axis=0)
WW_lep1_pt = np.concatenate((WW1_lep1.pt, WW2_lep1.pt), axis=0)
WZ_lep1_pt = np.concatenate((WZ1_lep1.pt, WZ2_lep1.pt), axis=0)
ZZ_lep1_pt = np.concatenate((ZZ1_lep1.pt, ZZ2_lep1.pt), axis=0)
WWW_lep1_pt = np.concatenate((WWW1_lep1.pt, WWW2_lep1.pt), axis=0)
WWZ_lep1_pt = np.concatenate((WWZ1_lep1.pt, WWZ2_lep1.pt), axis=0)
WZZ_lep1_pt = np.concatenate((WZZ1_lep1.pt, WZZ2_lep1.pt), axis=0)
ZZZ_lep1_pt = np.concatenate((ZZZ1_lep1.pt, ZZZ2_lep1.pt), axis=0)
ttbarG_lep1_pt = np.concatenate((ttbarG1_lep1.pt, ttbarG2_lep1.pt), axis=0)

WZG_lep1_eta = np.concatenate((WZG1_lep1.eta, WZG2_lep1.eta), axis=0)
WG_lep1_eta = WG1_lep1.eta
ZG_lep1_eta = np.concatenate((ZG1_lep1.eta, ZG2_lep1.eta), axis=0)
WW_lep1_eta = np.concatenate((WW1_lep1.eta, WW2_lep1.eta), axis=0)
WZ_lep1_eta = np.concatenate((WZ1_lep1.eta, WZ2_lep1.eta), axis=0)
ZZ_lep1_eta = np.concatenate((ZZ1_lep1.eta, ZZ2_lep1.eta), axis=0)
WWW_lep1_eta = np.concatenate((WWW1_lep1.eta, WWW2_lep1.eta), axis=0)
WWZ_lep1_eta = np.concatenate((WWZ1_lep1.eta, WWZ2_lep1.eta), axis=0)
WZZ_lep1_eta = np.concatenate((WZZ1_lep1.eta, WZZ2_lep1.eta), axis=0)
ZZZ_lep1_eta = np.concatenate((ZZZ1_lep1.eta, ZZZ2_lep1.eta), axis=0)
ttbarG_lep1_eta = np.concatenate((ttbarG1_lep1.eta, ttbarG2_lep1.eta), axis=0)

WZG_lep1_phi = np.concatenate((WZG1_lep1.phi, WZG2_lep1.phi), axis=0)
WG_lep1_phi = WG1_lep1.phi
ZG_lep1_phi = np.concatenate((ZG1_lep1.phi, ZG2_lep1.phi), axis=0)
WW_lep1_phi = np.concatenate((WW1_lep1.phi, WW2_lep1.phi), axis=0)
WZ_lep1_phi = np.concatenate((WZ1_lep1.phi, WZ2_lep1.phi), axis=0)
ZZ_lep1_phi = np.concatenate((ZZ1_lep1.phi, ZZ2_lep1.phi), axis=0)
WWW_lep1_phi = np.concatenate((WWW1_lep1.phi, WWW2_lep1.phi), axis=0)
WWZ_lep1_phi = np.concatenate((WWZ1_lep1.phi, WWZ2_lep1.phi), axis=0)
WZZ_lep1_phi = np.concatenate((WZZ1_lep1.phi, WZZ2_lep1.phi), axis=0)
ZZZ_lep1_phi = np.concatenate((ZZZ1_lep1.phi, ZZZ2_lep1.phi), axis=0)
ttbarG_lep1_phi = np.concatenate((ttbarG1_lep1.phi, ttbarG2_lep1.phi), axis=0)

WZG_lep1_mass = np.concatenate((WZG1_lep1.mass, WZG2_lep1.mass), axis=0)
WG_lep1_mass = WG1_lep1.mass
ZG_lep1_mass = np.concatenate((ZG1_lep1.mass, ZG2_lep1.mass), axis=0)
WW_lep1_mass = np.concatenate((WW1_lep1.mass, WW2_lep1.mass), axis=0)
WZ_lep1_mass = np.concatenate((WZ1_lep1.mass, WZ2_lep1.mass), axis=0)
ZZ_lep1_mass = np.concatenate((ZZ1_lep1.mass, ZZ2_lep1.mass), axis=0)
WWW_lep1_mass = np.concatenate((WWW1_lep1.mass, WWW2_lep1.mass), axis=0)
WWZ_lep1_mass = np.concatenate((WWZ1_lep1.mass, WWZ2_lep1.mass), axis=0)
WZZ_lep1_mass = np.concatenate((WZZ1_lep1.mass, WZZ2_lep1.mass), axis=0)
ZZZ_lep1_mass = np.concatenate((ZZZ1_lep1.mass, ZZZ2_lep1.mass), axis=0)
ttbarG_lep1_mass = np.concatenate((ttbarG1_lep1.mass, ttbarG2_lep1.mass), axis=0)

WZG_lep1_E = np.concatenate((WZG1_lep1.E, WZG2_lep1.E), axis=0)
WG_lep1_E = WG1_lep1.E
ZG_lep1_E = np.concatenate((ZG1_lep1.E, ZG2_lep1.E), axis=0)
WW_lep1_E = np.concatenate((WW1_lep1.E, WW2_lep1.E), axis=0)
WZ_lep1_E = np.concatenate((WZ1_lep1.E, WZ2_lep1.E), axis=0)
ZZ_lep1_E = np.concatenate((ZZ1_lep1.E, ZZ2_lep1.E), axis=0)
WWW_lep1_E = np.concatenate((WWW1_lep1.E, WWW2_lep1.E), axis=0)
WWZ_lep1_E = np.concatenate((WWZ1_lep1.E, WWZ2_lep1.E), axis=0)
WZZ_lep1_E = np.concatenate((WZZ1_lep1.E, WZZ2_lep1.E), axis=0)
ZZZ_lep1_E = np.concatenate((ZZZ1_lep1.E, ZZZ2_lep1.E), axis=0)
ttbarG_lep1_E = np.concatenate((ttbarG1_lep1.E, ttbarG2_lep1.E), axis=0)

WZG_lep1_F = np.concatenate((WZG1_lep1_Flav, WZG2_lep1_Flav), axis=0)
WG_lep1_F = WG1_lep1_Flav
ZG_lep1_F = np.concatenate((ZG1_lep1_Flav, ZG2_lep1_Flav), axis=0)
WW_lep1_F = np.concatenate((WW1_lep1_Flav, WW2_lep1_Flav), axis=0)
WZ_lep1_F = np.concatenate((WZ1_lep1_Flav, WZ2_lep1_Flav), axis=0)
ZZ_lep1_F = np.concatenate((ZZ1_lep1_Flav, ZZ2_lep1_Flav), axis=0)
WWW_lep1_F = np.concatenate((WWW1_lep1_Flav, WWW2_lep1_Flav), axis=0)
WWZ_lep1_F = np.concatenate((WWZ1_lep1_Flav, WWZ2_lep1_Flav), axis=0)
WZZ_lep1_F = np.concatenate((WZZ1_lep1_Flav, WZZ2_lep1_Flav), axis=0)
ZZZ_lep1_F = np.concatenate((ZZZ1_lep1_Flav, ZZZ2_lep1_Flav), axis=0)
ttbarG_lep1_F = np.concatenate((ttbarG1_lep1_Flav, ttbarG2_lep1_Flav), axis=0)

WZG_lep1_C = np.concatenate((WZG1_lep1_C, WZG2_lep1_C), axis=0)
WG_lep1_C = WG1_lep1_C
ZG_lep1_C = np.concatenate((ZG1_lep1_C, ZG2_lep1_C), axis=0)
WW_lep1_C = np.concatenate((WW1_lep1_C, WW2_lep1_C), axis=0)
WZ_lep1_C = np.concatenate((WZ1_lep1_C, WZ2_lep1_C), axis=0)
ZZ_lep1_C = np.concatenate((ZZ1_lep1_C, ZZ2_lep1_C), axis=0)
WWW_lep1_C = np.concatenate((WWW1_lep1_C, WWW2_lep1_C), axis=0)
WWZ_lep1_C = np.concatenate((WWZ1_lep1_C, WWZ2_lep1_C), axis=0)
WZZ_lep1_C = np.concatenate((WZZ1_lep1_C, WZZ2_lep1_C), axis=0)
ZZZ_lep1_C = np.concatenate((ZZZ1_lep1_C, ZZZ2_lep1_C), axis=0)
ttbarG_lep1_C = np.concatenate((ttbarG1_lep1_C, ttbarG2_lep1_C), axis=0)

WZG_lep2_pt = np.concatenate((WZG1_lep2.pt, WZG2_lep2.pt), axis=0)
WG_lep2_pt = WG1_lep2.pt
ZG_lep2_pt = np.concatenate((ZG1_lep2.pt, ZG2_lep2.pt), axis=0)
WW_lep2_pt = np.concatenate((WW1_lep2.pt, WW2_lep2.pt), axis=0)
WZ_lep2_pt = np.concatenate((WZ1_lep2.pt, WZ2_lep2.pt), axis=0)
ZZ_lep2_pt = np.concatenate((ZZ1_lep2.pt, ZZ2_lep2.pt), axis=0)
WWW_lep2_pt = np.concatenate((WWW1_lep2.pt, WWW2_lep2.pt), axis=0)
WWZ_lep2_pt = np.concatenate((WWZ1_lep2.pt, WWZ2_lep2.pt), axis=0)
WZZ_lep2_pt = np.concatenate((WZZ1_lep2.pt, WZZ2_lep2.pt), axis=0)
ZZZ_lep2_pt = np.concatenate((ZZZ1_lep2.pt, ZZZ2_lep2.pt), axis=0)
ttbarG_lep2_pt = np.concatenate((ttbarG1_lep2.pt, ttbarG2_lep2.pt), axis=0)

WZG_lep2_eta = np.concatenate((WZG1_lep2.eta, WZG2_lep2.eta), axis=0)
WG_lep2_eta = WG1_lep2.eta
ZG_lep2_eta = np.concatenate((ZG1_lep2.eta, ZG2_lep2.eta), axis=0)
WW_lep2_eta = np.concatenate((WW1_lep2.eta, WW2_lep2.eta), axis=0)
WZ_lep2_eta = np.concatenate((WZ1_lep2.eta, WZ2_lep2.eta), axis=0)
ZZ_lep2_eta = np.concatenate((ZZ1_lep2.eta, ZZ2_lep2.eta), axis=0)
WWW_lep2_eta = np.concatenate((WWW1_lep2.eta, WWW2_lep2.eta), axis=0)
WWZ_lep2_eta = np.concatenate((WWZ1_lep2.eta, WWZ2_lep2.eta), axis=0)
WZZ_lep2_eta = np.concatenate((WZZ1_lep2.eta, WZZ2_lep2.eta), axis=0)
ZZZ_lep2_eta = np.concatenate((ZZZ1_lep2.eta, ZZZ2_lep2.eta), axis=0)
ttbarG_lep2_eta = np.concatenate((ttbarG1_lep2.eta, ttbarG2_lep2.eta), axis=0)

WZG_lep2_phi = np.concatenate((WZG1_lep2.phi, WZG2_lep2.phi), axis=0)
WG_lep2_phi = WG1_lep2.phi
ZG_lep2_phi = np.concatenate((ZG1_lep2.phi, ZG2_lep2.phi), axis=0)
WW_lep2_phi = np.concatenate((WW1_lep2.phi, WW2_lep2.phi), axis=0)
WZ_lep2_phi = np.concatenate((WZ1_lep2.phi, WZ2_lep2.phi), axis=0)
ZZ_lep2_phi = np.concatenate((ZZ1_lep2.phi, ZZ2_lep2.phi), axis=0)
WWW_lep2_phi = np.concatenate((WWW1_lep2.phi, WWW2_lep2.phi), axis=0)
WWZ_lep2_phi = np.concatenate((WWZ1_lep2.phi, WWZ2_lep2.phi), axis=0)
WZZ_lep2_phi = np.concatenate((WZZ1_lep2.phi, WZZ2_lep2.phi), axis=0)
ZZZ_lep2_phi = np.concatenate((ZZZ1_lep2.phi, ZZZ2_lep2.phi), axis=0)
ttbarG_lep2_phi = np.concatenate((ttbarG1_lep2.phi, ttbarG2_lep2.phi), axis=0)

WZG_lep2_mass = np.concatenate((WZG1_lep2.mass, WZG2_lep2.mass), axis=0)
WG_lep2_mass = WG1_lep2.mass
ZG_lep2_mass = np.concatenate((ZG1_lep2.mass, ZG2_lep2.mass), axis=0)
WW_lep2_mass = np.concatenate((WW1_lep2.mass, WW2_lep2.mass), axis=0)
WZ_lep2_mass = np.concatenate((WZ1_lep2.mass, WZ2_lep2.mass), axis=0)
ZZ_lep2_mass = np.concatenate((ZZ1_lep2.mass, ZZ2_lep2.mass), axis=0)
WWW_lep2_mass = np.concatenate((WWW1_lep2.mass, WWW2_lep2.mass), axis=0)
WWZ_lep2_mass = np.concatenate((WWZ1_lep2.mass, WWZ2_lep2.mass), axis=0)
WZZ_lep2_mass = np.concatenate((WZZ1_lep2.mass, WZZ2_lep2.mass), axis=0)
ZZZ_lep2_mass = np.concatenate((ZZZ1_lep2.mass, ZZZ2_lep2.mass), axis=0)
ttbarG_lep2_mass = np.concatenate((ttbarG1_lep2.mass, ttbarG2_lep2.mass), axis=0)

WZG_lep2_E = np.concatenate((WZG1_lep2.E, WZG2_lep2.E), axis=0)
WG_lep2_E = WG1_lep2.E
ZG_lep2_E = np.concatenate((ZG1_lep2.E, ZG2_lep2.E), axis=0)
WW_lep2_E = np.concatenate((WW1_lep2.E, WW2_lep2.E), axis=0)
WZ_lep2_E = np.concatenate((WZ1_lep2.E, WZ2_lep2.E), axis=0)
ZZ_lep2_E = np.concatenate((ZZ1_lep2.E, ZZ2_lep2.E), axis=0)
WWW_lep2_E = np.concatenate((WWW1_lep2.E, WWW2_lep2.E), axis=0)
WWZ_lep2_E = np.concatenate((WWZ1_lep2.E, WWZ2_lep2.E), axis=0)
WZZ_lep2_E = np.concatenate((WZZ1_lep2.E, WZZ2_lep2.E), axis=0)
ZZZ_lep2_E = np.concatenate((ZZZ1_lep2.E, ZZZ2_lep2.E), axis=0)
ttbarG_lep2_E = np.concatenate((ttbarG1_lep2.E, ttbarG2_lep2.E), axis=0)

WZG_lep2_F = np.concatenate((WZG1_lep2_Flav, WZG2_lep2_Flav), axis=0)
WG_lep2_F = WG1_lep2_Flav
ZG_lep2_F = np.concatenate((ZG1_lep2_Flav, ZG2_lep2_Flav), axis=0)
WW_lep2_F = np.concatenate((WW1_lep2_Flav, WW2_lep2_Flav), axis=0)
WZ_lep2_F = np.concatenate((WZ1_lep2_Flav, WZ2_lep2_Flav), axis=0)
ZZ_lep2_F = np.concatenate((ZZ1_lep2_Flav, ZZ2_lep2_Flav), axis=0)
WWW_lep2_F = np.concatenate((WWW1_lep2_Flav, WWW2_lep2_Flav), axis=0)
WWZ_lep2_F = np.concatenate((WWZ1_lep2_Flav, WWZ2_lep2_Flav), axis=0)
WZZ_lep2_F = np.concatenate((WZZ1_lep2_Flav, WZZ2_lep2_Flav), axis=0)
ZZZ_lep2_F = np.concatenate((ZZZ1_lep2_Flav, ZZZ2_lep2_Flav), axis=0)
ttbarG_lep2_F = np.concatenate((ttbarG1_lep2_Flav, ttbarG2_lep2_Flav), axis=0)

WZG_lep2_C = np.concatenate((WZG1_lep2_C, WZG2_lep2_C), axis=0)
WG_lep2_C = WG1_lep2_C
ZG_lep2_C = np.concatenate((ZG1_lep2_C, ZG2_lep2_C), axis=0)
WW_lep2_C = np.concatenate((WW1_lep2_C, WW2_lep2_C), axis=0)
WZ_lep2_C = np.concatenate((WZ1_lep2_C, WZ2_lep2_C), axis=0)
ZZ_lep2_C = np.concatenate((ZZ1_lep2_C, ZZ2_lep2_C), axis=0)
WWW_lep2_C = np.concatenate((WWW1_lep2_C, WWW2_lep2_C), axis=0)
WWZ_lep2_C = np.concatenate((WWZ1_lep2_C, WWZ2_lep2_C), axis=0)
WZZ_lep2_C = np.concatenate((WZZ1_lep2_C, WZZ2_lep2_C), axis=0)
ZZZ_lep2_C = np.concatenate((ZZZ1_lep2_C, ZZZ2_lep2_C), axis=0)
ttbarG_lep2_C = np.concatenate((ttbarG1_lep2_C, ttbarG2_lep2_C), axis=0)

WZG_lep3_pt = np.concatenate((WZG1_lep3.pt, WZG2_lep3.pt), axis=0)
WG_lep3_pt = WG1_lep3.pt
ZG_lep3_pt = np.concatenate((ZG1_lep3.pt, ZG2_lep3.pt), axis=0)
WW_lep3_pt = np.concatenate((WW1_lep3.pt, WW2_lep3.pt), axis=0)
WZ_lep3_pt = np.concatenate((WZ1_lep3.pt, WZ2_lep3.pt), axis=0)
ZZ_lep3_pt = np.concatenate((ZZ1_lep3.pt, ZZ2_lep3.pt), axis=0)
WWW_lep3_pt = np.concatenate((WWW1_lep3.pt, WWW2_lep3.pt), axis=0)
WWZ_lep3_pt = np.concatenate((WWZ1_lep3.pt, WWZ2_lep3.pt), axis=0)
WZZ_lep3_pt = np.concatenate((WZZ1_lep3.pt, WZZ2_lep3.pt), axis=0)
ZZZ_lep3_pt = np.concatenate((ZZZ1_lep3.pt, ZZZ2_lep3.pt), axis=0)
ttbarG_lep3_pt = np.concatenate((ttbarG1_lep3.pt, ttbarG2_lep3.pt), axis=0)

WZG_lep3_eta = np.concatenate((WZG1_lep3.eta, WZG2_lep3.eta), axis=0)
WG_lep3_eta = WG1_lep3.eta
ZG_lep3_eta = np.concatenate((ZG1_lep3.eta, ZG2_lep3.eta), axis=0)
WW_lep3_eta = np.concatenate((WW1_lep3.eta, WW2_lep3.eta), axis=0)
WZ_lep3_eta = np.concatenate((WZ1_lep3.eta, WZ2_lep3.eta), axis=0)
ZZ_lep3_eta = np.concatenate((ZZ1_lep3.eta, ZZ2_lep3.eta), axis=0)
WWW_lep3_eta = np.concatenate((WWW1_lep3.eta, WWW2_lep3.eta), axis=0)
WWZ_lep3_eta = np.concatenate((WWZ1_lep3.eta, WWZ2_lep3.eta), axis=0)
WZZ_lep3_eta = np.concatenate((WZZ1_lep3.eta, WZZ2_lep3.eta), axis=0)
ZZZ_lep3_eta = np.concatenate((ZZZ1_lep3.eta, ZZZ2_lep3.eta), axis=0)
ttbarG_lep3_eta = np.concatenate((ttbarG1_lep3.eta, ttbarG2_lep3.eta), axis=0)

WZG_lep3_phi = np.concatenate((WZG1_lep3.phi, WZG2_lep3.phi), axis=0)
WG_lep3_phi = WG1_lep3.phi
ZG_lep3_phi = np.concatenate((ZG1_lep3.phi, ZG2_lep3.phi), axis=0)
WW_lep3_phi = np.concatenate((WW1_lep3.phi, WW2_lep3.phi), axis=0)
WZ_lep3_phi = np.concatenate((WZ1_lep3.phi, WZ2_lep3.phi), axis=0)
ZZ_lep3_phi = np.concatenate((ZZ1_lep3.phi, ZZ2_lep3.phi), axis=0)
WWW_lep3_phi = np.concatenate((WWW1_lep3.phi, WWW2_lep3.phi), axis=0)
WWZ_lep3_phi = np.concatenate((WWZ1_lep3.phi, WWZ2_lep3.phi), axis=0)
WZZ_lep3_phi = np.concatenate((WZZ1_lep3.phi, WZZ2_lep3.phi), axis=0)
ZZZ_lep3_phi = np.concatenate((ZZZ1_lep3.phi, ZZZ2_lep3.phi), axis=0)
ttbarG_lep3_phi = np.concatenate((ttbarG1_lep3.phi, ttbarG2_lep3.phi), axis=0)

WZG_lep3_mass = np.concatenate((WZG1_lep3.mass, WZG2_lep3.mass), axis=0)
WG_lep3_mass = WG1_lep3.mass
ZG_lep3_mass = np.concatenate((ZG1_lep3.mass, ZG2_lep3.mass), axis=0)
WW_lep3_mass = np.concatenate((WW1_lep3.mass, WW2_lep3.mass), axis=0)
WZ_lep3_mass = np.concatenate((WZ1_lep3.mass, WZ2_lep3.mass), axis=0)
ZZ_lep3_mass = np.concatenate((ZZ1_lep3.mass, ZZ2_lep3.mass), axis=0)
WWW_lep3_mass = np.concatenate((WWW1_lep3.mass, WWW2_lep3.mass), axis=0)
WWZ_lep3_mass = np.concatenate((WWZ1_lep3.mass, WWZ2_lep3.mass), axis=0)
WZZ_lep3_mass = np.concatenate((WZZ1_lep3.mass, WZZ2_lep3.mass), axis=0)
ZZZ_lep3_mass = np.concatenate((ZZZ1_lep3.mass, ZZZ2_lep3.mass), axis=0)
ttbarG_lep3_mass = np.concatenate((ttbarG1_lep3.mass, ttbarG2_lep3.mass), axis=0)

WZG_lep3_E = np.concatenate((WZG1_lep3.E, WZG2_lep3.E), axis=0)
WG_lep3_E = WG1_lep3.E
ZG_lep3_E = np.concatenate((ZG1_lep3.E, ZG2_lep3.E), axis=0)
WW_lep3_E = np.concatenate((WW1_lep3.E, WW2_lep3.E), axis=0)
WZ_lep3_E = np.concatenate((WZ1_lep3.E, WZ2_lep3.E), axis=0)
ZZ_lep3_E = np.concatenate((ZZ1_lep3.E, ZZ2_lep3.E), axis=0)
WWW_lep3_E = np.concatenate((WWW1_lep3.E, WWW2_lep3.E), axis=0)
WWZ_lep3_E = np.concatenate((WWZ1_lep3.E, WWZ2_lep3.E), axis=0)
WZZ_lep3_E = np.concatenate((WZZ1_lep3.E, WZZ2_lep3.E), axis=0)
ZZZ_lep3_E = np.concatenate((ZZZ1_lep3.E, ZZZ2_lep3.E), axis=0)
ttbarG_lep3_E = np.concatenate((ttbarG1_lep3.E, ttbarG2_lep3.E), axis=0)

WZG_lep3_F = np.concatenate((WZG1_lep3_Flav, WZG2_lep3_Flav), axis=0)
WG_lep3_F = WG1_lep3_Flav
ZG_lep3_F = np.concatenate((ZG1_lep3_Flav, ZG2_lep3_Flav), axis=0)
WW_lep3_F = np.concatenate((WW1_lep3_Flav, WW2_lep3_Flav), axis=0)
WZ_lep3_F = np.concatenate((WZ1_lep3_Flav, WZ2_lep3_Flav), axis=0)
ZZ_lep3_F = np.concatenate((ZZ1_lep3_Flav, ZZ2_lep3_Flav), axis=0)
WWW_lep3_F = np.concatenate((WWW1_lep3_Flav, WWW2_lep3_Flav), axis=0)
WWZ_lep3_F = np.concatenate((WWZ1_lep3_Flav, WWZ2_lep3_Flav), axis=0)
WZZ_lep3_F = np.concatenate((WZZ1_lep3_Flav, WZZ2_lep3_Flav), axis=0)
ZZZ_lep3_F = np.concatenate((ZZZ1_lep3_Flav, ZZZ2_lep3_Flav), axis=0)
ttbarG_lep3_F = np.concatenate((ttbarG1_lep3_Flav, ttbarG2_lep3_Flav), axis=0)

WZG_lep3_C = np.concatenate((WZG1_lep3_C, WZG2_lep3_C), axis=0)
WG_lep3_C = WG1_lep3_C
ZG_lep3_C = np.concatenate((ZG1_lep3_C, ZG2_lep3_C), axis=0)
WW_lep3_C = np.concatenate((WW1_lep3_C, WW2_lep3_C), axis=0)
WZ_lep3_C = np.concatenate((WZ1_lep3_C, WZ2_lep3_C), axis=0)
ZZ_lep3_C = np.concatenate((ZZ1_lep3_C, ZZ2_lep3_C), axis=0)
WWW_lep3_C = np.concatenate((WWW1_lep3_C, WWW2_lep3_C), axis=0)
WWZ_lep3_C = np.concatenate((WWZ1_lep3_C, WWZ2_lep3_C), axis=0)
WZZ_lep3_C = np.concatenate((WZZ1_lep3_C, WZZ2_lep3_C), axis=0)
ZZZ_lep3_C = np.concatenate((ZZZ1_lep3_C, ZZZ2_lep3_C), axis=0)
ttbarG_lep3_C = np.concatenate((ttbarG1_lep3_C, ttbarG2_lep3_C), axis=0)

WZG_Pho_pt = np.concatenate((WZG1_Pho.pt, WZG2_Pho.pt), axis=0)
WG_Pho_pt = WG1_Pho.pt
ZG_Pho_pt = np.concatenate((ZG1_Pho.pt, ZG2_Pho.pt), axis=0)
WW_Pho_pt = np.concatenate((WW1_Pho.pt, WW2_Pho.pt), axis=0)
WZ_Pho_pt = np.concatenate((WZ1_Pho.pt, WZ2_Pho.pt), axis=0)
ZZ_Pho_pt = np.concatenate((ZZ1_Pho.pt, ZZ2_Pho.pt), axis=0)
WWW_Pho_pt = np.concatenate((WWW1_Pho.pt, WWW2_Pho.pt), axis=0)
WWZ_Pho_pt = np.concatenate((WWZ1_Pho.pt, WWZ2_Pho.pt), axis=0)
WZZ_Pho_pt = np.concatenate((WZZ1_Pho.pt, WZZ2_Pho.pt), axis=0)
ZZZ_Pho_pt = np.concatenate((ZZZ1_Pho.pt, ZZZ2_Pho.pt), axis=0)
ttbarG_Pho_pt = np.concatenate((ttbarG1_Pho.pt, ttbarG2_Pho.pt), axis=0)

WZG_Pho_eta = np.concatenate((WZG1_Pho.eta, WZG2_Pho.eta), axis=0)
WG_Pho_eta = WG1_Pho.eta
ZG_Pho_eta = np.concatenate((ZG1_Pho.eta, ZG2_Pho.eta), axis=0)
WW_Pho_eta = np.concatenate((WW1_Pho.eta, WW2_Pho.eta), axis=0)
WZ_Pho_eta = np.concatenate((WZ1_Pho.eta, WZ2_Pho.eta), axis=0)
ZZ_Pho_eta = np.concatenate((ZZ1_Pho.eta, ZZ2_Pho.eta), axis=0)
WWW_Pho_eta = np.concatenate((WWW1_Pho.eta, WWW2_Pho.eta), axis=0)
WWZ_Pho_eta = np.concatenate((WWZ1_Pho.eta, WWZ2_Pho.eta), axis=0)
WZZ_Pho_eta = np.concatenate((WZZ1_Pho.eta, WZZ2_Pho.eta), axis=0)
ZZZ_Pho_eta = np.concatenate((ZZZ1_Pho.eta, ZZZ2_Pho.eta), axis=0)
ttbarG_Pho_eta = np.concatenate((ttbarG1_Pho.eta, ttbarG2_Pho.eta), axis=0)

WZG_Pho_phi = np.concatenate((WZG1_Pho.phi, WZG2_Pho.phi), axis=0)
WG_Pho_phi = WG1_Pho.phi
ZG_Pho_phi = np.concatenate((ZG1_Pho.phi, ZG2_Pho.phi), axis=0)
WW_Pho_phi = np.concatenate((WW1_Pho.phi, WW2_Pho.phi), axis=0)
WZ_Pho_phi = np.concatenate((WZ1_Pho.phi, WZ2_Pho.phi), axis=0)
ZZ_Pho_phi = np.concatenate((ZZ1_Pho.phi, ZZ2_Pho.phi), axis=0)
WWW_Pho_phi = np.concatenate((WWW1_Pho.phi, WWW2_Pho.phi), axis=0)
WWZ_Pho_phi = np.concatenate((WWZ1_Pho.phi, WWZ2_Pho.phi), axis=0)
WZZ_Pho_phi = np.concatenate((WZZ1_Pho.phi, WZZ2_Pho.phi), axis=0)
ZZZ_Pho_phi = np.concatenate((ZZZ1_Pho.phi, ZZZ2_Pho.phi), axis=0)
ttbarG_Pho_phi = np.concatenate((ttbarG1_Pho.phi, ttbarG2_Pho.phi), axis=0)

WZG_Pho_E = np.concatenate((WZG1_Pho.E, WZG2_Pho.E), axis=0)
WG_Pho_E = WG1_Pho.E
ZG_Pho_E = np.concatenate((ZG1_Pho.E, ZG2_Pho.E), axis=0)
WW_Pho_E = np.concatenate((WW1_Pho.E, WW2_Pho.E), axis=0)
WZ_Pho_E = np.concatenate((WZ1_Pho.E, WZ2_Pho.E), axis=0)
ZZ_Pho_E = np.concatenate((ZZ1_Pho.E, ZZ2_Pho.E), axis=0)
WWW_Pho_E = np.concatenate((WWW1_Pho.E, WWW2_Pho.E), axis=0)
WWZ_Pho_E = np.concatenate((WWZ1_Pho.E, WWZ2_Pho.E), axis=0)
WZZ_Pho_E = np.concatenate((WZZ1_Pho.E, WZZ2_Pho.E), axis=0)
ZZZ_Pho_E = np.concatenate((ZZZ1_Pho.E, ZZZ2_Pho.E), axis=0)
ttbarG_Pho_E = np.concatenate((ttbarG1_Pho.E, ttbarG2_Pho.E), axis=0)

WZG_MET_pt = np.concatenate((WZG1_MET.pt, WZG2_MET.pt), axis=0)
WG_MET_pt = WG1_MET.pt
ZG_MET_pt = np.concatenate((ZG1_MET.pt, ZG2_MET.pt), axis=0)
WW_MET_pt = np.concatenate((WW1_MET.pt, WW2_MET.pt), axis=0)
WZ_MET_pt = np.concatenate((WZ1_MET.pt, WZ2_MET.pt), axis=0)
ZZ_MET_pt = np.concatenate((ZZ1_MET.pt, ZZ2_MET.pt), axis=0)
WWW_MET_pt = np.concatenate((WWW1_MET.pt, WWW2_MET.pt), axis=0)
WWZ_MET_pt = np.concatenate((WWZ1_MET.pt, WWZ2_MET.pt), axis=0)
WZZ_MET_pt = np.concatenate((WZZ1_MET.pt, WZZ2_MET.pt), axis=0)
ZZZ_MET_pt = np.concatenate((ZZZ1_MET.pt, ZZZ2_MET.pt), axis=0)
ttbarG_MET_pt = np.concatenate((ttbarG1_MET.pt, ttbarG2_MET.pt), axis=0)

WZG_MET_phi = np.concatenate((WZG1_MET.phi, WZG2_MET.phi), axis=0)
WG_MET_phi = WG1_MET.phi
ZG_MET_phi = np.concatenate((ZG1_MET.phi, ZG2_MET.phi), axis=0)
WW_MET_phi = np.concatenate((WW1_MET.phi, WW2_MET.phi), axis=0)
WZ_MET_phi = np.concatenate((WZ1_MET.phi, WZ2_MET.phi), axis=0)
ZZ_MET_phi = np.concatenate((ZZ1_MET.phi, ZZ2_MET.phi), axis=0)
WWW_MET_phi = np.concatenate((WWW1_MET.phi, WWW2_MET.phi), axis=0)
WWZ_MET_phi = np.concatenate((WWZ1_MET.phi, WWZ2_MET.phi), axis=0)
WZZ_MET_phi = np.concatenate((WZZ1_MET.phi, WZZ2_MET.phi), axis=0)
ZZZ_MET_phi = np.concatenate((ZZZ1_MET.phi, ZZZ2_MET.phi), axis=0)
ttbarG_MET_phi = np.concatenate((ttbarG1_MET.phi, ttbarG2_MET.phi), axis=0)

WZG_MT = np.concatenate((WZG1_MT, WZG2_MT), axis=0)
WG_MT = WG1_MT
ZG_MT = np.concatenate((ZG1_MT, ZG2_MT), axis=0)
WW_MT = np.concatenate((WW1_MT, WW2_MT), axis=0)
WZ_MT = np.concatenate((WZ1_MT, WZ2_MT), axis=0)
ZZ_MT = np.concatenate((ZZ1_MT, ZZ2_MT), axis=0)
WWW_MT = np.concatenate((WWW1_MT, WWW2_MT), axis=0)
WWZ_MT = np.concatenate((WWZ1_MT, WWZ2_MT), axis=0)
WZZ_MT = np.concatenate((WZZ1_MT, WZZ2_MT), axis=0)
ZZZ_MT = np.concatenate((ZZZ1_MT, ZZZ2_MT), axis=0)
ttbarG_MT = np.concatenate((ttbarG1_MT, ttbarG2_MT), axis=0)

WZG_Dilepptsum = np.concatenate((WZG1_Dilepptsum, WZG2_Dilepptsum), axis=0)
WG_Dilepptsum = WG1_Dilepptsum
ZG_Dilepptsum = np.concatenate((ZG1_Dilepptsum, ZG2_Dilepptsum), axis=0)
WW_Dilepptsum = np.concatenate((WW1_Dilepptsum, WW2_Dilepptsum), axis=0)
WZ_Dilepptsum = np.concatenate((WZ1_Dilepptsum, WZ2_Dilepptsum), axis=0)
ZZ_Dilepptsum = np.concatenate((ZZ1_Dilepptsum, ZZ2_Dilepptsum), axis=0)
WWW_Dilepptsum = np.concatenate((WWW1_Dilepptsum, WWW2_Dilepptsum), axis=0)
WWZ_Dilepptsum = np.concatenate((WWZ1_Dilepptsum, WWZ2_Dilepptsum), axis=0)
WZZ_Dilepptsum = np.concatenate((WZZ1_Dilepptsum, WZZ2_Dilepptsum), axis=0)
ZZZ_Dilepptsum = np.concatenate((ZZZ1_Dilepptsum, ZZZ2_Dilepptsum), axis=0)
ttbarG_Dilepptsum = np.concatenate((ttbarG1_Dilepptsum, ttbarG2_Dilepptsum), axis=0)

WZG_Trilepptsum = np.concatenate((WZG1_Trilepptsum, WZG2_Trilepptsum), axis=0)
WG_Trilepptsum = WG1_Trilepptsum
ZG_Trilepptsum = np.concatenate((ZG1_Trilepptsum, ZG2_Trilepptsum), axis=0)
WW_Trilepptsum = np.concatenate((WW1_Trilepptsum, WW2_Trilepptsum), axis=0)
WZ_Trilepptsum = np.concatenate((WZ1_Trilepptsum, WZ2_Trilepptsum), axis=0)
ZZ_Trilepptsum = np.concatenate((ZZ1_Trilepptsum, ZZ2_Trilepptsum), axis=0)
WWW_Trilepptsum = np.concatenate((WWW1_Trilepptsum, WWW2_Trilepptsum), axis=0)
WWZ_Trilepptsum = np.concatenate((WWZ1_Trilepptsum, WWZ2_Trilepptsum), axis=0)
WZZ_Trilepptsum = np.concatenate((WZZ1_Trilepptsum, WZZ2_Trilepptsum), axis=0)
ZZZ_Trilepptsum = np.concatenate((ZZZ1_Trilepptsum, ZZZ2_Trilepptsum), axis=0)
ttbarG_Trilepptsum = np.concatenate((ttbarG1_Trilepptsum, ttbarG2_Trilepptsum), axis=0)

WZG_Trilepphoptsum = np.concatenate((WZG1_Trilepphoptsum, WZG2_Trilepphoptsum), axis=0)
WG_Trilepphoptsum = WG1_Trilepphoptsum
ZG_Trilepphoptsum = np.concatenate((ZG1_Trilepphoptsum, ZG2_Trilepphoptsum), axis=0)
WW_Trilepphoptsum = np.concatenate((WW1_Trilepphoptsum, WW2_Trilepphoptsum), axis=0)
WZ_Trilepphoptsum = np.concatenate((WZ1_Trilepphoptsum, WZ2_Trilepphoptsum), axis=0)
ZZ_Trilepphoptsum = np.concatenate((ZZ1_Trilepphoptsum, ZZ2_Trilepphoptsum), axis=0)
WWW_Trilepphoptsum = np.concatenate((WWW1_Trilepphoptsum, WWW2_Trilepphoptsum), axis=0)
WWZ_Trilepphoptsum = np.concatenate((WWZ1_Trilepphoptsum, WWZ2_Trilepphoptsum), axis=0)
WZZ_Trilepphoptsum = np.concatenate((WZZ1_Trilepphoptsum, WZZ2_Trilepphoptsum), axis=0)
ZZZ_Trilepphoptsum = np.concatenate((ZZZ1_Trilepphoptsum, ZZZ2_Trilepphoptsum), axis=0)
ttbarG_Trilepphoptsum = np.concatenate((ttbarG1_Trilepphoptsum, ttbarG2_Trilepphoptsum), axis=0)

# Dict

WZG = ak.zip({

"Dilep_pt" : WZG_Dilep_pt,
"Dilep_mass" : WZG_Dilep_mass,
"Dilep_E" : WZG_Dilep_E,
"Trilep_pt" : WZG_Trilep_pt,
"Trilep_mass" : WZG_Trilep_mass,
"Trilep_E" : WZG_Trilep_E,
"Trileppho_pt" : WZG_Trileppho_pt,
"Trileppho_mass" : WZG_Trileppho_mass,
"Trileppho_E" : WZG_Trileppho_E,
"lep1_pt" : WZG_lep1_pt,
"lep1_eta" : WZG_lep1_eta,
"lep1_phi" : WZG_lep1_phi,
"lep1_mass" : WZG_lep1_mass,
"lep1_E" : WZG_lep1_E,
"lep1_F" : WZG_lep1_F,
"lep1_C" : WZG_lep1_C,
"lep2_pt" : WZG_lep2_pt,
"lep2_eta" : WZG_lep2_eta,
"lep2_phi" :  WZG_lep2_phi,
"lep2_mass" :  WZG_lep2_mass,
"lep2_E" :   WZG_lep2_E,
"lep2_F" : WZG_lep2_F,
"lep2_C" : WZG_lep2_C,
"lep3_pt" : WZG_lep3_pt,
"lep3_eta" : WZG_lep3_eta,
"lep3_phi" : WZG_lep3_phi,
"lep3_mass" : WZG_lep3_mass,
"lep3_E" : WZG_lep3_E,
"lep3_F" : WZG_lep3_F,
"lep3_C" : WZG_lep3_C,
"Pho_pt" : WZG_Pho_pt,
"Pho_eta" : WZG_Pho_eta,
"Pho_phi" : WZG_Pho_phi,
"Pho_E" : WZG_Pho_E,
"MET_pt" : WZG_MET_pt,
"MET_phi" : WZG_MET_phi,
"MT" : WZG_MT,
"Dilepptsum" : WZG_Dilepptsum,
"Trilepptsum" : WZG_Trilepptsum,
"Trilepphoptsum" : WZG_Trilepphoptsum

})

WG = ak.zip({

"Dilep_pt" : WG_Dilep_pt,
"Dilep_mass" : WG_Dilep_mass,
"Dilep_E" : WG_Dilep_E,
"Trilep_pt" : WG_Trilep_pt,
"Trilep_mass" : WG_Trilep_mass,
"Trilep_E" : WG_Trilep_E,
"Trileppho_pt" : WG_Trileppho_pt,
"Trileppho_mass" : WG_Trileppho_mass,
"Trileppho_E" : WG_Trileppho_E,
"lep1_pt" : WG_lep1_pt,
"lep1_eta" : WG_lep1_eta,
"lep1_phi" : WG_lep1_phi,
"lep1_mass" : WG_lep1_mass,
"lep1_E" :   WG_lep1_E,
"lep1_F" : WG_lep1_F,
"lep1_C" : WG_lep1_C,
"lep2_pt" : WG_lep2_pt,
"lep2_eta" : WG_lep2_eta,
"lep2_phi" :  WG_lep2_phi,
"lep2_mass" :  WG_lep2_mass,
"lep2_E" :   WG_lep2_E,
"lep2_F" : WG_lep2_F,
"lep2_C" : WG_lep2_C,
"lep3_pt" : WG_lep3_pt,
"lep3_eta" : WG_lep3_eta,
"lep3_phi" : WG_lep3_phi,
"lep3_mass" : WG_lep3_mass,
"lep3_E" : WG_lep3_E,
"lep3_F" : WG_lep3_F,
"lep3_C" : WG_lep3_C,
"Pho_pt" : WG_Pho_pt,
"Pho_eta" : WG_Pho_eta,
"Pho_phi" : WG_Pho_phi,
"Pho_E" : WG_Pho_E,
"MET_pt" : WG_MET_pt,
"MET_phi" : WG_MET_phi,
"MT" : WG_MT,
"Dilepptsum" : WG_Dilepptsum,
"Trilepptsum" : WG_Trilepptsum,
"Trilepphoptsum" : WG_Trilepphoptsum

})

ZG = ak.zip({

"Dilep_pt" : ZG_Dilep_pt,
"Dilep_mass" : ZG_Dilep_mass,
"Dilep_E" : ZG_Dilep_E,
"Trilep_pt" : ZG_Trilep_pt,
"Trilep_mass" : ZG_Trilep_mass,
"Trilep_E" : ZG_Trilep_E,
"Trileppho_pt" : ZG_Trileppho_pt,
"Trileppho_mass" : ZG_Trileppho_mass,
"Trileppho_E" : ZG_Trileppho_E,
"lep1_pt" : ZG_lep1_pt,
"lep1_eta" : ZG_lep1_eta,
"lep1_phi" : ZG_lep1_phi,
"lep1_mass" : ZG_lep1_mass,
"lep1_E" :   ZG_lep1_E,
"lep1_F" : ZG_lep1_F,
"lep1_C" : [],
"lep2_pt" : ZG_lep2_pt,
"lep2_eta" : ZG_lep2_eta,
"lep2_phi" :  ZG_lep2_phi,
"lep2_mass" :  ZG_lep2_mass,
"lep2_E" :   ZG_lep2_E,
"lep2_F" : ZG_lep2_F,
"lep2_C" : [],
"lep3_pt" : ZG_lep3_pt,
"lep3_eta" : ZG_lep3_eta,
"lep3_phi" : ZG_lep3_phi,
"lep3_mass" : ZG_lep3_mass,
"lep3_E" : ZG_lep3_E,
"lep3_F" : ZG_lep3_F,
"lep3_C" : [],
"Pho_pt" : ZG_Pho_pt,
"Pho_eta" : ZG_Pho_eta,
"Pho_phi" : ZG_Pho_phi,
"Pho_E" : ZG_Pho_E,
"MET_pt" : ZG_MET_pt,
"MET_phi" : ZG_MET_phi,
"MT" : ZG_MT,
"Dilepptsum" : ZG_Dilepptsum,
"Trilepptsum" : ZG_Trilepptsum,
"Trilepphoptsum" : ZG_Trilepphoptsum

})

WW = ak.zip({

"Dilep_pt" : WW_Dilep_pt,
"Dilep_mass" : WW_Dilep_mass,
"Dilep_E" : WW_Dilep_E,
"Trilep_pt" : WW_Trilep_pt,
"Trilep_mass" : WW_Trilep_mass,
"Trilep_E" : WW_Trilep_E,
"Trileppho_pt" : WW_Trileppho_pt,
"Trileppho_mass" : WW_Trileppho_mass,
"Trileppho_E" : WW_Trileppho_E,
"lep1_pt" : WW_lep1_pt,
"lep1_eta" : WW_lep1_eta,
"lep1_phi" : WW_lep1_phi,
"lep1_mass" : WW_lep1_mass,
"lep1_E" :   WW_lep1_E,
"lep1_F" : WW_lep1_F,
"lep1_C" : WW_lep1_C,
"lep2_pt" : WW_lep2_pt,
"lep2_eta" : WW_lep2_eta,
"lep2_phi" :  WW_lep2_phi,
"lep2_mass" :  WW_lep2_mass,
"lep2_E" :   WW_lep2_E,
"lep2_F" : WW_lep2_F,
"lep2_C" : WW_lep2_C,
"lep3_pt" : WW_lep3_pt,
"lep3_eta" : WW_lep3_eta,
"lep3_phi" : WW_lep3_phi,
"lep3_mass" : WW_lep3_mass,
"lep3_E" : WW_lep3_E,
"lep3_F" : WW_lep3_F,
"lep3_C" : WW_lep3_C,
"Pho_pt" : WW_Pho_pt,
"Pho_eta" : WW_Pho_eta,
"Pho_phi" : WW_Pho_phi,
"Pho_E" : WW_Pho_E,
"MET_pt" : WW_MET_pt,
"MET_phi" : WW_MET_phi,
"MT" : WW_MT,
"Dilepptsum" : WW_Dilepptsum,
"Trilepptsum" : WW_Trilepptsum,
"Trilepphoptsum" : WW_Trilepphoptsum

})

WZ = ak.zip({

"Dilep_pt" : WZ_Dilep_pt,
"Dilep_mass" : WZ_Dilep_mass,
"Dilep_E" : WZ_Dilep_E,
"Trilep_pt" : WZ_Trilep_pt,
"Trilep_mass" : WZ_Trilep_mass,
"Trilep_E" : WZ_Trilep_E,
"Trileppho_pt" : WZ_Trileppho_pt,
"Trileppho_mass" : WZ_Trileppho_mass,
"Trileppho_E" : WZ_Trileppho_E,
"lep1_pt" : WZ_lep1_pt,
"lep1_eta" : WZ_lep1_eta,
"lep1_phi" : WZ_lep1_phi,
"lep1_mass" : WZ_lep1_mass,
"lep1_E" :   WZ_lep1_E,
"lep1_F" : WZ_lep1_F,
"lep1_C" : WZ_lep1_C,
"lep2_pt" : WZ_lep2_pt,
"lep2_eta" : WZ_lep2_eta,
"lep2_phi" :  WZ_lep2_phi,
"lep2_mass" :  WZ_lep2_mass,
"lep2_E" :   WZ_lep2_E,
"lep2_F" : WZ_lep2_F,
"lep2_C" : WZ_lep2_C,
"lep3_pt" : WZ_lep3_pt,
"lep3_eta" : WZ_lep3_eta,
"lep3_phi" : WZ_lep3_phi,
"lep3_mass" : WZ_lep3_mass,
"lep3_E" : WZ_lep3_E,
"lep3_F" : WZ_lep3_F,
"lep3_C" : WZ_lep3_C,
"Pho_pt" : WZ_Pho_pt,
"Pho_eta" : WZ_Pho_eta,
"Pho_phi" : WZ_Pho_phi,
"Pho_E" : WZ_Pho_E,
"MET_pt" : WZ_MET_pt,
"MET_phi" : WZ_MET_phi,
"MT" : WZ_MT,
"Dilepptsum" : WZ_Dilepptsum,
"Trilepptsum" : WZ_Trilepptsum,
"Trilepphoptsum" : WZ_Trilepphoptsum

})

ZZ = ak.zip({

"Dilep_pt" : ZZ_Dilep_pt,
"Dilep_mass" : ZZ_Dilep_mass,
"Dilep_E" : ZZ_Dilep_E,
"Trilep_pt" : ZZ_Trilep_pt,
"Trilep_mass" : ZZ_Trilep_mass,
"Trilep_E" : ZZ_Trilep_E,
"Trileppho_pt" : ZZ_Trileppho_pt,
"Trileppho_mass" : ZZ_Trileppho_mass,
"Trileppho_E" : ZZ_Trileppho_E,
"lep1_pt" : ZZ_lep1_pt,
"lep1_eta" : ZZ_lep1_eta,
"lep1_phi" : ZZ_lep1_phi,
"lep1_mass" : ZZ_lep1_mass,
"lep1_E" :   ZZ_lep1_E,
"lep1_F" : ZZ_lep1_F,
"lep1_C" : ZZ_lep1_C,
"lep2_pt" : ZZ_lep2_pt,
"lep2_eta" : ZZ_lep2_eta,
"lep2_phi" :  ZZ_lep2_phi,
"lep2_mass" :  ZZ_lep2_mass,
"lep2_E" :   ZZ_lep2_E,
"lep2_F" : ZZ_lep2_F,
"lep2_C" : ZZ_lep2_C,
"lep3_pt" : ZZ_lep3_pt,
"lep3_eta" : ZZ_lep3_eta,
"lep3_phi" : ZZ_lep3_phi,
"lep3_mass" : ZZ_lep3_mass,
"lep3_E" : ZZ_lep3_E,
"lep3_F" : ZZ_lep3_F,
"lep3_C" : ZZ_lep3_C,
"Pho_pt" : ZZ_Pho_pt,
"Pho_eta" : ZZ_Pho_eta,
"Pho_phi" : ZZ_Pho_phi,
"Pho_E" : ZZ_Pho_E,
"MET_pt" : ZZ_MET_pt,
"MET_phi" : ZZ_MET_phi,
"MT" : ZZ_MT,
"Dilepptsum" : ZZ_Dilepptsum,
"Trilepptsum" : ZZ_Trilepptsum,
"Trilepphoptsum" : ZZ_Trilepphoptsum

})

WWW = ak.zip({

"Dilep_pt" : WWW_Dilep_pt,
"Dilep_mass" : WWW_Dilep_mass,
"Dilep_E" : WWW_Dilep_E,
"Trilep_pt" : WWW_Trilep_pt,
"Trilep_mass" : WWW_Trilep_mass,
"Trilep_E" : WWW_Trilep_E,
"Trileppho_pt" : WWW_Trileppho_pt,
"Trileppho_mass" : WWW_Trileppho_mass,
"Trileppho_E" : WWW_Trileppho_E,
"lep1_pt" : WWW_lep1_pt,
"lep1_eta" : WWW_lep1_eta,
"lep1_phi" : WWW_lep1_phi,
"lep1_mass" : WWW_lep1_mass,
"lep1_E" :   WWW_lep1_E,
"lep1_F" : WWW_lep1_F,
"lep1_C" : WWW_lep1_C,
"lep2_pt" : WWW_lep2_pt,
"lep2_eta" : WWW_lep2_eta,
"lep2_phi" :  WWW_lep2_phi,
"lep2_mass" :  WWW_lep2_mass,
"lep2_E" :   WWW_lep2_E,
"lep2_F" : WWW_lep2_F,
"lep2_C" : WWW_lep2_C,
"lep3_pt" : WWW_lep3_pt,
"lep3_eta" : WWW_lep3_eta,
"lep3_phi" : WWW_lep3_phi,
"lep3_mass" : WWW_lep3_mass,
"lep3_E" : WWW_lep3_E,
"lep3_F" : WWW_lep3_F,
"lep3_C" : WWW_lep3_C,
"Pho_pt" : WWW_Pho_pt,
"Pho_eta" : WWW_Pho_eta,
"Pho_phi" : WWW_Pho_phi,
"Pho_E" : WWW_Pho_E,
"MET_pt" : WWW_MET_pt,
"MET_phi" : WWW_MET_phi,
"MT" : WWW_MT,
"Dilepptsum" : WWW_Dilepptsum,
"Trilepptsum" : WWW_Trilepptsum,
"Trilepphoptsum" : WWW_Trilepphoptsum

})

WWZ = ak.zip({

"Dilep_pt" : WWZ_Dilep_pt,
"Dilep_mass" : WWZ_Dilep_mass,
"Dilep_E" : WWZ_Dilep_E,
"Trilep_pt" : WWZ_Trilep_pt,
"Trilep_mass" : WWZ_Trilep_mass,
"Trilep_E" : WWZ_Trilep_E,
"Trileppho_pt" : WWZ_Trileppho_pt,
"Trileppho_mass" : WWZ_Trileppho_mass,
"Trileppho_E" : WWZ_Trileppho_E,
"lep1_pt" : WWZ_lep1_pt,
"lep1_eta" : WWZ_lep1_eta,
"lep1_phi" : WWZ_lep1_phi,
"lep1_mass" : WWZ_lep1_mass,
"lep1_E" :   WWZ_lep1_E,
"lep1_F" : WWZ_lep1_F,
"lep1_C" : WWZ_lep1_C,
"lep2_pt" : WWZ_lep2_pt,
"lep2_eta" : WWZ_lep2_eta,
"lep2_phi" :  WWZ_lep2_phi,
"lep2_mass" :  WWZ_lep2_mass,
"lep2_E" :   WWZ_lep2_E,
"lep2_F" : WWZ_lep2_F,
"lep2_C" : WWZ_lep2_C,
"lep3_pt" : WWZ_lep3_pt,
"lep3_eta" : WWZ_lep3_eta,
"lep3_phi" : WWZ_lep3_phi,
"lep3_mass" : WWZ_lep3_mass,
"lep3_E" : WWZ_lep3_E,
"lep3_F" : WWZ_lep3_F,
"lep3_C" : WWZ_lep3_C,
"Pho_pt" : WWZ_Pho_pt,
"Pho_eta" : WWZ_Pho_eta,
"Pho_phi" : WWZ_Pho_phi,
"Pho_E" : WWZ_Pho_E,
"MET_pt" : WWZ_MET_pt,
"MET_phi" : WWZ_MET_phi,
"MT" : WWZ_MT,
"Dilepptsum" : WWZ_Dilepptsum,
"Trilepptsum" : WWZ_Trilepptsum,
"Trilepphoptsum" : WWZ_Trilepphoptsum

})

WZZ = ak.zip({

"Dilep_pt" : WZZ_Dilep_pt,
"Dilep_mass" : WZZ_Dilep_mass,
"Dilep_E" : WZZ_Dilep_E,
"Trilep_pt" : WZZ_Trilep_pt,
"Trilep_mass" : WZZ_Trilep_mass,
"Trilep_E" : WZZ_Trilep_E,
"Trileppho_pt" : WZZ_Trileppho_pt,
"Trileppho_mass" : WZZ_Trileppho_mass,
"Trileppho_E" : WZZ_Trileppho_E,
"lep1_pt" : WZZ_lep1_pt,
"lep1_eta" : WZZ_lep1_eta,
"lep1_phi" : WZZ_lep1_phi,
"lep1_mass" : WZZ_lep1_mass,
"lep1_E" :   WZZ_lep1_E,
"lep1_F" : WZZ_lep1_F,
"lep1_C" : WZZ_lep1_C,
"lep2_pt" : WZZ_lep2_pt,
"lep2_eta" : WZZ_lep2_eta,
"lep2_phi" :  WZZ_lep2_phi,
"lep2_mass" :  WZZ_lep2_mass,
"lep2_E" :   WZZ_lep2_E,
"lep2_F" : WZZ_lep2_F,
"lep2_C" : WZZ_lep2_C,
"lep3_pt" : WZZ_lep3_pt,
"lep3_eta" : WZZ_lep3_eta,
"lep3_phi" : WZZ_lep3_phi,
"lep3_mass" : WZZ_lep3_mass,
"lep3_E" : WZZ_lep3_E,
"lep3_F" : WZZ_lep3_F,
"lep3_C" : WZZ_lep3_C,
"Pho_pt" : WZZ_Pho_pt,
"Pho_eta" : WZZ_Pho_eta,
"Pho_phi" : WZZ_Pho_phi,
"Pho_E" : WZZ_Pho_E,
"MET_pt" : WZZ_MET_pt,
"MET_phi" : WZZ_MET_phi,
"MT" : WZZ_MT,
"Dilepptsum" : WZZ_Dilepptsum,
"Trilepptsum" : WZZ_Trilepptsum,
"Trilepphoptsum" : WZZ_Trilepphoptsum

})

ZZZ = ak.zip({

"Dilep_pt" : ZZZ_Dilep_pt,
"Dilep_mass" : ZZZ_Dilep_mass,
"Dilep_E" : ZZZ_Dilep_E,
"Trilep_pt" : ZZZ_Trilep_pt,
"Trilep_mass" : ZZZ_Trilep_mass,
"Trilep_E" : ZZZ_Trilep_E,
"Trileppho_pt" : ZZZ_Trileppho_pt,
"Trileppho_mass" : ZZZ_Trileppho_mass,
"Trileppho_E" : ZZZ_Trileppho_E,
"lep1_pt" : ZZZ_lep1_pt,
"lep1_eta" : ZZZ_lep1_eta,
"lep1_phi" : ZZZ_lep1_phi,
"lep1_mass" : ZZZ_lep1_mass,
"lep1_E" :   ZZZ_lep1_E,
"lep1_F" : ZZZ_lep1_F,
"lep1_C" : ZZZ_lep1_C,
"lep2_pt" : ZZZ_lep2_pt,
"lep2_eta" : ZZZ_lep2_eta,
"lep2_phi" :  ZZZ_lep2_phi,
"lep2_mass" :  ZZZ_lep2_mass,
"lep2_E" :   ZZZ_lep2_E,
"lep2_F" : ZZZ_lep2_F,
"lep2_C" : ZZZ_lep2_C,
"lep3_pt" : ZZZ_lep3_pt,
"lep3_eta" : ZZZ_lep3_eta,
"lep3_phi" : ZZZ_lep3_phi,
"lep3_mass" : ZZZ_lep3_mass,
"lep3_E" : ZZZ_lep3_E,
"lep3_F" : ZZZ_lep3_F,
"lep3_C" : ZZZ_lep3_C,
"Pho_pt" : ZZZ_Pho_pt,
"Pho_eta" : ZZZ_Pho_eta,
"Pho_phi" : ZZZ_Pho_phi,
"Pho_E" : ZZZ_Pho_E,
"MET_pt" : ZZZ_MET_pt,
"MET_phi" : ZZZ_MET_phi,
"MT" : ZZZ_MT,
"Dilepptsum" : ZZZ_Dilepptsum,
"Trilepptsum" : ZZZ_Trilepptsum,
"Trilepphoptsum" : ZZZ_Trilepphoptsum

})

ttbarG = ak.zip({

"Dilep_pt" : ttbarG_Dilep_pt,
"Dilep_mass" : ttbarG_Dilep_mass,
"Dilep_E" : ttbarG_Dilep_E,
"Trilep_pt" : ttbarG_Trilep_pt,
"Trilep_mass" : ttbarG_Trilep_mass,
"Trilep_E" : ttbarG_Trilep_E,
"Trileppho_pt" : ttbarG_Trileppho_pt,
"Trileppho_mass" : ttbarG_Trileppho_mass,
"Trileppho_E" : ttbarG_Trileppho_E,
"lep1_pt" : ttbarG_lep1_pt,
"lep1_eta" : ttbarG_lep1_eta,
"lep1_phi" : ttbarG_lep1_phi,
"lep1_mass" : ttbarG_lep1_mass,
"lep1_E" :   ttbarG_lep1_E,
"lep1_F" : ttbarG_lep1_F,
"lep1_C" : ttbarG_lep1_C,
"lep2_pt" : ttbarG_lep2_pt,
"lep2_eta" : ttbarG_lep2_eta,
"lep2_phi" :  ttbarG_lep2_phi,
"lep2_mass" :  ttbarG_lep2_mass,
"lep2_E" :   ttbarG_lep2_E,
"lep2_F" : ttbarG_lep2_F,
"lep2_C" : ttbarG_lep2_C,
"lep3_pt" : ttbarG_lep3_pt,
"lep3_eta" : ttbarG_lep3_eta,
"lep3_phi" : ttbarG_lep3_phi,
"lep3_mass" : ttbarG_lep3_mass,
"lep3_E" : ttbarG_lep3_E,
"lep3_F" : ttbarG_lep3_F,
"lep3_C" : ttbarG_lep3_C,
"Pho_pt" : ttbarG_Pho_pt,
"Pho_eta" : ttbarG_Pho_eta,
"Pho_phi" : ttbarG_Pho_phi,
"Pho_E" : ttbarG_Pho_E,
"MET_pt" : ttbarG_MET_pt,
"MET_phi" : ttbarG_MET_phi,
"MT" : ttbarG_MT,
"Dilepptsum" : ttbarG_Dilepptsum,
"Trilepptsum" : ttbarG_Trilepptsum,
"Trilepphoptsum" : ttbarG_Trilepphoptsum

})


histo = {}
histo['WZG'] = WZG
histo['WG'] = WG
histo['ZG'] = ZG
histo['WW'] = WW
histo['WZ'] = WZ
histo['ZZ'] = ZZ
histo['WWW'] = WWW
histo['WWZ'] = WWZ
histo['WZZ'] = WZZ
histo['ZZZ'] = ZZZ
histo['ttbarG'] = ttbarG

outname = "emm_channel.npy"

np.save(outname, histo)

print("MUYAHO!")
