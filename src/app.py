import streamlit as st
from utils import evaluate_password
from utils import is_common_password
from utils import check_password_breach
from utils import calculate_entropy
from utils import provide_password_feedback

st.title("🔐 Password Strength Checker")
st.write("Enter a password to evaluate its security.")

password = st.text_input("🔑 Enter your password:", type="password")

if password:
    if is_common_password(password):
        st.error("🚨 Your password is **too common**! Choose a more secure password.")

    breach_message = check_password_breach(password)
    if "leaked" in breach_message:
        st.error(breach_message)
    else:
        st.success(breach_message)

    entropy, entropy_feedback = calculate_entropy(password)
    
    st.subheader("📊 Entropy Calculation")
    st.write(f"**Entropy Score:** `{entropy}` bits")
    st.write(entropy_feedback)

    score, criteria = evaluate_password(password)
    
    st.subheader("🔍 Password Strength Evaluation")
    st.write(f"✅ Strength Score: **{score}/5**")

    st.write("🔹 **Criteria Breakdown:**")
    for key, value in criteria.items():
        st.write(f"- {'✅' if value else '❌'} {key.replace('_', ' ').capitalize()}")

    # New feature: Provide feedback
    feedback = provide_password_feedback(password)
    if feedback:
        st.subheader("💡 Suggestions to Improve Your Password")
        for tip in feedback:
            st.write(f"- {tip}")

    if score < 3:
        st.warning("⚠️ Your password is weak! Consider using more characters, numbers, and special symbols.")
    elif score < 5:
        st.info("ℹ️ Your password is decent but could be stronger.")
    else:
        st.success("🎉 Your password is strong!")
