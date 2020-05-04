import random as rnd
import statistics
import math
import matplotlib.pyplot as plt
import numpy as np



def load_data(filename,T):

    data_array = [T(line.strip()) for line in open(filename, 'r')]

    return data_array

def get_spike_train(rate,big_t,tau_ref):

    if 1<=rate*tau_ref:
        print("firing rate not possible given refractory period f/p")
        return []


    exp_rate=rate/(1-tau_ref*rate)

    spike_train=[]

    t=rnd.expovariate(exp_rate)

    while t< big_t:
        spike_train.append(t)
        t+=tau_ref+rnd.expovariate(exp_rate)

    return spike_train


def spike_count(interval,big_t,ms,spike_train):

    array = []
    min = 0
    max = interval*ms
    n_intervals = int(math.ceil(big_t/(interval*ms)))


    for x in range(n_intervals):

        running_count =0

        for i in spike_train:
            if i>min and i<max:
                running_count = running_count +1

        array.append(running_count)

        min = min + (interval*ms)
        max = max = max + (interval*ms)

    return array

def spike_intervals(spike_train):
    array =[]

    for x in range(len(spike_train)-1):
        array.append(spike_train[x+1]-spike_train[x])
    return array

def convert(spikes):
    array = []
    index = 0;

    for i in spikes:
        if i == 1:
            array.append(2*0.001*index)
            index = index +1

        else:
            index = index+1


    return array






Hz=1.0
sec=1.0
ms=0.001





###################################
###################################
#############Q1####################
###################################
###################################

rate=35 *Hz
tau_ref=0*ms
big_t=1000*sec

spike_train=get_spike_train(rate,big_t,tau_ref)

print("0ms refractory period:")

interval_10 = spike_count(10, big_t, ms, spike_train)
variance_10 = statistics.variance(interval_10)
average_10 = statistics.mean(interval_10)
fano_10 = variance_10/average_10
print("Fano Factor with 10ms interval:")
print(fano_10)

interval_50 = spike_count(50, big_t, ms, spike_train)
variance_50 = statistics.variance(interval_50)
average_50 = statistics.mean(interval_50)
fano_50 = variance_50/average_50
print("Fano Factor with 50ms interval:")
print(fano_50)

interval_100 = spike_count(100, big_t, ms, spike_train)
variance_100 = statistics.variance(interval_100)
average_100 = statistics.mean(interval_100)
fano_100 = variance_100/average_100
print("Fano Factor with 100ms interval:")
print(fano_100)

intervals =spike_intervals(spike_train)
s_dev = statistics.stdev(intervals)
av = statistics.mean(intervals)
v_coeff = s_dev/av
print("Coefficient of deviation:")
print(v_coeff)





rate=35 *Hz
tau_ref=5*ms
big_t=1000*sec

spike_train=get_spike_train(rate,big_t,tau_ref)

print("5ms refractory period:")

interval_10 = spike_count(10, big_t, ms, spike_train)
variance_10 = statistics.variance(interval_10)
average_10 = statistics.mean(interval_10)
fano_10 = variance_10/average_10
print("Fano Factor with 10ms interval:")
print(fano_10)

interval_50 = spike_count(50, big_t, ms, spike_train)
variance_50 = statistics.variance(interval_50)
average_50 = statistics.mean(interval_50)
fano_50 = variance_50/average_50
print("Fano Factor with 50ms interval:")
print(fano_50)

interval_100 = spike_count(100, big_t, ms, spike_train)
variance_100 = statistics.variance(interval_100)
average_100 = statistics.mean(interval_100)
fano_100 = variance_100/average_100
print("Fano Factor with 100ms interval:")
print(fano_100)

intervals =spike_intervals(spike_train)
s_dev = statistics.stdev(intervals)
av = statistics.mean(intervals)
v_coeff = s_dev/av
print("Coefficient of deviation:")
print(v_coeff)



###################################
###################################
#############Q2####################
###################################
###################################

rate=500 *Hz
tau_ref=0*ms
big_t=1200*sec



spikes=load_data("rho.dat",int)

train = convert(spikes)


print("For Q2 loaded Data:")

interval_10 = spike_count(10, big_t, ms, train)
variance_10 = statistics.variance(interval_10)
average_10 = statistics.mean(interval_10)
fano_10 = variance_10/average_10
print("Fano Factor with 10ms interval:")
print(fano_10)

interval_50 = spike_count(50, big_t, ms, train)
variance_50 = statistics.variance(interval_50)
average_50 = statistics.mean(interval_50)
fano_50 = variance_50/average_50
print("Fano Factor with 50ms interval:")
print(fano_50)

interval_100 = spike_count(100, big_t, ms, train)
variance_100 = statistics.variance(interval_100)
average_100 = statistics.mean(interval_100)
fano_100 = variance_100/average_100
print("Fano Factor with 100ms interval:")
print(fano_100)

intervals =spike_intervals(train)
s_dev = statistics.stdev(intervals)
av = statistics.mean(intervals)
v_coeff = s_dev/av
print("Coefficient of deviation:")
print(v_coeff)





###################################
###################################
#############Q3####################
###################################
###################################

array = [0.0]*51
n_spikes = spikes.count(1)

for i in range(0, len(spikes)):
    if spikes[i] == 1:
        for j in range(0,51):
            try:
                if(spikes[i+j] == 1):
                    array[j] = array[j] + 1
            except IndexError:
                pass
            continue

array_y_2 = [float(x / n_spikes) for x in array]
array_y_1 = array_y_2[::-1]
array_y_2.pop(0)
array_y = array_y_1+array_y_2;

array_x = [x*2 for x in range(int(0.5*-100),int(math.ceil(0.5*101)))]


plt.plot(array_x,array_y)
plt.xlabel("Interval (ms)")
plt.ylabel("Normalized Autocorrelation")
plt.title("Question 3 Autocorrelogram for Rho Spike Train Data")
plt.show()




###################################
###################################
#############Q4####################
###################################
###################################

stimulus=load_data("stim.dat",float)

array = [0.0]*51
n_spikes = spikes.count(1)

for i in range(0, len(spikes)):
    if spikes[i] == 1:
        for j in range(0,51):
            try:
                    array[j] = array[j] + stimulus[i-j]
            except IndexError:
                pass
            continue

array_y = [float(x / n_spikes) for x in array]
array_y = array_y[::-1]


array_x = [x*2 for x in range(int(0.5*-100),int(1))]


plt.plot(array_x,array_y)
plt.xlabel("Time (ms)")
plt.ylabel("Spike Triggered Average")
plt.title("Question 4 Spike Triggered Average")
plt.show()
