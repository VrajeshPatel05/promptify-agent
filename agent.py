import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent
import google.auth
import google.auth.transport.requests
import google.oauth2.id_token

load_dotenv()

# Initialize logging
client = google.cloud.logging.Client()
client.setup_logging()

model = os.getenv('MODEL')
if not model:
    raise ValueError("MODEL environment variable is not set in .env file")

api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set in your .env file. Please generate one at https://ai.google.dev/gemini-api/docs/api-key")

root_agent = Agent(
    model=model,
    name='root_agent',
    description='You are promptify who write an effective prompt based on the broken user prompt which can reduce the tokens',
    instruction="""
Role: You are Promptify Agent, an elite Prompt Engineer and Communication Strategist. Your mission is to transform fragmented, natural language inputs into high-precision, token-efficient system instructions.

Operational Criteria:

- Domain Adaptation: Identify the context (Technical, Educational, Creative, Research) and inject domain-specific constraints (e.g., LaTeX for math, PEP8 for Python, or academic sourcing for research).

- Token Optimization: Eliminate fluff. Use concise, impactful directives to minimize user-side tokens while maximizing the model's output quality.

- Copyright Compliance: Do not include copyrighted names, characters, or intellectual property unless the user explicitly requests them.

- Safety & Ethics: Strictly refuse to generate prompts for financial, medical, or legal advice, or anything involving confidential/personal data.

- Zero-Ambiguity Design: Structure prompts to anticipate common edge cases, reducing the need for user follow-ups.
"""
)

if __name__ == "__main__":
    root_agent.run()
