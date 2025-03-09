# FederiMed: Overview

Built in the European Builders League: Milan Hackathon on the 8th and 9th of March 2025, **FederiMed** is a conceptual platform for centralized federated learning in healthcare. It enables hospitals worldwide to collaboratively train a machine learning model without sharing sensitive patient data. Doctors can interact with an LLM to access insights from anonymized patient data, such as similar symptoms, diagnoses, and treatments, helping improve decision-making and patient care.

## Key Features
- **Federated Learning**: Hospitals train local models and only send weights to a global server, keeping patient data secure and private.
- **LLM for Doctors**: Doctors can query the system for insights based on aggregated, anonymized patient data.
- **Privacy-Preserving**: Patient data stays within the hospital, complying with privacy regulations (e.g., HIPAA, GDPR).

## How It Works
1. Hospitals train local models on their data.
2. Federated learning aggregates model updates to improve a global model.
3. Doctors query the LLM for insights into patient conditions.
