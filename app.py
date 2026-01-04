import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday Maida!",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600;700&display=swap');

    .stApp {
        background: linear-gradient(45deg, #ffafcc, #cdb4db, #a2d2ff);
        animation: gradient 15s ease infinite;
        background-size: 400% 400%;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .birthday-title {
        font-family: 'Dancing Script', cursive;
        font-size: 4rem !important;
        color: #ff4d8d !important;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px !important;
    }

    .message-box {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 20px;
        border-left: 5px solid #ffafcc;
        border-right: 5px solid #a2d2ff;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        line-height: 1.8;
        color: #333;
    }

    .stButton > button {
        background: linear-gradient(45deg, #ffafcc, #ff4d8d);
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 15px 30px;
        border-radius: 50px;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
        font-family: 'Poppins', sans-serif;
    }

    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 20px rgba(255, 77, 141, 0.25);
    }

    .surprise-section {
        background: linear-gradient(135deg, #f9f0ff 0%, #e6f7ff 100%);
        padding: 25px;
        border-radius: 20px;
        margin: 25px 0;
        border: 1px solid #e0e7ff;
    }

    .gift-animation {
        text-align: center;
        font-size: 3.5rem;
        margin: 20px 0;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .countdown-box {
        background: linear-gradient(45deg, #ff6b9d, #ff8e53);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
        font-family: 'Poppins', sans-serif;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("<h1 class='birthday-title'>Happy Birthday, Maida!</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-family: Poppins; color: #9d4edd; font-size: 1.2rem; margin-bottom: 30px;'>Wishing you the most wonderful day</p>",
    unsafe_allow_html=True)

# Main message in a styled box
st.markdown("""
<div class="message-box">
    <div style="font-size: 1.2rem; color: #7209b7; text-align: center; margin-bottom: 20px; font-weight: 600;">
        So Pookie Maida
    </div>
""", unsafe_allow_html=True)

# First paragraph
st.markdown("""
<div style="color: #555; margin-bottom: 15px; font-family: Poppins;">
    I hope you like this type of wish hehe so,I'm honestly so grateful for all the laughs, fun, and memories we share and yes agy bhi krty rhiengy hehe.
</div>
""", unsafe_allow_html=True)

# Second paragraph
st.markdown("""
<div style="color: #555; margin-bottom: 15px; font-family: Poppins;">
    Pookie khy sath thora sa bhi time guzry mela bht maza ata sae shugal lgta kher.
</div>
""", unsafe_allow_html=True)

# Prayer section
st.markdown("""
<div style="background: #f0f7ff; padding: 15px; border-radius: 10px; margin: 15px 0; border-left: 4px solid #4361ee;">
    <div style="color: #2a4d8f; font-weight: 600; margin-bottom: 8px; font-family: Poppins;">I pray that:</div>
    <div style="color: #4361ee; font-family: Poppins;">
        May Allah always keep you happy, protect you, and grant you success in everything. Ameen.
        May you achieve all your dreams and may your life always remain as sweet and beautiful as you are.
    </div>
</div>
""", unsafe_allow_html=True)

# Final wish
st.markdown("""
<div style="color: #4361ee; margin-top: 20px; text-align: center; font-weight: 600; font-family: Poppins;">
    Wishing you all the happiness and blessings in the world today and always.
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Close the message-box div

# Surprise Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    button_clicked = st.button("Discover Your Birthday Surprise")

# Display content based on button click
if button_clicked:
    # --- UPDATED LOCAL AUDIO LOGIC ---
    try:
        audio_file = open('videoplayback.mp4', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
    except FileNotFoundError:
        st.error("Wait! Please make sure 'latina.mp3' is in your PyCharm project folder.")
    # Balloons and snow animations
    st.balloons()
    st.snow()

    # Clear the previous content area
    st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)

    # Surprise Section
    st.markdown("""
    <div class="surprise-section">
        <div style="text-align: center; margin-bottom: 25px;">
            <h2 style="color: #ff4d8d; font-family: 'Dancing Script', cursive; font-size: 2.5rem;">
                A Special Message For You
            </h2>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # First message in surprise section
    st.markdown("""
    <div style="color: #555; margin-bottom: 20px; font-family: Poppins; padding: 0 10px;">
        you are sweetest pookie i got. I'll always be here to support you and always stand with you .
    </div>
    """, unsafe_allow_html=True)

    # Gift message box
    st.markdown("""
    <div style="background: #fff0f5; padding: 15px; border-radius: 10px; margin: 15px 0; border: 1px solid #ffd1dc;">
        <div style="color: #d81b60; font-weight: 600; text-align: center; font-family: Poppins;">
            Gifts Tiyar hain apky .
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Final birthday wish
    st.markdown("""
    <div style="color: #555; margin-top: 20px; text-align: center; font-family: Poppins; padding: 0 10px;">
        Once again, happy birthday. May this day become an unforgettable memory for you.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # Close the surprise-section div

    # Gift Animation
    st.markdown('<div class="gift-animation">🎁</div>', unsafe_allow_html=True)

    # Countdown
    st.markdown("""
    <div class="countdown-box">
        <h3 style="margin-bottom: 15px; color: white;">Birthday Celebration Countdown</h3>
    </div>
    """, unsafe_allow_html=True)

    countdown_placeholder = st.empty()
    for i in range(3, 0, -1):
        countdown_placeholder.markdown(f"""
        <div style="text-align: center; font-family: Poppins; font-size: 3rem; color: #ff4d8d; font-weight: bold;">
            {i}
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)

else:
    # Initial message when page loads
    st.markdown("""
    <div style="text-align: center; padding: 20px; margin: 30px 0; background: rgba(255, 255, 255, 0.9); border-radius: 15px;">
        <p style="color: #6b7280; font-size: 1.1rem; font-family: Poppins;">
            A beautiful surprise is waiting for you. Click the button above to reveal it!
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>Made with heartfelt wishes for Maida's pookie </p>
    <p style="margin-top: 5px; opacity: 0.8;">© Created with love and mehnat by teddy</p>
</div>
""", unsafe_allow_html=True)