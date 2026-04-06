import json
import streamlit as st

# -----------------------------
# Load Medications Data
# -----------------------------
@st.cache_data
def load_medications():
    with open("medications.json", "r") as f:
        return json.load(f)

meds = load_medications()

# -----------------------------
# Helper Function
# -----------------------------
def find_medication(query):
    query = query.lower().strip()
    for med in meds:
        if query in med["medication"].lower():
            return med
        if any(query in brand.lower() for brand in med["brand_names"]):
            return med
    return None

# -----------------------------
# Streamlit Page Setup
# -----------------------------
st.set_page_config(
    page_title="Caregiver Medication & Monitoring Assistant",
    layout="wide"
)

st.title("💊 Caregiver Medication & Monitoring Assistant")
st.write("Educational tool for caregivers in long-term care, assisted living, and home-care settings.")
st.divider()

# -----------------------------
# Session State for Search History
# -----------------------------
if "search_history" not in st.session_state:
    st.session_state.search_history = []

# -----------------------------
# User Input
# -----------------------------
user_input = st.text_input("Enter a medication name or brand name:")

if user_input:
    med = find_medication(user_input)

    if med:
        # Save search in session state
        st.session_state.search_history.append(med["medication"])

        st.subheader(f"📘 {med['medication']}")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### General Information")
            st.write("**Category:**", med["category"])
            st.write("**General Uses:**", ", ".join(med["general_uses"]))
            st.write("**Typical Dosage Range:**", med["typical_dosage_range"])
            st.write("**Brand Names:**", ", ".join(med["brand_names"]))

        with col2:
            st.markdown("### Side Effects & Safety")
            st.write("**Common Side Effects:**", ", ".join(med["common_side_effects"]))
            st.write("**Safety Alerts:**", ", ".join(med["safety_alerts"]))
            st.write("**Fall Risk Prompts:**", ", ".join(med["fall_risk_prompts"]) if med["fall_risk_prompts"] else "None")
            st.write("**Hydration Prompts:**", ", ".join(med["hydration_prompts"]) if med["hydration_prompts"] else "None")

        st.divider()

        # -----------------------------
        # Monitoring Guidance
        # -----------------------------
        st.markdown("### 👀 Caregiver Monitoring Guidance")
        st.write(", ".join(med["monitoring_guidance"]))

        st.divider()

        # -----------------------------
        # Shift Handover Note Generator
        # -----------------------------
        st.markdown("### 📝 Shift Handover Note Generator")

        handover_text = f"""
Medication: {med['medication']}
Category: {med['category']}
General Uses: {", ".join(med['general_uses'])}

Monitoring Guidance:
- {chr(10).join(med['monitoring_guidance'])}

Safety Alerts:
- {chr(10).join(med['safety_alerts'])}

Hydration Prompts:
- {chr(10).join(med['hydration_prompts']) if med['hydration_prompts'] else "None"}

Fall Risk Prompts:
- {chr(10).join(med['fall_risk_prompts']) if med['fall_risk_prompts'] else "None"}

Suggested Handover Notes:
- {chr(10).join(med['handover_notes'])}
"""
        st.text_area("Copy this into your documentation system:", handover_text, height=250)

    else:
        st.error("Medication not found. Try another name or check spelling.")

# -----------------------------
# Display Search History
# -----------------------------
if st.session_state.search_history:
    st.divider()
    st.markdown("### 🔍 Search History")
    st.write(", ".join(st.session_state.search_history))