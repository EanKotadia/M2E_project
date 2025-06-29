REQUIREMENTS TO RUN QISKIT CODE:-

1)Set up miniconda environment in jupyter notebook and use the miniconda kernel 

2)pip install qiskit qiskit-aer cryptography matplotlib networkx numpy (or pip install dependencies)

Stage-by-Stage Process
🔐 Stage 1: Quantum Key Distribution
Qubit Transmission
Generates 1024+ quantum bits (qubits) with random bases
Rover encodes bits: |0⟩/|1⟩ (Z-basis) or |+⟩/|-⟩ (X-basis)
Orbiter measures in random bases
Sifting & Error Detection
Keeps only measurements with matching bases (50% loss expected)
Checks 128 random bits for eavesdropping (aborts if >12% error)
Produces 256-bit cryptographic key
AES-256 Encryption
Encrypts "Mars Life Detection" message
Uses CBC mode with PKCS#7 padding
Generates random Initialization Vector (IV)

🛰️ Stage 2: Optimal Path Routing
Satellite Network Modeling
Nodes: ["A (Mars)", "B (Relay)", "C (Gateway)", "D (Earth)"]
Edges: [("A","B",2), ("A","C",4), ("A","D",10), ("B","D",8), ("C","D",3)]
Path optimization to conserve energy
