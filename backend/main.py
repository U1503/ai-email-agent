from fastapi import FastAPI
from backend.agent import build_agent
from backend.gmail_tools import read_email, send_email

app = FastAPI()
agent = build_agent()

@app.get("/")
def home():
    return {"message": "AI Email Agent Running 🚀"}

@app.get("/run-agent")
def run_agent():
    email = read_email()

    result = agent.invoke({
        "subject": email["subject"],
        "body": email["body"]
    })

    return result

@app.post("/send-email")
def send_final_email(data: dict):
    result = send_email(
        to="customer@example.com",
        subject=data.get("subject"),
        body=data.get("reply")
    )

    return {"status": result}
