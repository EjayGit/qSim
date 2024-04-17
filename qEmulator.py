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
print("Enter the first gate in order of operation. Enter 0 after the last gate input. 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T, 7=CNOT, 8=CZ, 9=SWAP, 10=Toloffi.")
# Store user number and then request details required for that gate operation
gateInput = int(input())
while gateInput < 0 or gateInput > 10:
    print(f"Gate at list[{gateInput}] is not a permitted value. Please run program again with correct gate values.'\n' 0=End of operations, 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T, 7=CNOT, 8=CZ, 9=SWAP, 10=Toloffi")
    gateInput = int(input())
if gateInput == 0:
        print("You have entered 0, the program will end. Please start again.")
        exit()
# Start while loop
while gateInput != 0:
    # check gates are within permitted limits of operation
    if gateInput < 0 or gateInput > 10:
        while gateInput < 0 or gateInput > 10:
            print(f"Gate at list[{gateInput}] is not a permitted value. Please run program again with correct gate values.'\n' 0=End of operations, 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T, 7=CNOT, 8=CZ, 9=SWAP, 10=Toloffi")
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
        print("Enter the next gate in order of operation. Enter 0 after the last gate input. 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T, 7=CNOT, 8=CZ, 9=SWAP, 10=Toloffi.")
        gateInput = int(input())
    elif gateInput >=7 and gateInput <=9: # CNOT, CZ, SWAP Gates
        # Request the qubit that this operation is to be applied to
        print(f"Enter the control qubit this gate is to be applied to ( 1 to {qubits}): ")
        qubitNum1 = int(input())
        while qubitNum1 < 1 or qubitNum1 > qubits:
            print(f"The qubit selected is out of range, please select another control qubit between 1 and {qubits}")
            qubitNum1 = int(input())
        print(f"Enter the target qubit this gate is to be applied to ( 1 to {qubits}): ")
        qubitNum2 = int(input())
        while qubitNum2 < 1 or qubitNum2 > qubits or qubitNum2 == qubitNum1:
            print(f"The qubit selected is out of range, please select another between 1 and {qubits}")
            qubitNum2 = int(input())
        # Add gate type and qubit to list of gate objects
        gateList.append([ [gateInput] , [[qubitNum1],[qubitNum2]] ])
        print("Enter the next gate in order of operation. Enter 0 after the last gate input. 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T, 7=CNOT, 8=CZ, 9=SWAP, 10=Toloffi.")
        gateInput = int(input())
    elif gateInput == 10: # Toloffi Gate
        # Request the qubit that this operation is to be applied to
        print(f"Enter the first control qubit this gate is to be applied to ( 1 to {qubits}): ")
        qubitNum1 = int(input())
        while qubitNum1 < 1 or qubitNum1 > qubits:
            print(f"The qubit selected is out of range, please select another between 1 and {qubits}")
            qubitNum1 = int(input())
        print(f"Enter the second control qubit this gate is to be applied to ( 1 to {qubits}): ")
        qubitNum2 = int(input())
        while qubitNum2 < 1 or qubitNum2 > qubits or qubitNum2 == qubitNum1:
            print(f"The qubit selected is invalid, please select another between 1 and {qubits}")
            qubitNum2 = int(input())
        print(f"Enter the target qubit this gate is to be applied to ( 1 to {qubits}): ")
        qubitNum3 = int(input())
        while qubitNum3 < 1 or qubitNum3 > qubits or qubitNum3 == qubitNum1 or qubitNum3 == qubitNum2:
            print(f"The qubit selected is invalid, please select another between 1 and {qubits}")
            qubitNum3 = int(input())
        # Add gate type and qubit to list of gate objects
        gateList.append([ [  gateInput] , [[qubitNum1],[qubitNum2],[qubitNum3]] ])
        print("Enter the next gate in order of operation. Enter 0 after the last gate input. 1=X, 2=Y, 3=Z, 4=H, 5=P, 6=T, 7=CNOT, 8=CZ, 9=SWAP, 10=Toloffi.")
        gateInput = int(input())
    else:
        break
print(f"'\n'Results:'\n'")

### To be added -> The manipulation of matrix sizes
###             -> The additional info required for each gate, e.g. which qubits are to be used as control and target for CNOT etc.
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
                      [0,1j]])
        qStates[qubit-1] = np.dot(P,qState)
    elif gateList[gate][0][0] == 6: # T gate
        qubit = gateList[gate][1][0][0]
        qState = qStates[qubit-1]
        T = np.array([[1,0],
                      [0,isq2 + isq2 * 1j]])
        qStates[qubit-1] = np.dot(T,qState)
    elif gateList[gate][0][0] == 7: # Controlled NOT gate
        qubit1 = gateList[gate][1][0][0] # Control
        qubit2 = gateList[gate][1][1][0] # Target
        qState1 = qStates[qubit1-1]
        qState2 = qStates[qubit2-1]
        qState = np.kron(qState1, qState2)
        CNOT = np.array([[1,0,0,0],
                         [0,1,0,0],
                         [0,0,0,1],
                         [0,0,1,0]])
        qStates[qubit2-1] = np.dot(CNOT,qState)
    elif gateList[gate][0][0] == 8: # Controlled Z gate
        qubit1 = gateList[gate][1][0][0]
        qubit2 = gateList[gate][1][1][0]
        qState1 = qStates[qubit1-1]
        qState2 = qStates[qubit2-1]
        qState = np.kron(qState1, qState2)
        CZ = np.array([[1,0,0,0],
                       [0,1,0,0],
                       [0,0,1,0],
                       [0,0,0,-1]])
        qStates[qubit2-1] = np.dot(CZ,qState)
    elif gateList[gate][0][0] == 9: # SWAP gate
        qubit1 = gateList[gate][1][0][0]
        qubit2 = gateList[gate][1][1][0]
        qState1 = qStates[qubit1-1]
        qState2 = qStates[qubit2-1]
        qState = np.kron(qState1, qState2)
        SWAP = np.array([[1,0,0,0],
                         [0,0,1,0],
                         [0,1,0,0],
                         [0,0,0,1]])
        qStates[qubit-1] = np.dot(SWAP,qState)
    elif gateList[gate][0][0] == 10: # Toffoil gate
        qubit1 = gateList[gate][1][0][0]
        qubit2 = gateList[gate][1][1][0]
        qubit3 = gateList[gate][1][2][0]
        qState1 = qStates[qubit1-1]
        qState2 = qStates[qubit2-1]
        qState3 = qStates[qubit3-1]
        qState = np.kron(qState1, qState2)
        qState = np.kron(qState, qState3)
        toffoli = np.array([[1,0,0,0,0,0,0,0],
                            [0,1,0,0,0,0,0,0],
                            [0,0,1,0,0,0,0,0],
                            [0,0,0,1,0,0,0,0],
                            [0,0,0,0,1,0,0,0],
                            [0,0,0,0,0,1,0,0],
                            [0,0,0,0,0,0,0,1],
                            [0,0,0,0,0,0,1,0]])
        qStates[qubit3-1] = np.dot(toffoli,qState)
    else:
        print("Error line 193")

# Measure states (Born rule)
# Initialise a classical register.
cReg = []
# For each qubit
#for qState in qStates:
    # Identify the possible states and their probabilities.

    # Allocate the possible states an appropriate range between 0-1.

    # Test a random number generated, against the range of possible states.

    # Record the state in a classical register.
#    cReg.append(cState)

for qState in range(len(qStates)):
    print(qStates[qState])

print("Enter any value to end program.")
end = input()
