import wave
from collections import Counter
from matplotlib import pyplot as plt
from scipy.io import wavfile
import numpy as np



#init golabl variables 
zeros_burst=[]
X_Y_axis=[]
Max_allowed_zeros_burst = 10
Max_allowed_repetitions  = 5
range_X_axis= 500
range_Y_axis= 500



def find_zeroes_burst(data): #create list of zeroes burst
    counter = 0
    for i, value in enumerate(data):
        if (value != 0 and counter==0): # checking if its not end of zeros sequence, FALSE => end of zeros sequence => jump to else , True =>this is not end of a zeros sequence continue to search zeros 
            counter=0
        elif value == 0:   #starting of zeros sequence 
            counter = counter + 1
            if (i == len(data)-1): #last iterations
                zeros_burst.append(counter)
        else:
            zeros_burst.append(counter) #end of zeros sequence
            counter=0
    return (zeros_burst)


def find_X_Y_axis(zeros_burst): # list of tuples [(size of zeros sequence,number of repetitions ), .....]
    count = Counter(zeros_burst)
    X_Y_axis = sorted(count.items(), key=lambda c: c[0])
    return (X_Y_axis)
    
def print_Histogram_of_zeros(X_Y_axis):
    X_Y_axis_range = list(filter(lambda x: x[0] <= range_X_axis, X_Y_axis)) #set x axis range
    x_axis, y_axis = zip(*X_Y_axis_range)
    indices = np.arange(len(X_Y_axis_range))
    plt.bar( indices, y_axis, color='b')
    plt.xticks(indices, x_axis, rotation='vertical')
    plt.tight_layout()
    plt.ylim(0, range_Y_axis)  #set Y axis range
    plt.xlabel("size of a sequence",size=20)
    plt.ylabel("number of repetitions",size=20)
    plt.show()
    
    
def pass_fail():
    MAX=max(X_Y_axis)
    MAX_burst ,MAX_repetitions=MAX[0], MAX[1]
    if ((MAX_burst > Max_allowed_zeros_burst) or (MAX_repetitions > Max_allowed_repetitions )):
        print("FAIL\n") 
    else:
        print("PASS\n")    
    print  ('MAX zeros burst = '+ str(MAX_burst) + ',  number of repetitions = ' + str(MAX_repetitions))
    

#main

help=input("Please enter:  max allowed sequence length, max allowed repetition, X axis range, Y axis range:  (--help for instruction or press enter to continue)\n")
if help=='--help':
    print("enter the requested parameters, for default value press 'enter'")
    print("defaults:  Max_allowed_zeros_burst = 10 , Max_allowed_repetitions  = 5 , range_X_axis= 500  ,range_Y_axis= 500" )

Max_allowed_zeros_burst,Max_allowed_repetitions ,range_X_axis,range_Y_axis=int(input("Max_allowed_zeros_burst: ") or Max_allowed_zeros_burst),int(input("Max_allowed_repetitions : ") or Max_allowed_repetitions ),int(input("range_X_axis: ") or range_X_axis),int(input("range_Y_axis: ") or range_Y_axis)
print ('running: ' + 'Max_allowed_zeros_burst = ' + str(Max_allowed_zeros_burst) + ',   Max_allowed_repetitions  = ' + str(Max_allowed_repetitions ) +  ',  range_X_axis = ' + str(range_X_axis)  +   ',   range_Y_axis = ' + str(range_Y_axis) + '\n')

samplerate, data = wavfile.read('in.wav')
zeros_burst=find_zeroes_burst(data)
X_Y_axis=find_X_Y_axis(zeros_burst)
pass_fail()
print_Histogram_of_zeros(X_Y_axis)





