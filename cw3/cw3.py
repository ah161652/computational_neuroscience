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


#Variables
tau_m = 0.01
el = -0.07
vr = -0.07
vt = -0.04
rm = 10000000
timestep = 0.00025
ie = 0.0000000031

#Arrays
times = [0]*4000
voltages = [0]*4000

#Set intial time and voltage
times[0] = 0
voltages[0]= vr


#Compute all voltages via Euler Method
for i in range(1, len(voltages)):

    if voltages[i-1] >= vt:
        voltages[i] = vr
        times[i] = times[i-1]+timestep

    else:
        voltages[i] = voltages[i-1] + timestep*(((el-voltages[i-1])+(rm*ie))/tau_m)
        times[i] = times[i-1] + timestep


#Plot graph
plt.plot(times,voltages, label = "Integrate and Fire Neuron Membrane Potential")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Question 1 Integrate and Fire Neuron Model")
plt.legend(loc=2)
plt.show()





##############################
##############################
##########PART A Q2###########
##############################
##############################

#neuron variables
tau_m = 0.02
el = -0.07
vr = -0.08
vt = -0.054
rmie = 0.018
timestep = 0.00025


#synapse variables - es = -0.08 for inhibitory, 0 for excitory
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




##############################
##############################
##########PART B Q1###########
##############################
##############################



#Variables
tau_m = 0.01
el = -0.065
vr = -0.065
vt = -0.05
rm = 100000000
ie = 0.0000000001
timestep = 0.00025

#synapse variables
tau_s = 0.002
g = [0.000000004]*40
es = 0
delta_s = 0.5
s = [0]*40


#Arrays
times = [0]*4000
voltages = [0]*4000

#Set intial time and voltage
times[0] = 0
voltages[0]= vr

#Rmis and rmgs arrays
rmis = [0]*40
rmgs = [0]*40

# set input firing rate and intial spike count
r = 15
neuron_spike_count = 0

#Compute all voltages
for i in range(1, len(voltages)):

    for x in range(0,len(rmgs)):
        rmgs[x] = rm *g[x]

    # Calculate rmis for each synapse
    for x in range(0,len(rmis)):
        rmis[x] = rmgs[x]*s[x]*(es-voltages[i-1])


    #Use the rmis' and euler's method to calculate next potential
    voltages[i] = voltages[i-1] + timestep*(((el-voltages[i-1])+sum(rmis))/tau_m)


    #if potential over thesh then set to reset and use euler's method to find next s2 ( +0.5 because it is spiking)
    if voltages[i] >= vt:
        voltages[i] = vr
        neuron_spike_count = neuron_spike_count  + 1

    #For each synapse, generate wether its spiking or not, and update s accordingly
    for x in range(0, len(s)):
        rnd = random.uniform(0,1)

        if rnd < r*timestep:
            s[x] = s[x] + (timestep * -s[x] /tau_s) + delta_s
        else:
            s[x] = s[x] + (timestep * -s[x] /tau_s)



    #increment time by timestep
    times[i] = times[i-1] + timestep


#Plot graph
plt.plot(times,voltages, 'g', label = 'Neuron Voltage')
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Question 1 Integrate and Fire Neuron Voltage with 40 Input Synapses")
plt.legend(loc=2)
plt.show()


##############################
##############################
##########PART B Q2###########
##############################
##############################

#New variables for STDP
t_pre = [-1000]*40
t_post = -1000
delta_t = [0]*40
f_delta_t = [0]*40
A_plus = 0.0000000002
A_minus = 0.00000000025
tau_plus = 0.02
tau_minus = 0.02
stdp = True


#Variables
tau_m = 0.01
el = -0.065
vr = -0.065
vt = -0.05
rm = 100000000
ie = 0.0000000001
timestep = 0.00025
rmis = [0]*40
rmgs = [0]*40
r = 15
neuron_spike_count = 0
spike_count_averages = [float(0)]*30
average_index = 0

