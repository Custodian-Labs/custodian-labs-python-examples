# Plan note: the Free plan includes 1 deployed Custodian and always uses gpt-4o.
# Upgrade to Pro for more Custodians and more models: https://dashboard.custodianlabs.io

from custodian_labs import Custodian

ai_agent = Custodian(
    name="Customer Support AI",
    model="gpt-4o",
    system_prompt="You are a customer support agent.",
    privacy_enabled=True,  # mask PII (names, phone numbers, ...) before it reaches the LLM
)

# Few-shot examples teach the agent the tone and format of your answers.
ai_agent.add_examples(
    [
        {"user": "How do I reset my password?", "assistant": "Go to settings, open security, and choose reset password."},
        {"user": "How do I invite teammates?", "assistant": "Open workspace settings, then add members by email."},
    ]
)

app = ai_agent.deploy()

print("Your AI agent for customer support is ready and live here:")
print(app.chat_url)
# To remove this deployment later, delete it under My AIs in the Dashboard.

# Ask something that isn't in the examples. It should answer in the same short style.
reply = app.chat("How do I change my billing email?")
print(reply.response)

# The app remembers the conversation, so follow-up questions have context.
reply = app.chat("And what if I no longer have access to the old email?")
print(reply.response)

# Optional: override the model for one request (Pro plan only;
# on the Free plan requests always run on gpt-4o):
# reply = app.chat("How do I change my billing email?", model="gpt-4o-mini")
# print(reply.response)
