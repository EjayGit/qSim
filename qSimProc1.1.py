"""

"""

import numpy as np
import random
import math

isq2 = 1.0/(2.0**0.5)
ket0 = np.array([[1],
                 [0]], dtype=complex) # to be made zeros(2,1) with dtype=complex at next iteration

# Request the number of inputs 
print("Input the number of qubits:")
qubits = int(input())

# Create list of qubits set to Ket0
qStates = []
for qubit in range(qubits):
    qStates.append(ket0)

'''
Init opsList in which:

opsList = [ gateType , gateType , ... , gateType ]

gateType = [ qubitNum1 , qubitNum2, ... , qubitNumX ]

e.g.: opsList = [ gateType = [ [ gateInput ] , [ qubitNum1 , qubitNum2 ] ], [ [ gateInput ] , [ qubitNum1 , qubitNum2 ] ] ]

Reference example to access gateType of second qubit = opsList[1]

'''
# Get gate inputs in order and for each gate input find details required to carry out that operation
# Set variable for while loop exit (gateInput need to be 0 to exit.).
# Init opsList to store gate type (dtype=int)
opsList = []
# Request gate type from user
print("Enter the first gate in order of operation. Enter 0 after the last gate input. 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T.")
# Store user number and then request details required for that gate operation
gateInput = int(input())
while gateInput < 0 or gateInput > 10:
    print(f"Gate at list[{gateInput}] is not a permitted value. Please run program again with correct gate values.'\n' 0=End of operations, 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T")
    gateInput = int(input())
if gateInput == 0:
        print("You have entered 0, the program will end. Please start again.")
        exit()
# Start while loop
while gateInput != 0:
    # check gates are within permitted limits of operation
    if gateInput < 0 or gateInput > 6:
        while gateInput < 0 or gateInput > 6:
            print(f"Gate at list[{gateInput}] is not a permitted value. Please run program again with correct gate values.'\n' 0=End of operations, 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T")
            gateInput = int(input())
    elif gateInput >= 1 and gateInput <=6: # X,Y,Z,H,P,T Gates
        # Request the qubit that this operation is to be applied to
        print(f"Enter the qubit this gate is to be applied to ( 1 to {qubits}): ")
        qubitNum1 = int(input())
        # Check qubit is within range
        while qubitNum1 < 1 or qubitNum1 > qubits:
            print(f"The qubit selected is out of range, please select another between 1 and {qubits}")
            qubitNum1 = int(input())
        # Add gate type and qubit to list of gate objects
        opsList.append([ [gateInput] , [[qubitNum1]] ])
        print("Enter the next gate in order of operation. Enter 0 after the last gate input. 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T.")
        gateInput = int(input())
    else:
        break
print(f"'\n'Results:'\n'")

### TODO -> The manipulation of matrix sizes
###      -> The additional info required for each gate, e.g. which qubits are to be used as control and target for CNOT etc.
###      -> Convert gates to objects. Inputs = qStates. Output = qStates.
for gate in range(len(opsList)):
    if opsList[gate][0][0] == 1: # Pauli-X gate
        qubit = opsList[gate][1][0][0]
        qState = qStates[qubit-1]
        X = np.array([[0, 1],
                      [1, 0]], dtype=complex)
        qStates[qubit-1] = np.dot(X,qState)
    elif opsList[gate][0][0] == 2: # Pauli-Y gate
        qubit = opsList[gate][1][0][0]
        qState = qStates[qubit-1]
        Y = np.array([[0,-1j],
                      [1j, 0]], dtype=complex)
        qStates[qubit-1] = np.dot(Y,qState)
    elif opsList[gate][0][0] == 3: # Pauli-Z gate
        qubit = opsList[gate][1][0][0]
        qState = qStates[qubit-1]
        Z = np.array([[1, 0],
                      [0,-1]])
        qStates[qubit-1] = np.dot(Z,qState)
    elif opsList[gate][0][0] == 4: # Hadamard gate
        qubit = opsList[gate][1][0][0]
        qState = qStates[qubit-1]
        H = isq2 * np.array([[1, 1],
                             [1,-1]])
        qStates[qubit-1] = np.dot(H,qState)
    elif opsList[gate][0][0] == 5: # Phase gate
        qubit = opsList[gate][1][0][0]
        qState = qStates[qubit-1]
        P = np.array([[1,0],
                      [0,0+1j]])
        qStates[qubit-1] = np.dot(P,qState)
    elif opsList[gate][0][0] == 6: # T gate
        qubit = opsList[gate][1][0][0]
        qState = qStates[qubit-1]
        T = np.array([[1,0],
                      [0,isq2 + isq2 * 1j]])
        qStates[qubit-1] = np.dot(T,qState)
    else:
        print("Error here")

# Measure states (Born rule)
# Initialise a classical register.
cReg = []
# For each qubit
for qState in range(len(qStates)):
    print(qStates[qState])
    # Identify the possible states and their probabilities. Take into account any in superposition and entangled states.
    print(np.square((qStates[qState]).real))
    # Test a random number generated, against the range of possible states.
    threshold = random.random()
    if np.square((qStates[qState]).real)[0] > threshold:
        cState = 0
    else:
        cState = 1
    # Record the state in a classical register.
    cReg.append(cState)



print("Press enter to end program.")

end = input()