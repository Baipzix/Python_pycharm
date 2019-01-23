import numpy as np
import pandas as pd
from numpy import genfromtxt


def safety_score(emg,stu):
    ss=np.zeros(len(emg))

    ss[np.logical_and(emg=="No", stu=="No")]=0
    ss[np.logical_and(emg=="No", stu=="Potential")] = 10
    ss[np.logical_and(emg=="No" , stu=="Yes")] = 20

    ss[np.logical_and(emg=="Potential", stu=="No")]=20
    ss[np.logical_and(emg=="Potential", stu=="Potential")] = 20
    ss[np.logical_and(emg=="Potential" , stu=="Yes")] = 30

    ss[np.logical_and(emg=="Yes", stu=="No")]=20
    ss[np.logical_and(emg=="Yes", stu=="Potential")] = 30
    ss[np.logical_and(emg=="Yes" , stu=="Yes")] = 40
    return ss
def erosion_score(ero,de,sed):
    ss=np.zeros(len(ero))

    ss[np.logical_and(ero=="No", sed=="No")]=0
    ss[np.logical_and(np.logical_or(ero=='Potential', ero=='Yes'), de=="Low", sed == "No")] = 5
    ss[np.logical_and(np.logical_or(ero == 'Potential', ero == 'Yes'), de == "High-Unsatisfactory", sed == "No")] = 10

    ss[np.logical_and(ero=="No", sed=="Potential")]=5
    ss[np.logical_and(np.logical_or(ero=='Potential', ero=='Yes'), de=="Low", sed == "Potential")] = 10
    ss[np.logical_and(np.logical_or(ero == 'Potential', ero == 'Yes'), de == "High-Unsatisfactory", sed == "Potential")] = 15

    ss[np.logical_and(ero=="No", sed=="Yes")]=10
    ss[np.logical_and(np.logical_or(ero=='Potential', ero=='Yes'), de=="Low", sed == "Yes")] = 15
    ss[np.logical_and(np.logical_or(ero == 'Potential', ero == 'Yes'), de == "High-Unsatisfactory", sed == "Yes")] = 20
    return ss
def fish_score(fish, block):
    fs=np.zeros(len(fish))

    fs[np.logical_and(fish=="No Concerns", block=="No")]=0
    fs[np.logical_and(fish == "No Concerns", np.logical_or(block=='Potential', block=='Yes'))] = 5

    fs[np.logical_and(fish == "Some Concerns", block == "No")] = 15
    fs[np.logical_and(fish == "Some Concerns", np.logical_or(block == 'Potential', block == 'Yes'))] = 20

    fs[np.logical_and(fish == "Serious Concerns", block == "No")] = 30
    fs[np.logical_and(fish == "Serious Concerns", np.logical_or(block == 'Potential', block == 'Yes'))] = 40

    return fs


csvfile=r"C:\SCARI\ScariData.csv"

scarip=pd.read_csv(csvfile,sep=',',header=0)
print(scarip[0:3])


sLen=len(scarip["ID"])

scarip["SAFETY"]=pd.Series(np.zeros(sLen),index=scarip.index)
scarip["EROSION_SCORE"]=pd.Series(np.zeros(sLen),index=scarip.index)
scarip["FISH"]=pd.Series(np.zeros(sLen),index=scarip.index)

print(sLen)
scarip["RISKFACTOR2"]=pd.Series(np.zeros(sLen),index=scarip.index)

sn=np.array(scarip)


scarip["SAFETY"]=safety_score(sn[:,10],sn[:,11])
scarip["EROSION_SCORE"]=erosion_score(sn[:,6],sn[:,7],sn[:,12])
scarip["FISH"]=fish_score(sn[:,9],sn[:,8])
scarip["RISKFACTOR"]=scarip["SAFETY"]+scarip["EROSION_SCORE"]+scarip["FISH"]

scarip["RISKFACTOR2"]=scarip["SAFETY"]*0.4+scarip["EROSION_SCORE"]*0.2+scarip["FISH"]*0.4
print("========")
print(type(sn[:,10]))
print(scarip["EROSION_DE"].values)

scarip["SAFETY2"]=safety_score(scarip["EMG_REP_RE"].values, scarip["STU_PROBS"].values)
erosion2=erosion_score(scarip["EROSION"].values,scarip["EROSION_DE"].values, scarip["SEDEMENTAT"].values)
fish2=fish_score(scarip["FISH_PCONC"].values, scarip["BLOCKAGE"].values)
scarip["risk_2"]=erosion2+fish2

scarip.to_csv(r"C:\SCARI\ScariOut.csv", sep=',', index=False)