#synapse variables
tau_s = 0.002
g = [0.000000004]*40
es = 0
delta_s = 0.5
s = [0]*40


#Arrays
times = [0]*1200000
voltages = [0]*1200000

#Set intial time and voltage
times[0] = 0
voltages[0]= vr


#Compute all voltages
for i in range(1, len(voltages)):

    #increment time by timestep
    times[i] = times[i-1] + timestep

    for x in range(0,len(rmgs)):
        rmgs[x] = rm *g[x]

    # Calculate rmis for each synapse
    for x in range(0,len(rmis)):
        rmis[x] = rmgs[x]*s[x]*(es-voltages[i-1])


    #Use the rmis' and euler's method to calculate next potential
    voltages[i] = voltages[i-1] + timestep*(((el-voltages[i-1])+sum(rmis))/tau_m)


    #Neuron Code
    if voltages[i] >= vt:
        voltages[i] = vr
        neuron_spike_count = neuron_spike_count  + 1

        if(stdp == True):
            t_post = times[i]
            for x in range(0, len(s)):
                delta_t[x] = t_post - t_pre[x]
                f_delta_t[x] = A_plus*math.exp((-1)*abs(delta_t[x]/tau_plus))
                g[x] = g[x] + f_delta_t[x]
                if (g[x]<0):
                    g[x] = 0
                if (g[x]>0.000000004):
                    g[x] = 0.000000004


    #Synapse code
    for x in range(0, len(s)):
        rnd = random.uniform(0,1)

        if rnd < r*timestep:
            s[x] = s[x] + (timestep * -s[x] /tau_s) + delta_s

            if(stdp == True):
                t_pre[x] = times[i]
                delta_t[x] = t_post - t_pre[x]
                f_delta_t[x] = (-1)*A_minus*math.exp((-1)*abs(delta_t[x]/tau_minus))
                g[x] = g[x] + f_delta_t[x]
                if (g[x]<0):
                    g[x] = 0
                if (g[x]>0.000000004):
                    g[x] = 0.000000004

        else:
            s[x] = s[x] + (timestep * -s[x] /tau_s)


    #Code to calculate average spike counts in 10s intervals
    if i%40000 == 0:
        spike_count_averages[average_index] = float(float(neuron_spike_count)/float(10))
        average_index = average_index+1
        neuron_spike_count = 0


average_g = statistics.mean(g)
g_nano = [x*pow(10,9) for x in g]
steady_average_firing_rate = (spike_count_averages[-1] + spike_count_averages[-2] + spike_count_averages[-3])/3


#Plot histogram
plt.hist(g_nano, bins = 'auto')
plt.xlabel("Synaptic Weight (nS)")
plt.ylabel("Frequency")
plt.title("Question 2 Synaptic Weights with STDP On")
plt.legend(loc=2)
plt.show()

times_10s = range(0,30)

#Plot graph
plt.plot(times_10s,spike_count_averages, 'g', label = 'Postsynaptic Neuron Average Firing Rate')
plt.xlabel("Time in 10 s intervals")
plt.ylabel("Firing Rate (Hz)")
plt.title("Question 2 Integrate and Fire Neuron Firing Rate")
plt.legend(loc=2)
plt.show()



##############################
##############################
##########PART B Q3###########
##############################
##############################



t_pre = [-1000]*40
t_post = -1000
delta_t = [0]*40
f_delta_t = [0]*40
A_plus = 0.0000000002
A_minus = 0.00000000025
tau_plus = 0.02
tau_minus = 0.02


#Variables
tau_m = 0.01
el = -0.065
vr = -0.065
vt = -0.05
rm = 100000000
ie = 0.0000000001
timestep = 0.00025

#synapse variables
tau_s = 0.002
g = [0.000000004]*40
es = 0
delta_s = 0.5
s = [0]*40


#Arrays
times = [0]*1200000
voltages = [0]*1200000

#Set intial time and voltage
times[0] = 0
voltages[0]= vr

rmis = [0]*40
rmgs = [0]*40

r = 10

neuron_spike_count = 0

