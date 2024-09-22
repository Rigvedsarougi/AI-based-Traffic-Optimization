# AI Traffic Optimization System

This project aims to reduce traffic congestion using an AI-powered adaptive traffic signal control system. The system collects data from cameras and sensors, predicts traffic flows, and dynamically adjusts traffic lights using Reinforcement Learning (RL).

## Features
- Real-time traffic data processing from cameras and sensors
- Computer Vision for vehicle detection
- Reinforcement Learning model for adaptive traffic control
- Real-time monitoring dashboard

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the main script: `python main.py`
3. (Optional) Start the dashboard: `python dashboard/app.py`

## Directory Structure
- `data/`: Simulated camera and sensor data.
- `models/`: ML models for traffic optimization.
- `controllers/`: Logic for traffic light control.
- `dashboard/`: Real-time monitoring system.
