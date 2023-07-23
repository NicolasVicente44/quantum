# Import libraries
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, BasicAer
from qiskit.tools.visualization import *
from PIL import Image
import matplotlib.pyplot as plt
q = QuantumRegister(2) # Two Qubits
c = ClassicalRegister(2) # Two Bits
bell_state = QuantumCircuit(q, c) # Quantum Circuit
bell_state.h(q[0]) # Superposition. Hadamard Gate
bell_state.cx(q[0], q[1]) # Entanglement. CNOT gate.
bell_state.measure(q, c) # Measure value
# Use the simulator to get the measurements
job = execute(bell_state, backend = BasicAer.get_backend('qasm_simulator'), shots=1000)                     
result = job.result() # Get the result back from the job
bell_state.draw(output='mpl') # Draw the circuit
plt.show() # Display the circuit
fig = plot_histogram(result.get_counts(bell_state)) # Generate the image
fig.savefig("bell_state.png") # Save the image
image = Image.open("bell_state.png") # Open the image
image.show() # Display the image