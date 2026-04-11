from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END

from agent.intent_classifier import classify_intent
from agent.rag_pipeline import get_answer
from agent.tools import mock_lead_capture


# -------- STATE --------
class AgentState(TypedDict):
    user_input: str
    intent: Optional[str]
    response: Optional[str]
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
    last_topic: Optional[str]


# -------- NODES --------
def intent_node(state):
    intent = classify_intent(state["user_input"])
    return {**state, "intent": intent}


def greeting_node(state):
    return {**state, "response": "Hello! Ask me anything about our plans 😊"}


def rag_node(state):
    answer = get_answer(state["user_input"])
    return {**state, "response": answer, "last_topic": "pricing"}


def followup_node(state):
    if state.get("last_topic") == "pricing":
        return {
            **state,
            "response": "Sure! Here's more detail 👇\n" + get_answer("pricing")
        }
    return {
        **state,
        "response": "Could you clarify what you'd like more details about?"
    }


def lead_node(state):
    return {
        **state,
        "response": """Awesome! Let's get you started 🚀

Please enter your details in this format:
Name, Email, Platform

Example:
Somya, somya@gmail.com, YouTube"""
    }


def tool_node(state):
    text = state["user_input"]

    try:
        # Flexible parsing (works for both formats)
        if "name:" in text.lower():
            parts = text.split(",")
            name = parts[0].split(":")[1].strip()
            email = parts[1].split(":")[1].strip()
            platform = parts[2].split(":")[1].strip()
        else:
            parts = text.split(",")
            name = parts[0].strip()
            email = parts[1].strip()
            platform = parts[2].strip()

        mock_lead_capture(name, email, platform)

        return {
            **state,
            "response": "🎉 Done! Our team will contact you soon."
        }

    except:
        return {
            **state,
            "response": "Please provide details correctly like: Name, Email, Platform"
        }


# -------- ROUTER --------
def route(state):
    intent = state["intent"]
    text = state["user_input"].lower()

    if "@" in text and "," in text:
        return "tool"

    if intent == "greeting":
        return "greeting"

    elif intent == "pricing":
        return "rag"

    elif intent == "high_intent":
        return "lead"

    elif intent == "follow_up":
        return "followup"
    
    elif intent == "thanks":
        return "thanks"

    return "rag"


# -------- BUILD GRAPH --------
def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("intent", intent_node)
    workflow.add_node("greeting", greeting_node)
    workflow.add_node("rag", rag_node)
    workflow.add_node("lead", lead_node)
    workflow.add_node("followup", followup_node)
    workflow.add_node("tool", tool_node)
    workflow.add_node("thanks", thanks_node)

    workflow.set_entry_point("intent")

    workflow.add_conditional_edges(
        "intent",
        route,
        {
            "greeting": "greeting",
            "rag": "rag",
            "lead": "lead",
            "followup": "followup",
            "tool": "tool",
            "thanks": "thanks"
        }
    )

    workflow.add_edge("greeting", END)
    workflow.add_edge("rag", END)
    workflow.add_edge("followup", END)
    workflow.add_edge("lead", "tool")
    workflow.add_edge("tool", END)
    workflow.add_edge("thanks", END)

    return workflow.compile()

def thanks_node(state):
    return {
        **state,
        "response": "You're welcome! 😊 Let me know if you need anything else."
    }