# Template for a new application example.
# Copy this file to application_examples/<your_use_case>.py and fill in each TODO.
# See application_examples/README.md for how to submit it.

# Plan note: the Free plan includes 1 deployed Custodian and always uses gpt-4o.
# Upgrade to Pro for more Custodians and more models: https://dashboard.custodianlabs.io

from custodian_labs import Custodian

# TODO: One or two lines on the use case: who uses this AI agent, and for what.
# Run from the repo root: python application_examples/<your_use_case>.py

ai_agent = Custodian(
    name="TODO: Your AI Agent Name",
    model="gpt-4o",
    system_prompt=(
        "TODO: Describe the agent's role, who it talks to, and what it should "
        "do when it doesn't know the answer."
    ),
    privacy_enabled=False,  # set True to mask PII before it reaches the LLM
)

# Optional: a data file for RAG. Put it in data_examples/ (fictional or public data only).
# ai_agent.add_data_source_file("data_examples/your_file.pdf")

# Optional: few-shot examples to set tone, format, or boundaries.
# ai_agent.add_examples(
#     [
#         {"user": "Example question", "assistant": "Example answer"},
#     ]
# )

app = ai_agent.deploy()

print("Your AI agent is ready and live here:")
print(app.chat_url)
# To remove this deployment later, delete it under My AIs in the Dashboard.

# TODO: A question that shows off your use case.
reply = app.chat("TODO: Your test question")
print(reply.response)
