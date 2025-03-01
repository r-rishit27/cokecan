import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from groq import Groq  # Import Groq SDK
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GROQ_API_KEY = "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"

groq_client = Groq(api_key=GROQ_API_KEY)

# Function to calculate surface area
def surface_area(r, volume):
    h = volume / (np.pi * r**2)
    return 2 * np.pi * r**2 + 2 * np.pi * r * h

#design optimization function
def optimize_can(volume, max_diameter):
    result = minimize_scalar(surface_area, bounds=(0.1, max_diameter/2), args=(volume,), method='bounded')
    r_opt = result.x
    h_opt = volume / (np.pi * r_opt**2)
    return r_opt, h_opt, surface_area(r_opt, volume)



# AI Reasoning with Groq
def generate_ai_reasoning(volume, r_opt, h_opt):
    prompt = f"""
    Given a cylindrical can with volume {volume} mL, the optimal radius is {r_opt:.2f} cm and height is {h_opt:.2f} cm.
    Make calculations and optimize the design that minimizes material cost and enhances ergonomics ,
    Consider aspects such as:
    - Material efficiency in reducing waste
    - Stability and ease of gripping
    - Manufacturing feasibility
    - Impact on branding and aesthetics
    give response in form of summary report.
    keep report short summarize and siple and presnt it in tabular format for diffrent design aspect cost ,ergonomics and ballance approch,be consistent in calcluation and approch 
    """
    try:
        response = groq_client.chat.completions.create(
            model="deepseek-r1-distill-qwen-32b",  # Use an optimized model for inference
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content if response.choices else "AI reasoning unavailable."
    except Exception as e:
        return "AI reasoning unavailable."

# Streamlit UI
st.set_page_config(page_title="Coke Can Optimizer", layout="wide")
st.title("🛠️ Coke Can Optimizer")
st.write("### Optimize a Coke can design for cost-effectiveness, comfort, and efficiency.")


tabs = st.tabs(["📏 Design Inputs", "📊 Results & AI Insights"])

with tabs[0]:
    st.subheader("Design Parameters")
    volume = st.number_input("Enter minimum capacity (mL):", min_value=500, value=500, step=50)
    max_diameter = st.slider("Max comfortable diameter (cm):", min_value=3.0, max_value=8.0, value=7.0, step=0.1)
    optimize_button = st.button("🔍 Optimize Can Design")

if optimize_button:
    volume_cm3 = volume
    r_opt, h_opt, sa_opt = optimize_can(volume_cm3, max_diameter)
    ai_reasoning = generate_ai_reasoning(volume, r_opt, h_opt)
    
    with tabs[1]:
        st.success(f"""
            **Optimized Can Design:**  
            - **Radius:** {r_opt:.2f} cm  
            - **Height:** {h_opt:.2f} cm  
            - **Surface Area:** {sa_opt:.2f} cm²  
        """)
        
        # LaTeX representation of equations and ai driven design reasoning report 
        st.write("### 🧠 AI Reasoning:")
        st.code(ai_reasoning, language='latex')
        
        
        st.write("### 📐 Mathematical Formulation")
        st.latex(r"h = \frac{V}{\pi r^2}")
        st.latex(r"SA = 2\pi r^2 + 2\pi r h")
        
        # Visualization
        st.write("### 🏗️ Can Design Visualization")
        fig, ax = plt.subplots(figsize=(2, 3))
        rect = plt.Rectangle((-r_opt, 0), 2*r_opt, h_opt, color='r', fill=False, linewidth=1)
        ax.add_patch(rect)
        ax.set_xlim(-max_diameter/2, max_diameter/2)
        ax.set_ylim(0, h_opt * 1.2)
        ax.set_aspect('equal')
        ax.set_title("Optimized Can Shape")
        st.pyplot(fig)
