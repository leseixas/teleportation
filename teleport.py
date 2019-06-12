#!/usr/bin/env python

'''
  Quantum teleportation example
'''

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute

# IBM Q device
#from qiskit import IBMQ
#from qiskit.providers.ibmq import least_busy
#IBMQ.load_accounts()
#large_enough_devices = IBMQ.backends(filters=lambda x: x.configuration().n_qubits > 3 and not x.configuration().simulator)
#backend = least_busy(large_enough_devices)

# QASM simulator
from qiskit import Aer
backend = Aer.get_backend('qasm_simulator')

print("Backend:",backend)

