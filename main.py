from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class graphState(TypedDict):
    message: str

def node_one(state: graphState):
    print("node 1 recieved: ", state["message"])
    updated_message = input("Enter a word u want to update the message: ")
    state["message"] += updated_message
    print("Node 1 Output: ", state["message"])

    return state

def node_two(state: graphState):
    print("node 2 recieved: ", state["message"])
    updated_message = input("Enter a word u want to update the message: ")
    state["message"] += updated_message
    print("Node 2 Output: ", state["message"])

    return state

def node_three(state: graphState):
    print("node 3 recieved: ", state["message"])
    updated_message = input("Enter a word u want to update the message: ")
    state["message"] += updated_message
    print("Node 3 Output: ", state["message"])

    return state

builer = StateGraph(graphState)

builer.add_node("Node 1", node_one)
builer.add_node("Node 2", node_two)
builer.add_node("Node 3", node_three)

builer.add_edge(START, "Node 1")
builer.add_edge("Node 1", "Node 2")
builer.add_edge("Node 2", "Node 3")
builer.add_edge("Node 3", END)

graph = builer.compile()

start = input("Enter A message to start: ")

result = graph.invoke({"message" : start})

print("\nFinal Message: ")
print(result)
