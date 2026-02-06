from backend.agent import build_agent

def test_agent_response():
    agent = build_agent()

    result = agent.invoke({
        "subject": "Refund Request",
        "body": "I received a damaged product."
    })

    assert "reply" in result
    assert "category" in result
