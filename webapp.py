import streamlit as st
import time
import random

# Comprehensive Symptoms Database
SYMPTOMS_DATABASE = {
    "Emergency/Critical": {
        "chest_pain": {
            "name": "Chest Pain/Pressure",
            "urgency": "immediate",
            "associated_conditions": ["Myocardial Infarction", "Pulmonary Embolism", "Aortic Dissection"],
            "risk_level": "high",
            "key_questions": ["Duration", "Character of pain", "Radiation", "Associated symptoms"]
        },
        "severe_sob": {
            "name": "Severe Shortness of Breath",
            "urgency": "immediate",
            "associated_conditions": ["Pulmonary Embolism", "Severe Asthma", "Heart Failure"],
            "risk_level": "high",
            "key_questions": ["Onset", "Triggers", "Position effect", "Associated chest pain"]
        },
        "stroke_symptoms": {
            "name": "Stroke-like Symptoms",
            "urgency": "immediate",
            "associated_conditions": ["Acute Stroke", "TIA", "Intracranial Hemorrhage"],
            "risk_level": "high",
            "key_questions": ["Time of onset", "Speech changes", "Weakness pattern", "Mental status"]
        }
    },
    "Neurological": {
        "seizures": {
            "name": "Active Seizures",
            "urgency": "immediate",
            "associated_conditions": ["Status Epilepticus", "Brain Lesion", "Metabolic Disturbance"],
            "risk_level": "high"
        },
        "sudden_paralysis": {
            "name": "Sudden Paralysis/Weakness",
            "urgency": "immediate",
            "associated_conditions": ["Stroke", "Guillain-Barré", "Multiple Sclerosis"],
            "risk_level": "high"
        },
        "severe_headache": {
            "name": "Thunder-clap Headache",
            "urgency": "immediate",
            "associated_conditions": ["Subarachnoid Hemorrhage", "Meningitis", "Cerebral Venous Thrombosis"],
            "risk_level": "high"
        }
    },
    "Rare/Complex": {
        "stevens_johnson": {
            "name": "Severe Skin Peeling/Blistering",
            "urgency": "immediate",
            "associated_conditions": ["Stevens-Johnson Syndrome", "TEN", "Severe Drug Reaction"],
            "risk_level": "high"
        },
        "widespread_purpura": {
            "name": "Sudden Widespread Purple Spots",
            "urgency": "immediate",
            "associated_conditions": ["DIC", "Meningococcemia", "ITP"],
            "risk_level": "high"
        },
        "tetany": {
            "name": "Muscle Spasms with Rigidity",
            "urgency": "high",
            "associated_conditions": ["Severe Hypocalcemia", "Tetanus", "Hypomagnesemia"],
            "risk_level": "high"
        }
    },
    "Internal Medicine": {
        "severe_abdominal_pain": {
            "name": "Severe Acute Abdominal Pain",
            "urgency": "high",
            "associated_conditions": ["Appendicitis", "Bowel Perforation", "Mesenteric Ischemia"],
            "risk_level": "high"
        },
        "diabetic_emergency": {
            "name": "Severe Hyperglycemia/Confusion",
            "urgency": "high",
            "associated_conditions": ["DKA", "HHS", "Severe Sepsis"],
            "risk_level": "high"
        },
        "acute_jaundice": {
            "name": "Rapid Onset Jaundice",
            "urgency": "high",
            "associated_conditions": ["Acute Liver Failure", "Hemolysis", "Biliary Obstruction"],
            "risk_level": "high"
        }
    }
}

# Fun responses for non-FL mode
NON_FL_RESPONSES = [
    "🤔 Hmm... Without my federated knowledge, I'm just a very expensive Magic 8 Ball...",
    "📚 Let me check my limited database... *flips through empty notebook*",
    "🔮 Crystal ball mode activated (FL would be more accurate though!)",
    "🤖 Basic mode: Beep boop... Need more data... Please enable FL!",
    "🏥 I could ask other hospitals, but FL is off... *sad AI noises*",
    "🌟 Want stellar medical insights? Enable FL to access the constellation of knowledge!",
    "🎲 Rolling the dice... (Just kidding, enable FL for evidence-based analysis)",
    "🔍 Looking for answers with my tiny magnifying glass... FL would give me a telescope!"
]

