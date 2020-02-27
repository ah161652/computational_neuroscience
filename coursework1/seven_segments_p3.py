#for the submission uncomment the submission statements
#so submission.README

from math import *
import numpy as np

from submission import *

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False


    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")

    def vert(d1,d2,d3):
        word=""

        if d1:
            word="|"
        else:
            word=" "

        if d3:
            word+="_"
        else:
            word+=" "

        if d2:
            word+="|"
        else:
            word+=" "

        print(word)


    pattern_b=list(map(to_bool,pattern))

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))


def create_matrix(pattern0, pattern1, pattern2):

    weight_matrix=np.array([[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]], dtype='f')


    for i in range(0,11):
        for j in range(0,11):

            if i==j:
                w=float(0)
                weight_matrix[i][j] = w
            else:
                w = float(1/3*((pattern0[i]*pattern0[j])+(pattern1[i]*pattern1[j])+(pattern2[i]*pattern2[j])))
                weight_matrix[i][j] = w

    print(weight_matrix)
    return(weight_matrix)

def evolve(pattern, matrix, threshold):
    # tmp_pattern = [0]*11
    tmp_pattern = pattern
    for target_neuron in range(0,11):
        output = 0
        for input_neuron in range(0,11):
            output = output + ((matrix[target_neuron][input_neuron]*pattern[input_neuron]))- threshold
        if output>threshold:
            tmp_pattern[target_neuron]=1
        else:
            tmp_pattern[target_neuron]=(-1)
    print(tmp_pattern)
    return(tmp_pattern)


submission=Submission("Aidan Hood")
submission.header("Aidan Hood")

six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(three)
seven_segment(six)
seven_segment(one)

weight_matrix=create_matrix(three,six,one)

##this assumes you have called your weight matrix "weight_matrix"
submission.section("Weight matrix")
submission.matrix_print("W",weight_matrix)

print("test1")
submission.section("Test 1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]

print(test)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)




##this prints a space
submission.qquad()


print("test2")

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]
submission.section("Test 2")

print(test)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)

test = evolve(test,weight_matrix,0)

seven_segment(test)
submission.seven_segment(test)




##this prints a space
submission.qquad()



submission.bottomer()
