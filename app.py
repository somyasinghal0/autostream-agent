from agent.graph import build_graph

graph = build_graph()

def run():
    state = {
        "user_input": "",
        "intent": None,
        "response": None,
        "name": None,
        "email": None,
        "platform": None,
        "last_topic": None
    }

    print("🤖 AutoStream Agent (LangGraph): Hi!")

    while True:
        user_input = input("\nYou: ")
        state["user_input"] = user_input

        result = graph.invoke(state)

        print("Agent:", result["response"])


if __name__ == "__main__":
    run()