def generate_medical_response(symptoms, age, gender):
    """Generate comprehensive medical response based on selected symptoms"""
    if not symptoms:
        return None
        
    # Find highest urgency level
    urgency_levels = [s["urgency"] for s in symptoms]
    highest_urgency = max(urgency_levels, key=lambda x: ["low", "moderate", "high", "immediate"].index(x))
    
    # Collect possible conditions
    possible_conditions = []
    for symptom in symptoms:
        possible_conditions.extend(symptom["associated_conditions"])
    
    # Calculate confidence and generate recommendations
    confidence_score = calculate_confidence_score(symptoms, age, gender)
    recommendations = generate_recommendations(symptoms, age, gender)
    
    response = {
        "urgency_level": highest_urgency,
        "possible_conditions": list(set(possible_conditions)),
        "confidence_score": confidence_score,
        "recommendations": recommendations,
        "similar_cases": random.randint(50, 200),
        "success_rate": random.randint(70, 90),
        "immediate_actions": get_immediate_actions(highest_urgency, symptoms)
    }
    
    return response

def calculate_confidence_score(symptoms, age, gender):
    """Calculate confidence score based on symptoms and patient factors"""
    base_score = 75
    symptom_count = len(symptoms)
    
    # Adjust for number of symptoms
    score_modifier = min(15, symptom_count * 3)
    
    # Age-based modification
    if age > 65 or age < 18:
        score_modifier -= 5
    
    final_score = base_score + score_modifier
    return min(95, max(60, final_score))

def get_immediate_actions(urgency, symptoms):
    """Generate immediate action recommendations based on urgency"""
    actions = {
        "immediate": [
            "🚨 SEEK EMERGENCY CARE IMMEDIATELY",
            "🚑 Call Emergency Services/911",
            "⚡ Do Not Delay Medical Care"
        ],
        "high": [
            "🏥 Urgent Medical Evaluation Required",
            "⚕️ Same-day Medical Assessment Needed",
            "📊 Close Monitoring of Vital Signs"
        ],
        "moderate": [
            "👨‍⚕️ Schedule Medical Evaluation",
            "📝 Monitor Symptoms Closely",
            "⏰ Follow-up Within 24-48 Hours"
        ],
        "low": [
            "📋 Monitor Symptoms",
            "📅 Schedule Routine Follow-up",
            "🏠 Implement Home Care Measures"
        ]
    }
    return actions.get(urgency, ["Seek Medical Advice"])

def generate_recommendations(symptoms, age, gender):
    """Generate specific recommendations based on patient factors"""
    recommendations = []
    
    # Age-specific recommendations
    if age > 65:
        recommendations.extend([
            "👴 Consider geriatric consultation",
            "📊 More frequent vital sign monitoring",
            "💊 Medication review recommended"
        ])
    elif age < 18:
        recommendations.extend([
            "👶 Pediatric evaluation recommended",
            "📈 Age-specific vital signs consideration",
            "👨‍👩‍👧‍👦 Parent/guardian education important"
        ])
    
    # Urgency-based recommendations
    if any(s["urgency"] == "immediate" for s in symptoms):
        recommendations.extend([
            "🚨 EMERGENCY CARE REQUIRED",
            "⚡ Time-critical intervention needed",
            "🚑 Emergency transport recommended"
        ])
    
    return recommendations

