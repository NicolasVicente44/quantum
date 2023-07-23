# Import libraries
from qiskit import IBMQ, BasicAer, execute
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
import enchant
# Load the US library
d = enchant.Dict("en_US") 
q = QuantumRegister(24, 'q') # Twenty four Qubits
c = ClassicalRegister(24, 'c') # Twenty four Bits
qc = QuantumCircuit(q, c) # Quantum Circuit
# First letter
qc.h(q[0]) # Hadamard Gate
qc.h(q[1]) # Hadamard Gate
qc.h(q[2]) # Hadamard Gate
qc.h(q[3]) # Hadamard Gate
qc.h(q[4]) # Hadamard Gate
qc.x(q[5]) # Pauli X gate
qc.x(q[6]) # Pauli X gate
# Second letter
qc.h(q[8])
qc.h(q[9])
qc.h(q[10])
qc.h(q[11])
qc.h(q[12])
qc.x(q[13])
qc.x(q[14])
      
# Third letter
qc.h(q[16])
qc.h(q[17])
qc.h(q[18])
qc.h(q[19])
qc.h(q[20])
qc.x(q[21])
qc.x(q[22])
  
# Measure all 24 Qubits  
for j in range(24):
    qc.measure(q[j], c[j])
# Use the simulator to get the measurements    
job = execute(qc, backend=BasicAer.get_backend('qasm_simulator'), shots=100)
# Get the result back from the job
result = job.result().get_counts(qc)
characterDict = {}
# Separate each result into 8 bits, turning them into letters
for bitString in result:
    char1 = chr(int( bitString[0:8] ,2))
    char2 = chr(int( bitString[8:16] ,2))
    char3 = chr(int( bitString[16:24] ,2))
# Put all resulting words into an array    
    characterDict[ char1 + char2 + char3 ] = result[bitString] / 1024
    
counter = 0    
# Loop through all the generated words
for char in characterDict.keys():
# Using pyenchant, find which ones are valid  
    if d.check(char) == True:
# Count the valid words
        counter += 1
# Print them out    
        print(char)
# Out of a 100, how many are actually valid?
print(str(counter) + " valid words of a generated 100") 