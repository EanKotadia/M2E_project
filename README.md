# Interplanetary Communication Simulator

A project developed for **SpaceHack 2025: The Space Data Challenge**  
By **Ean Kotadia** and **Vihaan Vashistha**

## Overview

We are Ean Kotadia and Vihaan Vashistha, 10th-grade students passionate about science, technology, and innovation. During SpaceHack 2025, we were captivated by one of the most fundamental challenges in deep-space exploration — *how to maintain reliable communication over extreme distances, such as between Earth and Mars*.

Our project aims to simulate and visualize the real-world difficulties faced by interplanetary communication systems, such as signal delay, data degradation, and bandwidth constraints. Inspired by real mission data and challenges faced by space agencies, we set out to build an interactive tool that could both educate and propose future-facing solutions.

## Why Quantum Communication?

While exploring traditional models of signal transmission, we saw an opportunity to leverage **quantum information science** — specifically, the use of **qubits** (quantum bits) — to encode and transmit information more efficiently. Quantum communication has the potential to revolutionize how data is handled in space:

- Qubits can carry more information than classical bits through superposition and entanglement.
- Quantum encoding methods offer better security and integrity, which is essential in the noisy environments of space.
- Hypothetically, they could reduce the latency and increase resilience in high-noise or high-latency interplanetary networks.

Our simulator includes a conceptual layer where we model how qubits could be used to optimize data transfer protocols and compress information without significant loss. This exploration is powered by **Qiskit**, IBM’s quantum computing framework.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Flask), SQLAlchemy  
- **Quantum Simulation Layer**: Qiskit (for modeling qubit-based transmission)

## Purpose

This project is our contribution to advancing public understanding of space communication systems and exploring the exciting potential of quantum technologies in the context of space. Through SpaceHack 2025, we hope to inspire more students and enthusiasts to think creatively about the future of deep-space infrastructure and the role of emerging technologies in shaping it.

## How to Run

Follow the steps below to set up and run the project locally:

### 1. Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
### 2. Set Up a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
### 3. Install Dependencies
pip install -r requirements.txt
If requirements.txt doesn't exist, you can manually install:
pip install flask sqlalchemy qiskit
### 4. Run the Application
python app.py

Make sure you have Python 3.7+ installed.
Qiskit may require additional setup depending on your system. Visit Qiskit.org for details.