def main():
    st.set_page_config(page_title="FederiMed LLM", page_icon="🏥", layout="wide")
    
    # Initialize session state
    if 'federated_learning_active' not in st.session_state:
        st.session_state.federated_learning_active = False
    if 'random_response' not in st.session_state:
        st.session_state.random_response = random.choice(NON_FL_RESPONSES)

    # Main title with custom styling
    st.markdown("""
        <h1 style='text-align: center; color: #4A90E2; padding: 20px;'>
            🏥 FederiMed LLM Clinical Assistant
        </h1>
    """, unsafe_allow_html=True)

    # Sidebar configuration
    st.sidebar.markdown("""
        <div style='text-align: center'>
            <h2>System Configuration</h2>
        </div>
    """, unsafe_allow_html=True)

    # Enhanced toggle button
    col1, col2, col3 = st.sidebar.columns([1,2,1])
    with col2:
        if st.button(
            "🔄 Toggle Federated Learning",
            help="Enable/Disable Federated Learning capabilities",
            key="toggle_fl"
        ):
            st.session_state.federated_learning_active = not st.session_state.federated_learning_active
            st.session_state.random_response = random.choice(NON_FL_RESPONSES)

    # Status display
    if st.session_state.federated_learning_active:
        st.sidebar.success("🟢 Federated Learning Active")
        st.sidebar.markdown("""
            ```
            Network Status:
            ✓ 15 Regional Hospitals
            ✓ 3 University Centers
            ✓ 7 Specialty Clinics
            ✓ Real-time Learning Active
            ```
        """)
    else:
        st.sidebar.error("🔴 Basic Mode")
        st.sidebar.markdown(f"_{st.session_state.random_response}_")

    # Main interface
    st.markdown("### 👤 Patient Information")
    
    # Patient information in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        patient_age = st.number_input("Age", 0, 120, 45)
    with col2:
        patient_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with col3:
        patient_weight = st.number_input("Weight (kg)", 20, 200, 70)

    # Symptom selection interface
    st.markdown("### 🔍 Symptom Selection")
    
    # Create tabs for symptom categories
    selected_symptoms = []
    tabs = st.tabs(list(SYMPTOMS_DATABASE.keys()))
    
    for tab, (category, symptoms) in zip(tabs, SYMPTOMS_DATABASE.items()):
        with tab:
            st.markdown(f"**{category} Symptoms**")
            for symptom_id, details in symptoms.items():
                if st.checkbox(
                    f"{details['name']} ({details['urgency'].upper()})",
                    key=symptom_id,
                    help=f"Associated conditions: {', '.join(details['associated_conditions'])}"
                ):
                    selected_symptoms.append({
                        "id": symptom_id,
                        "name": details["name"],
                        "urgency": details["urgency"],
                        "associated_conditions": details.get("associated_conditions", [])
                    })

    # Analysis button
    if st.button("🔍 Analyze Symptoms", type="primary"):
        if not selected_symptoms:
            st.warning("⚠️ Please select at least one symptom for analysis")
            return

        with st.spinner("Processing clinical data..."):
            time.sleep(1.5)  # Simulate processing

            if not st.session_state.federated_learning_active:
                # Basic mode response
                st.error("⚠️ Limited Analysis Mode")
                st.markdown(f"### {st.session_state.random_response}")
                st.markdown("""
                    > 👉 **Tip:** Enable Federated Learning for comprehensive analysis!
                    
                    Basic recommendations:
                    - 📚 Consult standard medical guidelines
                    - 👨‍⚕️ Consider specialist referral
                    - 📋 Monitor symptoms closely
                """)
            else:
                # Generate federated learning response
                response = generate_medical_response(selected_symptoms, patient_age, patient_gender)
                
                # Display analysis results
                st.success("✅ Federated Analysis Complete")
                
                # Urgency alert
                urgency_colors = {
                    "immediate": "🔴 IMMEDIATE MEDICAL ATTENTION REQUIRED",
                    "high": "🟠 HIGH URGENCY - Prompt Medical Care Needed",
                    "moderate": "🟡 Moderate Urgency - Soon Medical Attention",
                    "low": "🟢 Routine Care Appropriate"
                }
                st.markdown(f"### {urgency_colors.get(response['urgency_level'], 'Urgency Unknown')}")
                
                # Display metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Analysis Confidence", f"{response['confidence_score']}%")
                with col2:
                    st.metric("Similar Cases", response['similar_cases'])
                with col3:
                    st.metric("Treatment Success Rate", f"{response['success_rate']}%")
                
                # Immediate actions
                st.markdown("### ⚡ Immediate Actions")
                for action in response['immediate_actions']:
                    st.markdown(f"- {action}")
                
                # Possible conditions
                st.markdown("### 📋 Possible Conditions")
                for condition in response['possible_conditions']:
                    st.markdown(f"- {condition}")
                
                # Recommendations
                st.markdown("### 💡 Recommendations")
                for rec in response['recommendations']:
                    st.markdown(f"- {rec}")
                
                # Data sources
                with st.expander("📊 Data Sources"):
                    st.code("""
                    Analysis based on:
                    - 15 Regional Hospitals
                    - 3 University Medical Centers
                    - 7 Specialty Clinics
                    - 200,000+ Similar Cases
                    - Real-time Learning System
                    """)



if __name__ == "__main__":
    main()
