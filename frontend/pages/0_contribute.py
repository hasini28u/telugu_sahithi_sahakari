import os
import requests
import streamlit as st
from requests_toolbelt.multipart.encoder import MultipartEncoder

# --- Configuration ---
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
UPLOAD_ENDPOINT = f"{BACKEND_URL}/upload/"
CATEGORIES_ENDPOINT = f"{BACKEND_URL}/categories/"

# --- Helper Function ---
@st.cache_data
def fetch_categories():
    """Fetches the list of categories from our backend."""
    try:
        token = st.session_state.get("access_token")
        if not token:
            return []

        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(CATEGORIES_ENDPOINT, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        st.error("Error: Could not connect to the backend. Is it running?")
        return []

# --- Main Application UI ---
st.set_page_config(page_title="తెలుగు సాహితీ సహకారి", page_icon="📖")
st.title("📖 తెలుగు సాహితీ సహకారి - Contribute Literature")
st.markdown("Upload your Telugu literature, documents, and books to our community-powered archive.")

if not st.session_state.get("logged_in", False):
    st.warning("Please log in to contribute.")
else:
    token = st.session_state["access_token"]
    categories = fetch_categories()

    if categories:
        category_map = {cat["name"]: cat["id"] for cat in categories}

        with st.form("upload_form", clear_on_submit=True):
            st.subheader("Record Details")
            title = st.text_input(
                "Title of the work", placeholder="e.g., 'Kavitrayam: Mahabharatam'"
            )
            selected_category_name = st.selectbox(
                "Category", options=list(category_map.keys())
            )

            # --- TABS FOR UPLOAD OPTIONS ---
            tab1, tab2, tab3 = st.tabs(["📁 File Upload", "📸 Camera Input", "📝 Text Input"])

            final_file = None
            final_text = None

            with tab1:
                uploaded_file = st.file_uploader(
                    "Choose a file (PDF, JPG, PNG)", type=["pdf", "png", "jpg", "jpeg"]
                )
                if uploaded_file is not None:
                    final_file = uploaded_file

            with tab2:
                camera_file = st.camera_input("Take a picture of the document")
                if camera_file is not None:
                    final_file = camera_file
            
            with tab3:
                text_input = st.text_area("Enter your content here", height=300)
                if text_input:
                    final_text = text_input

            language = st.selectbox("Language", options=["telugu", "sanskrit", "english"])
            
            release_options = ["creator", "family_or_friend", "downloaded", "NA"]
            release_rights = st.selectbox("Release Rights", options=release_options)

            submitted = st.form_submit_button("Upload Record")

            if submitted:
                if not title:
                    st.warning("Please provide a title.")
                elif final_file is None and not final_text:
                    st.warning("Please upload a file, take a picture, or enter text.")
                else:
                    with st.spinner(f"Uploading..."):
                        category_id = category_map[selected_category_name]
                        
                        try:
                            # Use a special file-like object for text input
                            if final_text:
                                text_file = {
                                    "title": title,
                                    "category_id": category_id,
                                    "release_rights": release_rights,
                                    "language": language,
                                    "file": ("text_input.txt", final_text, "text/plain")
                                }
                                response = requests.post(
                                    UPLOAD_ENDPOINT, data=text_file, headers={"Authorization": f"Bearer {token}"}
                                )
                            else:
                                m = MultipartEncoder(
                                    fields={
                                        "title": title,
                                        "category_id": category_id,
                                        "release_rights": release_rights,
                                        "language": language,
                                        "file": (final_file.name, final_file.getvalue(), final_file.type),
                                    }
                                )

                                headers = {
                                    "Authorization": f"Bearer {token}",
                                    "Content-Type": m.content_type,
                                }

                                response = requests.post(
                                    UPLOAD_ENDPOINT, data=m, headers=headers
                                )

                            if response.status_code == 200:
                                st.success("✅ Upload successful! The document will be processed shortly.")
                                st.json(response.json())
                            else:
                                st.error("❌ Upload failed.")
                                st.json(response.json())
                        except requests.exceptions.RequestException as e:
                            st.error(f"Connection to backend failed: {e}")
