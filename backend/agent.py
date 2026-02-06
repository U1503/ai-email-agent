from typing import TypedDict
from langgraph.graph import StateGraph
from backend.llm import get_llm
from backend.gmail_tools import send_email

llm = get_llm()

class EmailState(TypedDict):
    subject: str
    body: str
    category: str
    reply: str
    status: str

# Step 1: Classify
def classify_email(state: EmailState):
    prompt = f"""
    Classify this email into: Complaint, Inquiry, Spam, or Other.

    Subject: {state['subject']}
    Body: {state['body']}
    """
    response = llm.invoke(prompt)
    return {"category": response.content.strip()}

# Step 2: Generate reply
def generate_reply(state: EmailState):
    prompt = f"""
    Write a professional email reply.

    Subject: {state['subject']}
    Body: {state['body']}
    """
    response = llm.invoke(prompt)
    clean_reply = response.content.replace("\\n", "\n")
    return {"reply": clean_reply.strip()}


# Step 3: Send reply
def send_reply(state: EmailState):
    result = send_email(
        to="customer@example.com",
        subject="Re: " + state["subject"],
        body=state["reply"]
    )
    return {"status": result}

# Build graph
def build_agent():
    graph = StateGraph(EmailState)

    graph.add_node("classify", classify_email)
    graph.add_node("reply", generate_reply)

    graph.set_entry_point("classify")
    graph.add_edge("classify", "reply")

    return graph.compile()

