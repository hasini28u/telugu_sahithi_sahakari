import requests
import streamlit as st

# --- Configuration ---
BACKEND_URL = "http://127.0.0.1:8000"
TOKEN_ENDPOINT = f"{BACKEND_URL}/token"

st.set_page_config(page_title="Login", page_icon="🔑")
st.title("🔑 Login")
st.subheader("Sign in to your account")

# --- Login Form ---
with st.form("login_form"):
    mobile_number = st.text_input(
        "Enter 10-digit phone number",
        placeholder="9876543210",
        max_chars=10,
        key="mobile",
    )
    password = st.text_input("Password", type="password", key="password")
    submitted = st.form_submit_button("Login")

if submitted:
    if not mobile_number or not password:
        st.warning("Please enter both mobile number and password.")
    elif not mobile_number.isdigit() or len(mobile_number) != 10:
        st.error("Please enter a valid 10-digit mobile number.")
    else:
        with st.spinner("Authenticating..."):
            try:
                # Add the +91 prefix to the mobile number
                full_mobile_number = f"+91{mobile_number}"

                # Our backend's /token endpoint expects 'username' and 'password' in a form-data format.
                login_data = {"username": full_mobile_number, "password": password}

                response = requests.post(TOKEN_ENDPOINT, data=login_data)

                if response.status_code == 200:
                    token_data = response.json()

                    # Store the token in the session state to keep the user logged in
                    st.session_state["access_token"] = token_data["access_token"]
                    st.session_state["token_type"] = token_data["token_type"]
                    st.session_state["logged_in"] = True

                    st.success("Login successful!")
                    st.rerun()  # Rerun the script to update the UI
                else:
                    st.error("Login failed. Please check your credentials.")
                    st.json(response.json())

            except requests.exceptions.RequestException as e:
                st.error(f"Connection to backend failed: {e}")

# --- Logout Button ---
if st.session_state.get("logged_in", False):
    st.write("---")
    if st.button("Logout"):
        # Clear all session state keys to log the user out
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.success("You have been logged out.")
        st.rerun()