spike_count_averages = [float(0)]*30
average_index = 0

stdp = True

#Compute all voltages
for i in range(1, len(voltages)):

    #increment time by timestep
    times[i] = times[i-1] + timestep

    for x in range(0,len(rmgs)):
        rmgs[x] = rm *g[x]

    # Calculate rmis for each synapse
    for x in range(0,len(rmis)):
        rmis[x] = rmgs[x]*s[x]*(es-voltages[i-1])


    #Use the rmis' and euler's method to calculate next potential
    voltages[i] = voltages[i-1] + timestep*(((el-voltages[i-1])+sum(rmis))/tau_m)


    #neuron code
    if voltages[i] >= vt:
        voltages[i] = vr
        neuron_spike_count = neuron_spike_count  + 1



        if(stdp == True):
            t_post = times[i]
            for x in range(0, len(s)):
                delta_t[x] = t_post - t_pre[x]
                f_delta_t[x] = A_plus*math.exp((-1)*abs(delta_t[x]/tau_plus))
                g[x] = g[x] + f_delta_t[x]
                if (g[x]<0):
                    g[x] = 0
                if (g[x]>0.000000004):
                    g[x] = 0.000000004


    #synapse code
    for x in range(0, len(s)):
        rnd = random.uniform(0,1)

        if rnd < r*timestep:
            s[x] = s[x] + (timestep * -s[x] /tau_s) + delta_s

            if(stdp == True):
                t_pre[x] = times[i]
                delta_t[x] = t_post - t_pre[x]
                f_delta_t[x] = (-1)*A_minus*math.exp((-1)*abs(delta_t[x]/tau_minus))
                g[x] = g[x] + f_delta_t[x]
                if (g[x]<0):
                    g[x] = 0
                if (g[x]>0.000000004):
                    g[x] = 0.000000004

        else:
            s[x] = s[x] + (timestep * -s[x] /tau_s)


    if i%40000 == 0:
        spike_count_averages[average_index] = float(float(neuron_spike_count)/float(10))
        average_index = average_index+1
        neuron_spike_count = 0



g_nano = [x*pow(10,9) for x in g]

steady_average_firing_rate = (spike_count_averages[-1] + spike_count_averages[-2] + spike_count_averages[-3])/3

input_list = [10,11,12,13,14,15,16,17,18,19,20]
output_list_STDP_ON = [0.23,0.17,0.067,0.1,0.13,0.1,0.1,0.033,0,0,0.033]
output_list_STDP_OFF = [1.9,3,3.53,7.67,10.97,14.07,17.9,21.93,25.53,29.87,34.53]


# Plot graphs
plt.plot(input_list,output_list_STDP_ON, 'g')
plt.xlabel("Input Firing Rate (Hz)")
plt.ylabel("Steady-State Output Firing Rate (Hz)")
plt.title("Question 3 Steady-State Output Firing Rate as a Function of Input Firing Rate with STDP On")
plt.legend(loc=2)
plt.show()

plt.plot(input_list,output_list_STDP_OFF, 'g')
plt.xlabel("Input Firing Rate (Hz)")
plt.ylabel("Steady-State Output Firing Rate (Hz)")
plt.title("Question 3 Steady-State Output Firing Rate as a Function of Input Firing Rate with STDP Off")
plt.legend(loc=2)
plt.show()

# Plot histograms
plt.hist(g_nano, bins = 'auto')
plt.xlabel("Synaptic Weight (nS)")
plt.ylabel("Frequency")
plt.title("Question 3 Synaptic Weights")
plt.legend(loc=2)
plt.show()



##############################
##############################
##########PART B Q4###########
##############################
##############################




t_pre = [-1000]*40
t_post = -1000
delta_t = [0]*40
f_delta_t = [0]*40
A_plus = 0.0000000002
A_minus = 0.00000000025
tau_plus = 0.02
tau_minus = 0.02


#Variables
tau_m = 0.01
el = -0.065
vr = -0.065
vt = -0.05
rm = 100000000
ie = 0.0000000001
timestep = 0.00025

