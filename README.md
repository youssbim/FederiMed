# FederiMed: Overview

![FederiMed Demo](https://github.com/youssbim/FederiMed/blob/main/shortdemo.gif?raw=true)

# Introduction to the Problem

Imagine waking up with an unusual mix of symptoms and heading to your doctor.

But what if your symptoms represent a pattern of a condition, possibly a serious one, that your doctor has never seen before? Without prior experience, they might delay the best solution for you.

They might get it right, or they could misdiagnose your condition, postponing the right treatment when time is critical. A quick search online will show you just how many lives are impacted by delayed or incorrect diagnoses every year.

Now, what if thousands of doctors worldwide have already identified, treated, and even prevented this exact condition? Their knowledge exists, but it’s locked away in private records, inaccessible beyond their walls. And if time is critical, that delay could make all the difference.

Ask yourself:
- Would you rather wake up knowing your doctor can access the collective expertise of global medical cases, instantly improving their diagnosis and treatment plan?
- Or would you prefer relying on one doctor’s individual experience, hoping they get it right before it’s too late?

---

# The Challenge: Why Can’t We Train AI on Private Health Data?

Medical data is one of the most valuable yet highly protected assets in the world. Strict regulations, such as:

- **HIPAA (U.S.)** – Governs patient data privacy and security.
- **GDPR (Europe)** – Imposes strict rules on data sharing and processing.

While AI thrives on large, centralized datasets, using sensitive health data in this way presents major challenges:

- **Privacy risks** – Patient data could be exposed or misused.
- **Legal barriers** – Regulations prevent free sharing of health records.
- **Ethical concerns** – Patients may not consent to their data being used.
- **Security threats** – Even anonymized data is vulnerable to breaches.

Even if health institutions agreed to share anonymized records, data leaks and unauthorized access remain serious risks.

### This raises a critical question:
**How can we build a global AI model that learns from patient cases worldwide without exposing private health data?**

---

# The Demo We Wanted to Build: FederiMed (Proof of Concept)

To demonstrate the potential of federated learning in healthcare, we developed a prototype:

- **Synthetic Patient Data** – Instead of using **Synthea**, we used the **MedAlpaca flash card dataset** to simulate real-world scenarios.
- **Fine-Tuned LLMs** – We fine-tuned **DistilBERT** and **GPT-2** from Hugging Face to enhance clinical text understanding and improve diagnostic insights.
- **Federated Learning Framework** – We implemented our model using **FLWR (Flower)**, a federated learning framework designed for secure AI collaboration.
- **Live Testing** – Due to computational limitations, we were unable to complete our demo with more than **two clients**. However, we are actively working on overcoming these challenges to build a fully functional and scalable demo as soon as possible.

---

# Computational Challenges and Next Steps

While we aimed to develop a fully functional federated learning prototype, we encountered computational limitations that restricted our ability to scale beyond two clients. The challenges included:

- **High computational requirements** – Training federated models requires significant processing power, which was a bottleneck for our initial prototype.
- **Resource constraints** – Limited access to cloud-based GPUs prevented us from running large-scale federated learning experiments.

### Next Steps:

- **Optimize model efficiency** – We will explore ways to reduce computational load while maintaining high accuracy.
- **Expand client base** – Our goal is to scale beyond two clients to fully validate the benefits of federated learning.
- **Improve infrastructure** – Seeking access to more powerful hardware and cloud resources to support our research and development.

Additionally, the current web application is **hard-coded and not yet connected to the fine-tuned LLM**. It serves only as a visual representation of what the final product will be. Our next goal is to fully integrate the web app with our federated learning model to enable real-time AI-driven insights for medical professionals.

We remain committed to building a fully functional demo that showcases the real potential of federated learning in healthcare. Stay tuned for updates as we continue our work!


