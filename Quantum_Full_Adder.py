# Import libraries
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, BasicAer, execute
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.visualization import *
from PIL import Image
import matplotlib.pyplot as plt
q = QuantumRegister(5) # Five Qubits
c = ClassicalRegister(5) # Five Bits
qc = QuantumCircuit(q, c) # Quantum Circuit
qc.x(q[0]) # Pauli X gate
qc.x(q[1]) # Pauli X gate
qc.ccx(q[0], q[1], q[3]) # Toffoli Gate
qc.cx(q[0], q[1]) # CNot gate
qc.x(q[2]) # Pauli X gate
qc.ccx(q[1], q[2], q[4]) # Toffoli Gate
qc.cx(q[1], q[2]) # CNot gate
qc.cx(q[0], q[1]) # CNot gate
qc.measure(q[2], c[0]) # Measure value
qc.measure(q[1], c[1]) # Measure value
# Use the simulator to get the measurements
job = execute(qc, backend = BasicAer.get_backend('qasm_simulator'), shots=1000)
result = job.result() # Get the result back from the job
qc.draw(output='mpl') # Draw the circuit
plt.show() # Display the circuit
fig = plot_histogram(result.get_counts(qc)) # Generate the image
fig.savefig("full_adder.png") # Save the image
image = Image.open("full_adder.png") # Open the image
image.show() # Display the image