# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 07:33:02 2011

@author: Jeff

This script calculates brine salinity and the concentration factor for ice 
between 0 and -30 according to the equations of cox and weeks.  If volume to add
is negative, do not add any melt solution and disregard dilution factor
in log sheet.  

Before using this program you will need to change the output directory to one
that exists on your machine and input the salinity of your melting solution 
(S_brine).  The program will tell you what volume to add to reach your desired 
final salinity or an isohaline melt.  Simply follow the prompts.

You will receive this information and more in a log sheet in the directory
you specified.  Log output is in order time, sample ID, T, S, M, in situ 
brine salinity, in situ concentration factor, ice volume (melted), brine 
volume added, dilution factor.

To run the program you should have python installed.  Place this file with 
your other executables and execute from command line, or place in any directory,
navigate to it from command line, and execute.

"""

from time import localtime, strftime

S_brine=250 #salinity of brine used for melting
print("your currently selected brine salinity is", S_brine)
print("Enter T")
T=float(input('T=')) #temp
print("Enter bulk salinity")
S=float(input('S=')) #bulk salinity of ice
print("Enter sample mass in kg")
M=float(input('Mass=')) #sample mass
print("Enter sample ID")
sample_ID=(input('Sample ID=')) #input the ID of the sample

#Determine brine salinity for temperature indicated

if 0>T>=-2:
    brine_salinity=-3.9921-22.7*T-1.0015*pow(T,2)-0.019956*pow(T,3)
elif -2>T>-23:
    brine_salinity=-3.9921-22.7*T-1.0015*pow(T,2)-0.019956*pow(T,3)
elif T<=-23:
    brine_salinity=206.24-1.8907*T-0.060868*pow(T,2)-0.001024*pow(T,3)

#Determine target salinity, either user defined or isohaline

print("Enter target salinity, enter iso for isohaline melt")
S_target=input('target salinity=')
if S_target=="iso":
    S_target=brine_salinity
else:
    S_target=float(S_target)

output=open('/Users/Jeff/Documents/deming_lab/Antarctica/sample_volumes_test.txt', "a")

if 0>T>=-2:
    density_ice=0.917-0.0001403*T
    V_ice=M*density_ice
    F_1=0.041221-18.407*T+0.58402*pow(T,2)+0.21454*pow(T,3)
    F_2=0.090312-0.016111*T+0.00012291*pow(T,2)+0.00013603*pow(T,3)
    brine_volume=S*density_ice/(F_1-(S-density_ice*F_2)) #in situ brine volume
    conc_factor=1/brine_volume
    brine_salinity=-3.9921-22.7*T-1.0015*pow(T,2)-0.019956*pow(T,3)
    V_brine=(V_ice*(S-S_target))/(S_target-S_brine) #volume of melting brine added
    dilution_factor=(V_brine+V_ice)/V_ice
    time=strftime("%d %b %Y %H:%M:%S", localtime())
    print("brine salinity is", brine_salinity)
    print("add", V_brine, "L to reach", S_target, "ppt in final melt")
    print(time, sample_ID, T, S, M, brine_salinity, conc_factor, V_ice, V_brine, dilution_factor, file=output)

elif -2>T>-23:
    density_ice=0.917-0.0001403*T
    V_ice=M*density_ice
    F_1=-4.732-22.45*T-0.6397*pow(T,2)-0.01074*pow(T,3)
    F_2=0.090312-0.016111*T+0.00012291*pow(T,2)+0.00013603*pow(T,3)
    brine_volume=S*density_ice/(F_1-(S-density_ice*F_2))
    conc_factor=1/brine_volume
    brine_salinity=-3.9921-22.7*T-1.0015*pow(T,2)-0.019956*pow(T,3)
    V_brine=(V_ice*(S-S_target))/(S_target-S_brine) #volume of melting brine added
    dilution_factor=(V_brine+V_ice)/V_ice
    time=strftime("%d %b %Y %H:%M:%S", localtime())
    print("brine salinity is", brine_salinity)
    print("add", V_brine, "L to reach", S_target, "ppt in final melt")
    print(time, sample_ID, T, S, M, brine_salinity, conc_factor, V_ice, V_brine, dilution_factor, file=output)

elif T<=-23:
    density_ice=0.917-0.0001403*T
    V_ice=M*density_ice
    F_1=9899+1309*T+55.27*pow(T,2)+0.716*pow(T,3)
    F_2=8.547+1.089*T+0.04518*pow(T,2)+0.0005819*pow(T,3)
    brine_volume=S*density_ice/(F_1-(S-density_ice*F_2))
    conc_factor=1/brine_volume
    brine_salinity=206.24-1.8907*T-0.060868*pow(T,2)-0.001024*pow(T,3)
    V_brine=(V_ice*(S-S_target))/(S_target-S_brine) #volume of melting brine added
    dilution_factor=(V_brine+V_ice)/V_ice
    time=strftime("%d %b %Y %H:%M:%S", localtime())
    print("brine salinity is", brine_salinity)
    print("add", V_brine, "L to reach", S_target, "ppt in final melt")
    print(time, sample_ID, T, S, M, brine_salinity, conc_factor, V_ice, V_brine, dilution_factor, file=output)

else:
    print("Temperature is out of range")
    
output.close()

