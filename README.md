# M2E-Link

M2E-Link is a simulation demonstrating how quantum bits (qbits) could enable secure, faster, and theoretically unbreakable communication between Mars rovers, satellites, and Earth.

Developed during the SpaceHack: Space Data Challenge by Ean Kotadia and Vihaan Vashistha.

## Project Overview

M2E-Link showcases:

A multi-hop relay simulation from Mars to Earth.
Animated data packet transfers and live mission logs.
A dynamic interface styled to match a futuristic mission aesthetic.
Concepts inspired by quantum encryption and deep-space communication research.
Features

Python Flask server to run the simulation.
JavaScript and CSS animations for visualizing data transfer.
Interactive log system and real-time status updates.
Installation and Setup

### Clone the repository
git clone https://github.com/yourusername/m2e-link.git
cd m2e-link
### Create a virtual environment
python -m venv venv
Activate the virtual environment
### On Windows:
venv\Scripts\activate
### On macOS/Linux:
source venv/bin/activate
### Install dependencies
pip install -r requirements.txt
### Run the Flask app
flask run
### Open your browser and go to
http://127.0.0.1:5000
## Project Structure

m2e-link/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
## Notes

The quantum simulation code using Qiskit is available in the qiskit-sim branch:

git checkout qiskit-sim
This branch contains prototype Qiskit scripts illustrating basic quantum key distribution concepts.

## License

This project is released under the MIT License.

