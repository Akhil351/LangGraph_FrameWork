# Import the typing tools to define structured data (state)
from typing import Dict, TypedDict

# Import LangGraph's StateGraph class
from langgraph.graph import StateGraph


# Define the structure of the state that will flow through the graph
# In this case, the state will have just one key: "message", which is a string
class AgentState(TypedDict):
    message: str


# Define a node (function) that modifies the state
# It takes in a message and adds a friendly greeting
def greeting_node(state: AgentState) -> AgentState:
    # Modify the 'message' by adding a greeting text
    state['message'] = "Hey " + state['message'] + ", how is your day going?"
    return state  # Return the updated state


# Create a new state graph and tell it what the state looks like (AgentState)
graph = StateGraph(AgentState)

# Add a node to the graph called "greeter" that runs the greeting_node function
graph.add_node("greeter", greeting_node)

# Set the starting point of the graph to be the "greeter" node
graph.set_entry_point("greeter")

# Set the ending point of the graph to also be the "greeter" node
# (since this graph has only one step)
graph.set_finish_point("greeter")

# Compile the graph to get a runnable app
app = graph.compile()

# Run the graph by giving it a state input: {"message": "Akhil"}
result = app.invoke({"message": "Akhil"})

# Print the final message after the node processed it
print(result['message'])
