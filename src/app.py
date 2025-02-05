import streamlit as st
from utils import evaluate_password

st.title("🔐 Password Strength Checker")
st.write("Enter a password to evaluate its security.")

password = st.text_input("🔑 Enter your password:", type="password")

if password:
    score, criteria = evaluate_password(password)
    
    st.subheader("Password Strength Evaluation")
    st.write(f"✅ Strength Score: **{score}/5**")

    st.write("🔍 **Criteria Breakdown:**")
    for key, value in criteria.items():
        st.write(f"- {'✅' if value else '❌'} {key.replace('_', ' ').capitalize()}")

    if score < 3:
        st.warning("⚠️ Your password is weak! Consider using more characters, numbers, and special symbols.")
    elif score < 5:
        st.info("ℹ️ Your password is decent but could be stronger.")
    else:
        st.success("🎉 Your password is strong!")
