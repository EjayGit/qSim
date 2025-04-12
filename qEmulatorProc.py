import numpy as np

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
Init gateList in which:

gateList = [ gateType , gateType , ... , gateType ]

gateType = [ qubitNum1 , qubitNum2, ... , qubitNumX ]

e.g.: gateList = [ gateType = [ [ gateInput ] , [ qubitNum1 , qubitNum2 ] ] ]

Reference example to access gateType = gateList[1]

'''
# Get gate inputs in order and for each gate input find details required to carry out that operation
# Set variable for while loop exit (gateInput need to be 0 to exit.).
# Init gateList to store gate type (dtype=int)
gateList = []
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
        gateList.append([ [gateInput] , [[qubitNum1]] ])
        print("Enter the next gate in order of operation. Enter 0 after the last gate input. 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T.")
        gateInput = int(input())
    else:
        break
print(f"'\n'Results:'\n'")

### To be added -> The manipulation of matrix sizes
###             -> The additional info required for each gate, e.g. which qubits are to be used as control and target for CNOT etc.
###             -> Convert gates to objects. Inputs = qStates. Output = qStates.
for gate in range(len(gateList)):
    if gateList[gate][0][0] == 1: # Pauli-X gate
        qubit = gateList[gate][1][0][0]
        qState = qStates[qubit-1]
        X = np.array([[0, 1],
                      [1, 0]], dtype=complex)
        qStates[qubit-1] = np.dot(X,qState)
    elif gateList[gate][0][0] == 2: # Pauli-Y gate
        qubit = gateList[gate][1][0][0]
        qState = qStates[qubit-1]
        Y = np.array([[0,-1j],
                      [1j, 0]], dtype=complex)
        qStates[qubit-1] = np.dot(Y,qState)
    elif gateList[gate][0][0] == 3: # Pauli-Z gate
        qubit = gateList[gate][1][0][0]
        qState = qStates[qubit-1]
        Z = np.array([[1, 0],
                      [0,-1]])
        qStates[qubit-1] = np.dot(Z,qState)
    elif gateList[gate][0][0] == 4: # Hadamard gate
        qubit = gateList[gate][1][0][0]
        qState = qStates[qubit-1]
        H = isq2 * np.array([[1, 1],
                             [1,-1]])
        qStates[qubit-1] = np.dot(H,qState)
    elif gateList[gate][0][0] == 5: # Phase gate
        qubit = gateList[gate][1][0][0]
        qState = qStates[qubit-1]
        P = np.array([[1,0],
                      [0,0+1j]])
        qStates[qubit-1] = np.dot(P,qState)
    elif gateList[gate][0][0] == 6: # T gate
        qubit = gateList[gate][1][0][0]
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
#for qState in qStates:
    # Identify the possible states and their probabilities. Take into account any in superposition and entangled states.

    # Allocate the possible states an appropriate range between 0-1.

    # Test a random number generated, against the range of possible states.

    # Record the state in a classical register.
#    cReg.append(cState)

for qState in range(len(qStates)):
    print(qStates[qState])

print("Press enter to end program.")
end = input()
