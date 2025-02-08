import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from src.prompt import prompt
from src.Tools import wikipedia, simon_blog_search, calculate

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize LLM
llm_test = ChatGroq(model_name="llama-3.3-70b-versatile")
print("LLM Initialized")

# Define the chatbot class
class Chatbot:
    def __init__(self, system=""):
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})
    
    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result
        
    def execute(self):
        llm = ChatGroq(model_name="Gemma2-9b-It")
        result = llm.invoke(self.messages)
        return result.content

# Mapping of known actions to their corresponding functions
known_actions = {
    "wikipedia": wikipedia,
    "calculate": calculate,
    "simon_blog_search": simon_blog_search
}

# Regular expression to capture action commands in the model output
action_re = re.compile(r'^Action: (\w+): (.*)')

# Query function for processing user input
def query(question, max_turns=5):
    bot = Chatbot(prompt)
    next_prompt = question

    for _ in range(max_turns):
        result = bot(next_prompt)
        print("\nModel output:\n", result)

        # Look for action lines in the model output
        actions = [action_re.match(line) for line in result.split('\n') if action_re.match(line)]
        
        if actions:
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception(f"Unknown action: {action}: {action_input}")
            print(f" -- running {action} with input: {action_input}")
            observation = known_actions[action](action_input)
            print("Observation:", observation)
            next_prompt = f"Observation: {observation}"
        else:
            return result  # Final response from the chatbot

    return result
