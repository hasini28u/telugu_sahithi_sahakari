# తెలుగు సాహితీ సహకారి (Telugu Sahiti Sahakari)
A community-powered AI archive focused on preserving and promoting Telugu literary heritage. Users can upload diverse literary materials, which are digitized, processed with AI for text extraction and semantic organization, and made searchable via an interactive chatbot and search engine. The project contributes to open Telugu and English language research at [corpus.swecha.org].


# Features

  
  - User Authentication: Secure login with mobile number and password.
  
  - Literature Upload: Upload files (PDF, JPG, PNG), images via camera, or type content directly.
  
  - Categorization: Tag contributions with relevant literary categories for better organization.
  
  - AI-Powered Pipeline: OCR and generative AI clean and structure the uploaded texts.
  
  - Semantic Search: Search documents via vector embeddings (using FAISS).
  
  - Telugu Chatbot: Conversational answers to Telugu literature questions.
  
  - Open Dataset Contribution: Adds to the Swecha Corpus, facilitating linguistic research.



# Technology Stack


  - Frontend: Streamlit
  
  - Backend: FastAPI
  
  - Database: PostgreSQL (Supabase)
  
  - AI/NLP: Google Generative AI (Gemini), EasyOCR, LangChain
  
  - Semantic Search: FAISS
  
  - Authentication: JWT, OAuth2



# File Structure

    backend/
    │
    ├─ core/
    │ ├─ __init__.py
    │ ├─ settings.py
    │
    ├─ services/
    │ ├─ __init__.py
    │ ├─ corpus_api.py
    │ ├─ vector_store.py
    │ ├─ main.py
    │
    frontend/
    │ ├─ pages/
    │ │ ├─ 0_contribute.py
    │ │ ├─ 1_Login.py
    │ │ ├─ 2_telugu_chatbot.py
    │ ├─ app.py
    ├─ .gitignore
    ├─ pyproject.toml
    ├─ requirements.txt




# Setup & Usage

  1. Clone the repository
  
  git clone https://code.swecha.org/ananyakrishna/telugu_sahithi_sahakaari.git
  cd telugu-sahiti-sahakari/backend
  
  
  
  2. Install dependencies
  
  pip install -r requirements.txt
  
  
  
  3. Configure environment
  Create a .env file in the backend directory, and set the following:
  
  DATABASE_URL=postgresql://username:password@localhost:5432/yourdb
  GEMINI_API_KEY=your-google-gemini-api-key
  CORPUS_API_BASE_URL=https://api.corpus.swecha.org
  CORPUS_API_TOKEN=your-corpus-api-token
  
  
  
  4. Run the backend server
  
  uvicorn backend.core.main:app --reload
  
  
  
  5. Launch the Streamlit frontend
  
  streamlit run frontend/app.py
  
  
  
  6. Access the application
  Go to: http://localhost:8501


# Key Modules
    
    
    
  Module Description
  
  
  
  
  app.py
  Main frontend launcher, project intro, styling, top-level UI
  
  
  pages/0_contribute.py
  Literature upload UI: file, camera, text input, category selection
  
  
  pages/1_Login.py
  User login/logout UI, session and token management
  
  
  pages/2_telugu_chatbot.py
  Chatbot UI for conversational Telugu literature questions
  
  
  main.py
  FastAPI backend application, API routing, endpoints, document pipeline
  
  
  services/corpus_api.py
  Handles external API communication (Swecha Corpus API, uploads, metadata)
  
  
  services/vector_store.py
  In-memory FAISS vector store for semantic chunking and search
  
  
  core/settings.py
  Loads environment variables for central configuration




# Contribution Guidelines

  Fork the repo, make feature or fix branches, and submit pull requests.
  Ensure code is thoroughly tested and well documented.
  Help expand the open Telugu literature dataset for NLP research.



# License
  Open source project supporting free research and preservation of Telugu language and culture.
