# Plan note: the Free plan includes 1 deployed Custodian and always uses gpt-4o.
# Upgrade to Pro for more Custodians and more models: https://dashboard.custodianlabs.io

from custodian_labs import CustodianBuilder

# "Chaining" means calling methods one after another on the same object:
# each .with_...() sets one option and hands the builder back, so the next
# call can continue on the next line. .deploy() at the end creates the AI agent.
# Same result as Custodian(...) in 01/02, just a different style.
# Docs: https://docs.custodianlabs.io/python-sdk/

app = (
    CustodianBuilder()
    .with_name("Finance Policy AI")
    .with_model("gpt-4o")
    .with_prompt("You are a helpful finance assistant.")
    .with_examples(
        [
            {"user": "When is an invoice overdue?", "assistant": "An invoice is overdue after the due date passes without payment."}
        ]
    )
    # Uncomment to try more options:
    # .with_data_source_file("data_examples/contract.pdf")  # add a file for RAG
    # .with_privacy()                                       # mask PII before it reaches the LLM
    .deploy()
)

print("Your AI agent for finance policy is ready and live here:")
print(app.chat_url)
# To remove this deployment later, delete it under My AIs in the Dashboard.

reply = app.chat("Give me a short overdue invoice policy.")
print(reply.response)

# Optional: override the model for one request (Pro plan only;
# on the Free plan requests always run on gpt-4o):
# reply = app.chat("Give me a short overdue invoice policy.", model="gpt-4o-mini")
# print(reply.response)
