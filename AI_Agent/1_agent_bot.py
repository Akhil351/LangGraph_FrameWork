from typing import TypedDict, List, Union
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
import os
import json

# Load environment variables (e.g., OpenAI API key)
load_dotenv()

# Define the agent's state format
class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY")) # type: ignore

# Load existing memory from logging.txt if it exists
memory: List[Union[HumanMessage, AIMessage]] = []

if os.path.exists("logging.txt"):
    with open("logging.txt", "r") as f:
        try:
            raw = json.load(f)
            for msg in raw:
                if msg["type"] == "human":
                    memory.append(HumanMessage(content=msg["content"]))
                elif msg["type"] == "ai":
                    memory.append(AIMessage(content=msg["content"]))
        except Exception as e:
            print("Error loading memory:", e)

# Node that sends all messages to LLM and appends its reply to memory
def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print(f"Assistant: {response.content}")
    memory.append(AIMessage(content=response.content))  # Only once
    return {"messages": memory}  # Updated state is memory

# Build the LangGraph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

# Compile the graph into a runnable agent
agent = graph.compile()

# Start the chat loop
print("Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    memory.append(HumanMessage(content=user_input))

    # Run the LangGraph agent
    agent.invoke({"messages": memory})

# Save the entire message memory to logging.txt as JSON
with open("logging.txt", "w") as f:
    json.dump(
        [
            {"type": "human" if isinstance(m, HumanMessage) else "ai", "content": m.content}
            for m in memory
        ],
        f,
        indent=2
    )

print("✅ Conversation saved to logging.txt")
