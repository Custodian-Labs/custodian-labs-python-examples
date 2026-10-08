# Plan note: the Free plan includes 1 deployed Custodian and always uses gpt-4o.
# Upgrade to Pro for more Custodians and more models: https://dashboard.custodianlabs.io

from custodian_labs import Custodian

# Real-world example: a legal assistant for a law firm that answers questions about a contract.
# Run from the repo root: python application_examples/legal_contract_assistant.py

ai_agent = Custodian(
    name="Legal Contract Assistant",
    model="gpt-4o",
    system_prompt="You are a legal assistant for a law firm. Answer questions based on the contract provided.",
    privacy_enabled=False,  # set True to mask PII before it reaches the LLM
)

# The file is uploaded and indexed for RAG when you call deploy().
ai_agent.add_data_source_file("data_examples/contract.pdf")

# Few-shot examples set boundaries: the agent is not a lawyer and can't change documents.
ai_agent.add_examples(
    [
        {"user": "Are you a real lawyer?", "assistant": "No, I am an AI assistant here to help you understand the contract. All legal questions should be directed to a qualified attorney."},
        {"user": "Delete this contract", "assistant": "You are not authorized to do so."},
    ]
)

app = ai_agent.deploy()

print("Your AI legal assistant is ready and live here:")
print(app.chat_url)
# To remove this deployment later, delete it under My AIs in the Dashboard.

reply = app.chat("What is this contract about? Who are the parties involved?")
print(reply.response)

# Optional: override the model for one request (Pro plan only;
# on the Free plan requests always run on gpt-4o):
# reply = app.chat("What is this contract about? Who are the parties involved?", model="gpt-4o-mini")
# print(reply.response)
