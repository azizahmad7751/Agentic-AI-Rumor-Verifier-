from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, load_tools
from langchain.agents.agent_types import AgentType
import gradio as gr

# Correct Groq-compatible ChatOpenAI setup
llm = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    openai_api_key="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",  # Replace with your Groq key
    openai_api_base="https://api.groq.com/openai/v1",  # Correct base URL
    temperature=0.2
)

#  Load Wikipedia + DuckDuckGo as tools
tools = load_tools(["wikipedia", "ddg-search"])
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

#  Prompt builder to include sources in the response
def build_prompt(claim):
    return f"""
You are an agentic AI responsible for verifying social media claims.

Claim: "{claim}"

Search trusted sources (Wikipedia, Snopes, Google News).
Then label it as:
- TRUE (verified)
- FALSE (debunked)
- UNVERIFIED (unclear)

After verifying, provide the reasoning behind your decision and list the sources used to verify it.
"""

#  Verification logic
def verify_claim(claim):
    prompt = build_prompt(claim)
    result = agent.run(prompt)
    return result

#  Gradio UI with enhanced output to include references
iface = gr.Interface(
    fn=verify_claim,
    inputs=gr.Textbox(lines=3, placeholder="Paste a tweet or claim here..."),
    outputs=gr.Textbox(label=" Agentic AI Verdict and References"),
    title=" Agentic AI Rumor Verifier (Developed By Aziz Ahmad)",
    description="An LLM agent that uses real-time tools like Wikipedia and Web Search to verify online claims as TRUE, FALSE, or UNVERIFIED.",
    theme="default"
)

iface.launch(debug=True)
