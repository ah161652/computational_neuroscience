import random
import statistics
import math
import matplotlib.pyplot as plt
import numpy as np




#############################
#############################
#########PART A Q1###########
#############################
#############################


# #Variables
# tau_m = 0.01
# el = -0.07
# vr = -0.07
# vt = -0.04
# rm = 10000000
# timestep = 0.00025
# ie = 0.0000000031
#
# #Arrays
# times = [0]*4000
# voltages = [0]*4000
#
# #Set intial time and voltage
# times[0] = 0
# voltages[0]= vr
#
#
# #Compute all voltages via Euler Method
# for i in range(1, len(voltages)):
#
#     if voltages[i-1] >= vt:
#         voltages[i] = vr
#         times[i] = times[i-1]+timestep
#
#     else:
#         voltages[i] = voltages[i-1] + timestep*(((el-voltages[i-1])+(rm*ie))/tau_m)
#         times[i] = times[i-1] + timestep
#
#
# #Plot graph
# plt.plot(times,voltages, label = "Integrate and Fire Neuron Membrane Potential")
# plt.xlabel("Time (s)")
# plt.ylabel("Voltage (V)")
# plt.title("Question 1 Integrate and Fire Neuron Model")
# plt.legend(loc=2)
# plt.show()





# ##############################
# ##############################
# ##########PART A Q2###########
# ##############################
# ##############################
#
#
#neuron variables
tau_m = 0.02
el = -0.07
vr = -0.08
vt = -0.054
rmie = 0.018
timestep = 0.00025


#synapse variables - es = -0.08 for inhibitory, 0 for excitory
# es = -0.08
es = 0
tau_s = 0.01
rmgs = 0.15
s1 = 0
s2 = 0

#Effects on each neuron
rmis_1_to_2 = 0
rmis_2_to_1 = 0


#arrays
times = [0]*4000
voltages1 = [0]*4000
voltages2 = [0]*4000

# Set intial potentials to random float between rest and thresh
voltages1[0] = random.uniform(vr,vt)
voltages2[0] = random.uniform(vr,vt)


#Compute all voltages
for i in range(1, len(voltages1)):

    # Calculate rmis for each synapse
    rmis_1_to_2 = rmgs*s2*(es-voltages2[i-1])
    rmis_2_to_1 = rmgs*s1*(es-voltages1[i-1])

    #Use the rmis' and euler's method to calculate next potential for each neuron
    voltages1[i] = voltages1[i-1] + timestep*(((el-voltages1[i-1])+rmie+rmis_2_to_1)/tau_m)
    voltages2[i] = voltages2[i-1] + timestep*(((el-voltages2[i-1])+rmie+rmis_1_to_2)/tau_m)

    #Neuron1:
    #if potential over thesh then set to reset and use euler's method to find next s2 ( +0.5 because it is spiking)
    if voltages1[i] >= vt:
        voltages1[i] = vr
        s2 = s2 + (timestep * -s2 /tau_s) + 0.5
    # otherwise use euker's method to find next s2, without +0.5 because no spike
    else:
        s2 = s2 + (timestep * -s2 /tau_s)




    #Neuron2:
    #if potential over thesh then set to reset and use euler's method to find next s1 ( +0.5 because it is spiking)
    if voltages2[i] >= vt:
        voltages2[i] = vr
        s1 = s1 + (timestep * -s1 /tau_s) + 0.5
    # otherwise use euker's method to find next s1, without +0.5 because no spike
    else:
        s1 = s1 + (timestep * -s1 /tau_s)

    #increment time by timestep
    times[i] = times[i-1] + timestep



#Plot graph
plt.plot(times,voltages1, 'g', label = 'Neuron 1 Membrane Potential')
plt.plot(times,voltages2, 'r', label = 'Neuron 2 Membrane Potential')
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Question 2 Integrate and Fire Neuron Model with Synapses")
plt.legend(loc=2)
plt.show()
