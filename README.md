# M2E-Link

**M2E-Link** is a simulation demonstrating how quantum bits (qbits) could enable secure, faster, and theoretically unbreakable communication between Mars rovers, satellites, and Earth.

Developed during the **SpaceHack: Space Data Challenge** by **Ean Kotadia** and **Vihaan Vashistha**, 10th-grade students passionate about science and innovation.

---

## Project Overview

M2E-Link showcases:

- A **multi-hop relay simulation** transmitting data packets from Mars to Earth via satellites.
- Animated **data packet movement**, wave effects, and live mission logs.
- A **dynamic interface** styled to match a futuristic space mission aesthetic.
- Concepts inspired by **quantum encryption**, deep-space latency research, and interplanetary communication systems.

During the event, we researched NASA APIs, current encryption standards, and deep-space transmission challenges. Quantum communication emerged as a transformative technology, inspiring us to build this simulation.

---

## Features

- **Python Flask server** to serve the simulation web app.
- **JavaScript and CSS animations** for visualizing secure, multi-hop data transfer.
- **Interactive mission log system** with real-time status updates.
- **Wave and signal animations** to represent communication packets.
- Modular code ready for further experimentation with APIs and data streams.

---

## Screenshots

![small](https://github.com/user-attachments/assets/32351791-3305-43b0-9cd9-4e633c7fe0b1)

<img width="121" alt="small1" src="https://github.com/user-attachments/assets/919b4b2b-06d3-4f53-8dec-e8508bf80c23" />


---

## Installation and Setup

Follow these steps to set up the project locally:

### Clone the repository

```bash
git clone https://github.com/yourusername/m2e-link.git
cd m2e-link
```

### Create a virtual environment

```python -m venv venv```

### Activate the virtual environment

On Windows:
```
venv\Scripts\activate
```
On macOS/Linux:
```
source venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run the Flask app
```
flask run
```

## Notes

The quantum simulation code using Qiskit is available in the qiskit-sim branch:

git checkout qiskit-sim
This branch contains prototype Qiskit scripts demonstrating basic quantum key distribution concepts.

## License

This project is released under the MIT License.
