from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv
from agent import query  # Import query function from agent.py

# Load environment variables from .env file
load_dotenv()

# Create FastAPI app instance
app = FastAPI(title="Agent")

# Define a Pydantic model for request validation
class RequestState(BaseModel):
    messages: List[str]  # List of messages from the user

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    """
    API Endpoint to interact with the chatbot.
    """
    query_text = request.messages[0]  # Use the first message as the query

    # Call the AI agent function to process the query
    response = query(query_text)  # Assuming `query()` is defined in agent.py
    
    # Return the AI-generated response
    return {"response": response}

# Step 3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
