import streamlit as st

# App title and header
st.set_page_config(page_title="Agent Floral – Credit Repair AI", layout="centered")
st.title("🌸 Meet Agent Floral")
st.subheader("Your AI Partner in Credit Repair & Financial Solutions")

# Agent introduction
st.markdown("""
Agent Floral is the intelligent, always-on AI agent built to support the mission of **Guaranteed Financial Solutions**.

She's not just a bot – she's your reliable, knowledgeable assistant for everything related to:

✅ Credit Repair Sales  
✅ Credit Dispute Assistance  
✅ Customer Support & Education  
✅ Lead Qualification & Service Recommendations  
✅ Compliance-Backed Credit Restoration

""")

# Purpose section
st.markdown("### 💡 Why Agent Floral Exists")
st.markdown("""
Agent Floral was created to serve individuals and families across the United States with a personal touch, backed by legal, ethical, and effective credit restoration strategies.  
Her job is to **help people take back control of their financial story** – and feel empowered doing it.
""")

# Core features
st.markdown("### 🔧 What Agent Floral Can Do")

features = [
    "Answer client questions about credit reports, scores, and disputes",
    "Guide new leads through the onboarding process",
    "Provide updates on credit repair progress",
    "Educate clients about FCRA, FDCPA, and their legal rights",
    "Qualify leads for services and explain pricing",
    "Set up appointments with real representatives when needed"
]

for f in features:
    st.markdown(f"- {f}")

# Footer and call-to-action
st.markdown("---")
st.success("Agent Floral is here to serve – with compassion, clarity, and credit expertise. 💼✨")

st.markdown("📞 Need support building out your AI workflows or connecting Agent Floral to your CRM or chat system? Contact the Guaranteed Financial Solutions team for assistance.")

