# FederiMed: Overview

### The Problem
When you visit your primary care doctor with unique symptoms, they might suggest a conservative treatment plan with medications, but this could only delay the underlying condition. Meanwhile, other doctors around the world may have encountered similar cases and provided effective treatments. Unfortunately, this valuable clinical knowledge is stored in each hospital's database, sometimes in individual patient files, making it difficult for doctors to benefit from the collective insights of their global peers.

If you're fortunate enough to survive the initial treatment, you might return to primary care with new insights. This time, however, your doctor could offer a more effective treatment plan based on what has worked for other patients with similar symptoms or medical histories, thanks to the knowledge shared globally through **FederiMed**.

### Our Solution
Federated Learning (FL) allows AI models to learn from decentralized medical data without exposing patient records. Instead of transferring raw data, each hospital trains a local AI model, keeping patient information secure.

By combining FL with Fine-Tuned Large Language Models (LLMs), we enable a global AI system to improve continuously from real-world cases while ensuring data privacy.

## How It Works
Local Training:  Each health institution trains its own model on anonymized patient data.
Model Weight Sharing: Only model updates, not raw data, are sent to a global server.
Global Aggregation: A central system refines a shared LLM by integrating insights from multiple hospitals.
Privacy Preservation: Patient records never leave the hospital, ensuring compliance with HIPAA and GDPR.
Smarter AI Assistance: Doctors can query the federated fine-tuned LLM for personalized, evidence-based treatment recommendations.

### Current Demo (Proof of Concept)
- **Synthetic Data**: We generated synthetic patient data using [Synthea](https://github.com/synthetichealth/synthea), simulating 100 patients to test the system.
- **Federated Learning Framework**: We employed [**FLWR**](https://github.com/adap/flower), a Python-based federated learning framework, to facilitate the collaboration and model training.
- **Current Status**: The platform is currently operational with a demo setup supporting 1-2 clients, showcasing the potential of federated learning in healthcare.

By unlocking the power of federated learning, **FederiMed** empowers doctors to access actionable, data-driven insights and make more informed decisions, ultimately improving patient outcomes while safeguarding privacy.
