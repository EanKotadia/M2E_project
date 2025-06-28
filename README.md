# M2E-Link: Quantum-Powered Mars-to-Earth Communication

**By Ean Kotadia & Vihaan Vashistha**  
Built during the **SpaceHack: Space Data Challenge**

---

## Overview

**M2E-Link** is an interactive simulation that explores the future of **deep-space communication** using **quantum encryption** and **satellite relays**.

We imagined a world where rovers on Mars transmit critical data to Earth securely — by hopping across a quantum-linked satellite network using **Quantum Key Distribution (QKD)**.

This mission-themed web app blends science, UI/UX design, and futuristic tech to bring this vision to life.

---

## Features

- Mars-to-Earth relay animation
- Live packet transmission visualization
- Quantum communication showcase using Qiskit
- Real-time mission clock and status tracker
- Audio feedback with transmission "beep" effects
- Multi-hop satellite simulation
- Educational panel explaining quantum encryption and QKD

---

## Tech Stack

| Layer              | Tools Used                      |
|--------------------|----------------------------------|
| Frontend UI        | HTML, CSS, JavaScript            |
| Backend Framework  | Flask (Python)                   |
| Quantum Simulation | Qiskit (IBM Quantum SDK)         |
| Visual Effects     | CSS animations, DOM scripting    |
| Audio              | HTML5 Audio API (`beep.mp3`)     |

---

## How It Works

1. **Quantum Key Distribution (QKD)** enables unbreakable encryption using qubits.
2. The simulation visualizes a data packet hopping from:
   - **Mars → Sat3 → Sat2 → Sat1 → Earth → (return trip)**  
3. Each transmission uses:
   - Smooth CSS animations
   - DOM updates with colored data pulses
   - Wave pulse effects and sounds
4. A **mission dashboard** shows:
   - Mission ID
   - Current status
   - Phase
   - Live mission clock

---

## Project Structure

/static
/css # Stylesheets
/images # Quantum schematic placeholder
/sfx # Audio effects (beep)

/templates
index.html # Main simulation template

app.py # Flask app backend
README.md # Project documentation


---

## Hackathon Timeline

### Day 1 — Ideation
- Identified the problem: secure, efficient space communication
- Researched NASA APIs, QKD, satellite networks

### Day 2 — Visualization & Architecture
- Built Mars-Earth animation using CSS
- Defined relay hop logic and transmission layers

### Day 3 — Final Integration
- Polished the UI
- Added quantum education panel and live mission interface

---

## Preview

![Stage1](/static/images/S-1.png)  
*Quantum Satellite Link Schematic*

![Stage-2](/static/images/S-2.jpg)  
*Quantum Satellite Link Schematic*


## Mission ID

**MARS-0425**  
**Status:** ✔ Mission Complete  
**Phase:** Secure Relay Protocol Complete

---

## Acknowledgments

- Built with 💙 during the SpaceHack: Space Data Challenge
- Inspired by real-world work in QKD, IBM Qiskit, and NASA deep space protocols

---

## Contact
- Vihaan Vashistha 
- Ean Kotadia
*10th Grade*
Passionate about Quantum Tech & Space Innovation
