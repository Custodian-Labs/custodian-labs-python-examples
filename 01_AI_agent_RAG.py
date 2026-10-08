# Plan note: the Free plan includes 1 deployed Custodian and always uses gpt-4o.
# Upgrade to Pro for more Custodians and more models: https://dashboard.custodianlabs.io

from custodian_labs import Custodian

ai_agent = Custodian(
    name="Car Info Assistant",
    model="gpt-4o",
    system_prompt="You are a helpful assistant, and you are given a data file to answer questions about the data.",
    privacy_enabled=False,  # set True to mask PII before it reaches the LLM
)

# Run this script from the repo folder so the data_examples/ path is found.
# The file is uploaded and indexed for RAG when you call deploy().
ai_agent.add_data_source_file("data_examples/car_info.csv")

app = ai_agent.deploy()

print("Your AI agent for car info is ready and live here:")
print(app.chat_url)
# To remove this deployment later, delete it under My AIs in the Dashboard.

# Chat with it on the command line (type 'exit' or 'quit' to stop)
app.chat()

# Or send a single message and get a response object back.
# Pass model= to override the deployed model for that one request (Pro plan only;
# on the Free plan requests always run on gpt-4o):
# reply = app.chat("Which car has the lowest maintenance cost?", model="gpt-4o-mini")
# print(reply.response)
