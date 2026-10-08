# Plan note: the Free plan includes 1 deployed Custodian and always uses gpt-4o.
# Upgrade to Pro for more Custodians and more models: https://dashboard.custodianlabs.io

# A small FastAPI server that lets a web page chat with your AI agent over a WebSocket.
# Install:  pip install fastapi "uvicorn[standard]"
# Run (from the repo root):  uvicorn websocket_examples.01_simple_websocket_bridge:app
# Then open websocket_examples/02_simple_websocket_browser.html in your browser.

import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.concurrency import run_in_threadpool

from custodian_labs import App, Custodian, CustodianClient

# Deploy ONCE when the server starts, not on every connection,
# so refreshing the page doesn't create a new deployment each time.
ai_agent = Custodian(
    name="WebSocket Bridge AI",
    model="gpt-4o",
    system_prompt="You are a helpful assistant exposed through a websocket bridge.",
)
deployed = ai_agent.deploy()
print("Your AI agent is live here:", deployed.chat_url)
# To remove this deployment later, delete it under My AIs in the Dashboard.

client = CustodianClient()
app = FastAPI()


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket) -> None:
    await websocket.accept()

    # Each browser connection gets its own chat session (its own conversation memory)
    session = App(app_id=deployed.app_id, client=client, chat_url=deployed.chat_url)

    try:
        while True:
            raw = await websocket.receive_text()
            try:
                message = str(json.loads(raw).get("message") or "").strip()
            except (json.JSONDecodeError, AttributeError):
                message = raw.strip()

            if not message:
                await websocket.send_json({"error": "message is required"})
                continue

            # chat() waits on the network, so run it in a thread to keep the server responsive
            reply = await run_in_threadpool(session.chat, message)
            await websocket.send_json({"response": reply.response, "session_id": reply.session_id})
    except WebSocketDisconnect:
        pass