#synapse variables
tau_s = 0.002
g = [0.000000004]*40
es = 0
delta_s = 0.5
s = [0]*40


#Arrays
times = [0]*1200000
voltages = [0]*1200000

#Set intial time and voltage
times[0] = 0
voltages[0]= vr

rmis = [0]*40
rmgs = [0]*40

r0 = 20
f=10
B = 20
r = r0 + B*math.sin(2*math.pi*f*0)

neuron_spike_count = 0

spike_count_averages = [float(0)]*30
average_index = 0

stdp = True

#Compute all voltages
for i in range(1, len(voltages)):

    #increment time by timestep
    times[i] = times[i-1] + timestep

    r = r0 + B*math.sin(2*math.pi*f*times[i])

    for x in range(0,len(rmgs)):
        rmgs[x] = rm *g[x]

    # Calculate rmis for each synapse
    for x in range(0,len(rmis)):
        rmis[x] = rmgs[x]*s[x]*(es-voltages[i-1])


    #Use the rmis' and euler's method to calculate next potential
    voltages[i] = voltages[i-1] + timestep*(((el-voltages[i-1])+sum(rmis))/tau_m)


    #if potential over thesh then set to reset
    if voltages[i] >= vt:
        voltages[i] = vr
        neuron_spike_count = neuron_spike_count  + 1



        if(stdp == True):
            t_post = times[i]
            for x in range(0, len(s)):
                delta_t[x] = t_post - t_pre[x]
                f_delta_t[x] = A_plus*math.exp((-1)*abs(delta_t[x]/tau_plus))
                g[x] = g[x] + f_delta_t[x]
                if (g[x]<0):
                    g[x] = 0
                if (g[x]>0.000000004):
                    g[x] = 0.000000004


    for x in range(0, len(s)):
        rnd = random.uniform(0,1)

        if rnd < r*timestep:
            s[x] = s[x] + (timestep * -s[x] /tau_s) + delta_s

            if(stdp == True):
                t_pre[x] = times[i]
                delta_t[x] = t_post - t_pre[x]
                f_delta_t[x] = (-1)*A_minus*math.exp((-1)*abs(delta_t[x]/tau_minus))
                g[x] = g[x] + f_delta_t[x]
                if (g[x]<0):
                    g[x] = 0
                if (g[x]>0.000000004):
                    g[x] = 0.000000004

        else:
            s[x] = s[x] + (timestep * -s[x] /tau_s)

    if i%40000 == 0:
        spike_count_averages[average_index] = float(float(neuron_spike_count)/float(10))
        average_index = average_index+1
        neuron_spike_count = 0

average_g = statistics.mean(g)


standard_dev_g = statistics.stdev(g)


g_nano = [x*pow(10,9) for x in g]

steady_average_firing_rate = (spike_count_averages[-1] + spike_count_averages[-2] + spike_count_averages[-3])/3



input_list = [0,5,10,15,20]
mean_list = [1.40,1.26,1.22,3.60,3.82]
stdev_list = [1.36,1.43,1.25,0.48,0.22]



# Plot graphs
plt.plot(input_list,mean_list, 'g')
plt.xlabel("B (Hz)")
plt.ylabel("Steady-State Synaptic Strength Mean (nS)")
plt.title("Question 4 Steady-State Synaptic Strength Mean as a Function of B")
plt.legend(loc=2)
plt.show()

plt.plot(input_list,stdev_list, 'g')
plt.xlabel("B (Hz)")
plt.ylabel("Steady-State Synaptic Strength Standard Deviation (nS)")
plt.title("Question 4 Steady-State Synaptic Strength Standard Deviation as a Function of B")
plt.legend(loc=2)
plt.show()


#Plot histograms
plt.hist(g_nano, bins = 'auto')
plt.xlabel("Synaptic Weight (nS)")
plt.ylabel("Frequency")
plt.title("Question 4 Synaptic Weights")
plt.legend(loc=2)
plt.show()
