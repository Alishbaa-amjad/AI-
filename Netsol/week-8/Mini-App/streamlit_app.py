import streamlit as st
import requests

API_URL = "http://127.0.0.1:6000"

# 1. Page Configuration
st.set_page_config(
    page_title="AI Student Predictor",
    page_icon="🎓",
    layout="centered"
)

# 2. Custom CSS for "Enhanced" Look
st.markdown("""
    <style>
    /* Button styling */
    .stButton>button {
        border-radius: 20px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        transition: 0.3s;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    /* Main container background */
    .stApp {
        background-color: #f8f9fa;
    }
    /* Title styling */
    h1 {
        color: #2e4053;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.title("🎓 Student Success Predictor")
st.markdown("<p style='text-align: center; color: grey;'>Using Machine Learning to forecast academic outcomes</p>", unsafe_allow_html=True)

# 4. Sidebar Inputs (Instead of main page for cleaner look)
with st.sidebar:
    st.header("⚙️ Adjustment Panel")
    st.info("Adjust the sliders to update the prediction inputs.")
    
    study_hours = st.slider(
        "Study Hours Per Day", 0.0, 10.0, 4.0, 0.5,
        help="How many hours the student studies each day"
    )
    
    prev_score = st.slider(
        "Previous Exam Score", 0.0, 100.0, 60.0, 1.0,
        help="Score from the most recent exam"
    )
    
    st.divider()
    st.write("Current Settings:")
    st.caption(f"📚 Hours: {study_hours}")
    st.caption(f"📝 Score: {prev_score}")

# 5. Main Dashboard (Summary Cards)
st.subheader("📊 Input Summary")
m1, m2 = st.columns(2)
with m1:
    st.metric("Study Discipline", f"{study_hours} hrs", delta="Target: 6.0")
with m2:
    st.metric("Academic Standing", f"{prev_score}%", delta="Target: 70%")

st.markdown("---")

# 6. Prediction Logic with Enhanced UI
if st.button("🚀 Predict Result", use_container_width=True):
    try:
        response = requests.post(
            f"{API_URL}/predict",
            json={"study_hours": study_hours, "prev_score": prev_score}
        )
        
        if response.status_code == 200:
            result = response.json()
            
            # Create a nice container for the result
            with st.container():
                st.markdown("### 🔍 AI Analysis Report")
                
                if result["prediction"] == 1:
                    st.balloons() # Victory animation
                    st.success(f"## ✅ Result: {result['result_label']}")
                    st.write("This student is on the right track! Keeping this pace ensures success.")
                    
                else:
                    st.snow() # Warning animation
                    st.error(f"## ❌ Result: {result['result_label']}")
                    st.warning("Needs improvement. Consider increasing study hours.")

                # Confidence Gauge
                confidence = result['confidence'] * 100
                st.write(f"**Model Confidence:** {confidence:.1f}%")
                st.progress(int(confidence))
                
                # Debug Info in Expander
                with st.expander("🛠️ Technical Data"):
                    st.json(result)
        else:
            st.warning("⚠️ Connection Error: FastAPI is not responding.")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("<br><br><footer style='text-align: center; color: silver;'>Built with FastAPI & Streamlit</footer>", unsafe_allow_html=True)
