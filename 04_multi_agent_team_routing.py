# REQUIRES A PRO PLAN: multi-agent teams (more than 1 AI agent working together) are a
# Pro plan feature, and this script deploys 3 teams (the Free plan allows 1 deployment).
# Upgrade to Pro: https://dashboard.custodianlabs.io

from custodian_labs import Custodian, CustodianSquad

# A multi-agent team (CustodianSquad) is several AI agents deployed as one app.
# The routing mode decides which agents work on each question:
#
#   single   - ONE agent answers: the one whose topics appear in the message.
#   workflow - ALL agents answer, always in workflow_order. Each agent's answer
#              is passed to the next, and you get the last agent's answer.
#   chain    - Starts with the agent whose topics match, then hands off to the
#              agents listed in its can_handoff_to.
#
# This script deploys one team per mode and asks each team the same questions,
# so you can compare. Docs: https://docs.custodianlabs.io/python-sdk/custodian-squads/

car_specialist = Custodian(
    name="car_specialist",
    model="gpt-4o",
    system_prompt=(
        "You know the dealership's cars from the uploaded file. Answer questions about "
        "models, fuel economy (mpg) and maintenance costs using only that data."
    ),
    topics=["car", "suv", "mpg", "fuel", "maintenance"],  # keywords that route to this agent
    can_handoff_to=["finance_advisor"],                    # used in chain mode only
)
# Run this script from the repo folder so the data_examples/ path is found.
# Each agent has its own files: only car_specialist sees this one.
car_specialist.add_data_source_file("data_examples/car_info.csv")

finance_advisor = Custodian(
    name="finance_advisor",
    model="gpt-4o",
    system_prompt=(
        "You help customers understand the cost of owning a car: loans, monthly "
        "payments and yearly running costs. Keep answers short and practical."
    ),
    topics=["loan", "finance", "payment", "budget", "interest"],
)

questions = [
    "Which SUV has the lowest maintenance cost?",            # matches car_specialist's topics
    "What interest rate should I expect on a 5-year loan?",  # matches finance_advisor's topics
]

for mode in ["single", "workflow", "chain"]:
    car_agent_team = CustodianSquad(
        name=f"Car Multi-Agent Team ({mode})",
        custodians=[car_specialist, finance_advisor],
        routing_mode=mode,
        workflow_order=["car_specialist", "finance_advisor"],  # used in workflow mode only
    )
    app = car_agent_team.deploy()

    print(f"\n========== routing_mode = {mode} ==========")
    print("Live here:", app.chat_url)

    for question in questions:
        reply = app.chat(question)
        print("\nQ:", question)
        print("Agents involved:", reply.handoff_path)
        print(reply.response)

# What to expect in "Agents involved":
#   single   -> ['car_specialist']                     and ['finance_advisor']
#   workflow -> ['car_specialist', 'finance_advisor']  for both questions
#   chain    -> ['car_specialist', 'finance_advisor']  and ['finance_advisor']
#               (finance_advisor has no can_handoff_to, so the chain stops there)
#
# This deploys 3 teams. To remove them later, delete them under My AIs in the Dashboard.
