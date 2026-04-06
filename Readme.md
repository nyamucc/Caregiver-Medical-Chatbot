# Caregiver Medication & Monitoring Assistant

[![Live App](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen?logo=streamlit)](https://caregiver-medical-chatbot-6hagwgmusjnx46v7zihhpd.streamlit.app/)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)


A Streamlit-based educational tool that helps caregivers look up medications and receive general information, monitoring guidance, safety alerts, and documentation prompts. Designed for long-term care, assisted living, and home-care environments, this tool supports safer workflows and improves shift communication.

## App Preview

![App Screenshot](https://github.com/nyamucc/Caregiver-Medical-Chatbot/blob/main/interface.png)


## Features
- **Medication Lookup:** General uses, typical dosage ranges (non-personalized), side effects, contraindications, interactions, and storage guidance.
- **Caregiver Monitoring Guidance:** What to observe after medication administration, including behavior, mobility, appetite, hydration, and vital signs.
- **Safety Alerts:** General red flags that require escalation to a nurse or clinician.
- **Fall-Risk & Hydration Prompts:** Medication-linked reminders to reduce preventable injuries and dehydration.
- **Behavior & Cognitive Monitoring:** Useful for dementia care and early detection of changes.
- **Infection Early-Warning Signs:** Prompts for antibiotics and high-risk medications.
- **Shift-Handover Note Generator:** Auto-creates structured notes caregivers can copy into documentation systems.
- **Simple Streamlit Interface:** Easy for caregivers with varying digital literacy levels.

## Technical Architecture

**Frontend:** Streamlit  
**Backend:** Python  
**Data Source:** Structured JSON dataset (`medications.json`)  
**Core Components:**
- Medication search engine (generic + brand names)
- JSON‑based medication knowledge base
- Monitoring & safety guidance generator
- Shift‑handover note generator
- Streamlit UI with dynamic rendering

**Deployment:** Streamlit Cloud  
**Version Control:** Git + GitHub  



## Why This Project Matters for Long‑Term Care

Medication errors and inconsistent monitoring are major risks in long‑term care settings.  
This tool supports:

- Safer medication administration  
- More consistent monitoring  
- Better shift‑handover communication  
- Faster caregiver onboarding  
- Reduced documentation gaps  

It demonstrates applied expertise in **AI, healthcare workflows, and LTC documentation**, aligning with national healthcare priorities.

## Future Enhancements

- Add chat‑based medication Q&A  
- Add fuzzy search and autocomplete  
- Add color‑coded safety alerts  
- Add vitals‑based monitoring suggestions  
- Add a second tool (symptom checker or vitals tracker)  
- Add multilingual support  

# 📂 Project Structure

Caregiver-Medical-Chatbot/
│
├── Data/
│   ├── medications_app.py
│   ├── medications.json
│
├── requirements.txt
├── README.md

MIT License

Copyright (c) 2024 Charity

Permission is hereby granted, free of charge, to any person obtaining a copy...
