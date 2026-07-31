# LangGraph Fundamentals

A beginner-friendly project demonstrating the core concepts of **LangGraph** by building a simple sequential workflow. The application consists of three connected nodes that pass a shared state between them, allowing the user to update a message at each step and observe how data flows through the graph.

## Features

* Creates a workflow with **3 nodes**
* Connects nodes using **LangGraph edges**
* Passes a shared state between nodes
* Accepts user input at each node
* Prints the updated state after every step
* Demonstrates workflow execution from **START** to **END**

## Technologies Used

* Python 3.x
* LangGraph

## Project Structure

```text
LangGraph-Fundamentals/
│── main.py
│── README.md
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd LangGraph-Fundamentals
```

3. Install the required package:

```bash
pip install langgraph
```

## Running the Project

Run the application using:

```bash
python main.py
```

The program will:

1. Ask for an initial message.
2. Execute **Node 1**, where you can append text.
3. Execute **Node 2**, where you can append more text.
4. Execute **Node 3**, where you can append the final text.
5. Display the final updated message after the workflow completes.

## Example

```text
Enter a message to start:
Hello

Node 1 Received: Hello
Enter a word you want to update the message: World
Node 1 Output: Hello World

Node 2 Received: Hello World
Enter a word you want to update the message: from
Node 2 Output: Hello World from

Node 3 Received: Hello World from
Enter a word you want to update the message: LangGraph
Node 3 Output: Hello World from LangGraph

Final Message:
{'message': 'Hello World from LangGraph'}
```

## Learning Objectives

This project demonstrates:

* Creating a `StateGraph`
* Defining a shared state using `TypedDict`
* Creating and registering nodes
* Connecting nodes using edges
* Passing state between nodes
* Executing a LangGraph workflow from **START** to **END**

## Author

Developed by **Ahmad Mustafa** as a learning project to understand the fundamentals of **LangGraph** and workflow-based application development.
