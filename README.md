# ReACt_Custom_AI_Agent_in_Python

## Overview
This project implements a custom AI agent using the ReACt (Reasoning and Action in Python. The agent can perform various tasks such as Wikipedia searches, blog searches, and arithmetic calculations by leveraging different tools.

## Features
- **Reasoning and Action-based AI**: The agent follows a structured protocol to analyze queries and execute actions.
- **Advanced Query Processing**: Supports multi-step reasoning and validation of facts.
- **Context-Aware Responses**: Provides accurate and contextually relevant answers.
- **Document Analysis & Insights**: Capable of extracting and summarizing information from documents.

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)
- [httpx](https://www.python-httpx.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/SURESHBEEKHANI/ReACt_Custom_AI_Agent_in_Python.git
    cd ReACt_Custom_AI_Agent_in_Python
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add your environment variables:
    ```env
    GROQ_API_KEY=your_groq_api_key
    ```

## Running the Application

### Backend (FastAPI)
1. Navigate to the project root directory.
2. Run the FastAPI server:
    ```sh
    uvicorn backend:app --reload --host 127.0.0.1 --port 9999
    ```

### Frontend (Streamlit)
1. Open a new terminal and navigate to the project root directory.
2. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

### Jupyter Notebook
1. Navigate to the `research` directory.
2. Open the Jupyter notebook:
    ```sh
    jupyter notebook ReACt_Custom_AI_Agent.ipynb
    ```

## Usage
- Access the Streamlit app at `http://localhost:8501` to interact with the AI agent.
- Use the FastAPI Swagger UI at `http://localhost:9999/docs` to test the API endpoints.

## Project Structure
- `src/Tools.py`: Contains the action functions for Wikipedia search, blog search, and arithmetic calculations.
- `src/prompt.py`: Defines the prompt used by the AI agent.
- `backend.py`: Implements the FastAPI backend.
- `app.py`: Implements the Streamlit frontend.
- `agent.py`: Contains the main logic for the AI agent.
- `research/ReACt_Custom_AI_Agent.ipynb`: Jupyter notebook for research and testing.

## License
This project is licensed under the MIT License.