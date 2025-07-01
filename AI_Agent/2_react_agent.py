# ✅ Import necessary typing utilities
from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv
import os

# ✅ Import message types used in LangChain & LangGraph
from langchain_core.messages import BaseMessage, SystemMessage, ToolMessage,HumanMessage,AIMessage

# ✅ Import OpenAI chat model and LangGraph components
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

# ✅ Load environment variables from `.env` file (e.g., API key)
load_dotenv()

# 🧠 Define the state structure that flows between graph nodes
class AgentState(TypedDict):
    # 'messages' will store a list of messages exchanged (both user and AI)
    # Annotated with `add_messages` so LangGraph knows to automatically
    # accumulate messages returned from each node
    messages: Annotated[Sequence[BaseMessage], add_messages]

# 🛠️ Define a tool that the agent can call using function-calling
@tool
def add(a: int, b: int) -> int:
    """Adds two integers and returns the result."""
    return a + b

@tool
def sub(a: int, b: int) -> int:
    """Subtracts b from a and returns the result."""
    return a - b

@tool
def mult(a: int, b: int) -> int:
    """Multiplies two integers and returns the result."""
    return a * b

@tool
def div(a: int, b: int) -> float:
    """Divides a by b and returns the result as a float."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# 🔧 Register tools that the LLM is allowed to call
tools = [add,sub,mult,div]

# 🤖 Initialize the OpenAI model and bind the available tools to it
model = ChatOpenAI(
    model="gpt-4o", 
    api_key=os.getenv("OPENAI_API_KEY")  # Load API key from environment # type: ignore
).bind_tools(tools)  # Attach the defined tools to the model

# 🧩 Node function: Handles LLM invocation and returns assistant reply
def model_call(state: AgentState) -> AgentState:
    # Set the system prompt to guide the assistant’s behavior
    system_prompt = SystemMessage(content="You are my AI assistant, please answer my query to the best of your ability")
    
    # Combine system prompt and current conversation messages
    input_messages = [system_prompt] + state["messages"] # type: ignore

    # Call the LLM with the message history
    response = model.invoke(input_messages)

    # Return the new response to be automatically appended to state['messages'] by LangGraph
    return {"messages": [response]}

# 🔁 Router function: Determines whether the conversation should continue
def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]  # Get the last message (usually assistant's response)

    if not last_message.tool_calls: # type: ignore
        return "end"  # If no tools were called → end the graph
    else:
        return "continue"  # If tools were called → go to the tool executor node

# 🧠 Create the graph
graph = StateGraph(AgentState)

# Add main model node
graph.add_node("our_agent", model_call)

# Set graph starting point to the model node
graph.add_edge(START, "our_agent")

# Add the tool execution node
tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

# Conditional routing based on whether a tool is needed
graph.add_conditional_edges(
    "our_agent",          # From this node
    should_continue,      # Use this router function
    {
        "continue": "tools",  # If tool required, go to tool executor
        "end": END            # Otherwise, end the graph
    }
)

# After executing tool, go back to the model to continue the loop
graph.add_edge("tools", "our_agent")

# ✅ Compile the graph into an executable agent
app = graph.compile()


user_input = input("You: ")

# 🧪 Test input
input_state = {
    "messages": [HumanMessage(content=user_input)]  # Start with the user's message
}

# 🚀 Invoke the graph
final_state = app.invoke(input_state)  # type: ignore

# 📦 Print the final state, including tool call info if used
print("\nFinal Agent Response:")
for msg in final_state["messages"]:
    if isinstance(msg, AIMessage):
        print("AI:", msg.content)
        # If AI is calling a tool, show tool call info
        if msg.tool_calls:
            for tool_call in msg.tool_calls:
                print(f"🔧 Tool Call → Tool: {tool_call['name']}, Args: {tool_call['args']}")
    elif isinstance(msg, ToolMessage):
        print(f"🛠️ Tool Result: {msg.content}")
    else:
        print(f"{msg.type.capitalize()}: {msg.content}")
