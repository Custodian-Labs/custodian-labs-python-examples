# Plan note: the Free plan includes 1 deployed Custodian and always uses gpt-4o.
# Upgrade to Pro for more Custodians and more models: https://dashboard.custodianlabs.io

from custodian_labs import Custodian

# Real-world example: an AI agent that answers recruiters' questions about your CV.
# Swap in your own CV (.docx, .pdf or .txt) and share the link with hiring managers.
# Run from the repo root: python application_examples/cv_recruiter_assistant.py

ai_agent = Custodian(
    name="Ask About My CV",
    model="gpt-4o",
    system_prompt=(
        "You answer questions from recruiters and hiring managers about the candidate, "
        "using only the CV provided. Be professional and concise. If the CV doesn't "
        "cover something, say so and suggest contacting the candidate directly. "
        "Never invent experience, dates, or qualifications."
    ),
)

# The file is uploaded and indexed for RAG when you call deploy().
ai_agent.add_data_source_file("data_examples/CV.docx")

app = ai_agent.deploy()
# Only want people you invite to see it? Deploy with a password instead:
# app = ai_agent.deploy(share_mode="password", share_password="choose-a-password")

print("Your CV agent is live! Share this link with recruiters:")
print(app.chat_url)
# To remove this deployment later, delete it under My AIs in the Dashboard.

reply = app.chat("What is the candidate's name, and what roles are they a good fit for?")
print(reply.response)
