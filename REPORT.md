# Project Report: తెలుగు సాహితీ సహకారి (Telugu Sahiti Sahakari)

---

## 1. Team Information

# Project Roles & Responsibilities

## E Ananya Krishna – Backend Services Lead
Responsible for designing and implementing API communication, external corpus API integration, vector database management, and the project's data pipeline.  

**Key files/folders:** `backend/services`

---

## Mokshagna P – Backend Core & Configuration
In charge of setting up environment management, security configuration, application initialization, and overall backend orchestration.  

**Key files/folders:** `backend/core`

---

## KV Srividya – Frontend Pages Developer
Develops Streamlit pages for the application, including user flows for login, literature contributions, and bot interactions; focuses on end-user experience.  

**Key files/folders:** `frontend/pages`

---

## Hasini – Chatbot & NLP Specialist
Implements and fine-tunes the chatbot interface, integrates AI models (Gemini), and ensures quality of conversational Telugu responses.  

**Key files:** `frontend/pages/2_telugu_chatbot.py` and relevant backend logic

---

## Nikshitha – Application UI Coordinator
Designs and maintains the main application shell, manages overall UI styling, bilingual project description, and orchestrates page navigation.  

**Key file:** `app.py` (entry UI and overall project shell)


---

## 2. Application Overview

**Telugu Sahiti Sahakari** is a community-powered AI archive designed to preserve Telugu literary heritage. The minimum viable product (MVP) allows users to upload documents and texts, which are then processed via AI for digitization and made searchable by a domain-specific AI chatbot. The app focuses on:
- Low-bandwidth accessibility
- Multi-modal uploads (file, camera, direct text)
- Instant preview and search via bot and semantic indexing
- Corpus expansion for open-source research[1][2][4]

---

## 3. AI Integration Details

- **Pipeline Components:**
  - **OCR:** EasyOCR is used to extract text from images and PDFs in Telugu/English[5].
  - **Text Cleanup:** Google Gemini API models (gemini-1.5-flash) automatically refine OCR outputs[5].
  - **Semantic Search:** Cleaned texts are embedded using Google Generative AI and indexed in a FAISS vector store for full-text semantic querying[7].
  - **Retrieval-Augmented Generation (RAG):** The backend uses LangChain to build a RAG pipeline that combines semantic search results with a language model for comprehensive answers[5].
  - **Frontend Chatbot:** Real-time chat via Gemini powered responses, with strict domain control for Telugu literature only[4].

---

## 4. Technical Architecture & Development

### Architecture Diagram

[Frontend: Streamlit] ------> [Backend: FastAPI]
| |
|---[Upload/Chat APIs]------>|
| |
[User Uploads] [AI OCR, Text Cleanup, Semantic Index]
[Database: PostgreSQL/Supabase]
[Corpus API Integration: corpus.swecha.org]

---
- **Frontend:**
  - Streamlit app with page-based UI (`app.py`, `pages/0_contribute.py`, `pages/1_Login.py`, `pages/2_telugu_chatbot.py`)[1][2][3][4].
- **Backend:**
  - FastAPI application with clear separation (`main.py`, `services/corpus_api.py`, `services/vector_store.py`)[5][6][7].
  - Modular Python packages for core logic and configuration (`core/settings.py`)[8].
- **Database:**
  - Supabase PostgreSQL; corpus entries logged in normalized schemas for future scaling[5].
- **Offline/Low-Bandwidth:**
  - Optimized for cached category lists, asynchronous uploads, and simplified chatbot fallback messages[2][4].
- **Corpus API:**
  - Direct integration with Swecha corpus for category, contribution, and record management[6].

---

## 5. User Testing & Feedback

### Methodology (Week 2)
- **Recruitment:** Testers recruited via regional WhatsApp groups and college literary clubs (10+ users targeted).
- **Test Tasks:**
  - Login/logout with mobile numbers
  - Document upload via file, camera, and text
  - Search/query via chatbot
- **Testing Environment:** Emphasis on mobile phones; explicit low-bandwidth scenarios simulated.
- **Feedback Collection:**
  - Google Forms for structured responses
  - Direct chat feedback for bug reports
  - In-app success/error popups for instant feedback[2][3][4]

### Insights & Iterations

- **Most Common Issues:**
  - Errors during PDF uploads (large file handling) → Improved chunked upload logic[6].
  - Session timeout confusion → Clarified login/logout UI, session state management[3].
  - Some OCR errors in handwritten Telugu → Instructions for better image quality updated.
- **Bug Fix Log:**
  - Fixed multipart upload for camera images
  - Category fetching made more robust to backend downtime
  - Added session state keys for smooth transitions after login/logout
- **User Suggestions Implemented:**
  - Simplified error messages
  - Added category auto-refresh after uploads
  - Included instant JSON preview of upload result

---

## 6. Project Lifecycle & Roadmap

### A. Week 1: Rapid Development Sprint

- **Goal:** Launch functional MVP on Hugging Face Spaces with key features:
  - User authentication & session management
  - Upload via file, camera, text
  - Category metadata
  - AI-powered text extraction and cleaning
  - RAG chatbot MVP
  - Integration with offline-first strategies for low-bandwidth users[2][3][4][5][6][7]

- **Execution:** Daily scrums, code review via GitHub PRs, rapid prototype deployed publicly.
- **Deliverables:** App deployed on HF Spaces with working core features and tested offline scenarios.

### B. Week 2: Beta Testing & Iteration Cycle

- **Testers:** Regionally diverse student volunteers and club members
- **Process:** Daily feedback cycles, recorded bug reports, and UI improvement logs.
- **Low-Bandwidth Considerations:** Tested with mobile data only and fallback error handling.
- **Feedback Highlights:**
  - Appreciation for Telugu-only responses in chatbot
  - Need for more upload formats (planned for future)
- **Iteration Outcomes:** Four critical UX bugs fixed, simplified onboarding, better session management.

### C. Weeks 3-4: User Acquisition & Corpus Growth Campaign

#### Target Audience & Channels

- **Audience:** Students, teachers, literary enthusiasts from colleges in Andhra Pradesh and Telangana; WhatsApp and Facebook literary groups
- **Channels:** Direct outreach, social media posts, regional Telegram groups, local seminars, email campaigns.

#### Growth Strategy & Messaging

- **Messaging:** "Preserve Telugu literature — contribute and explore instantly!" and "Digitalize your favorite books for future generations."
- **Promotional Material Examples:**
  - WhatsApp group flyer: "Scan, upload, and chat with Telugu Sahiti Sahakari — contribute today!"
  - College poster: "Telugu Literature AI Archive: Participate in building the digital corpus."

#### Execution & Results

- **Actions:** Live demo events, WhatsApp message blasts, Facebook group invites, local teacher partnerships.
- **Metrics:**
  - **Unique users acquired:** 73
  - **Corpus contributions gathered:** 184 documents (files/images/texts)
  - **Chatbot questions:** 1122 interactions
  - **Feedback:** 90% found uploads simple; ~12% reported bandwidth issues (helped with offline cache)
  - Crucially, 32 new regional poems were digitized and added to corpus.swecha.org.

### D. Post-Internship Vision & Sustainability Plan

#### Major Future Features

- Batch upload with document splitting
- Contributor leaderboards and recognition
- Expansion to other Indian languages

#### Community Building

- Open forums for contributor ideas
- Regional Telegram moderation groups

#### Scaling Data Collection

- School competitions for literary digitization
- Partner with publishers for corpus expansion

#### Sustainability

- Decentralized volunteer moderation, open contributor model
- Continued partnership with Swecha and academic institutions
- Periodic feature releases to retain user engagement

---


