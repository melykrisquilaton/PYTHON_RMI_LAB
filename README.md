# Python RMI Lab Using Pyro5

## Project Description

This project translates a Java Remote Method Invocation (RMI) application into a Python distributed system using Pyro5 (Python Remote Objects).

The application demonstrates how a client can remotely access product information stored on a server.

## Project Files

- `product.py` – Defines the Product class, its attributes, and remotely accessible methods.
- `server.py` – Creates product objects and registers them with the Pyro5 Name Server.
- `client.py` – Connects to the server and retrieves product information.

## Requirements

- Python 3
- Pyro5

## Installation

Install Pyro5 using the terminal:

```bash
python -m pip install Pyro5
```

## How to Run

**Step 1:** Start the Pyro5 Name Server in the first terminal.

```bash
python -m Pyro5.nameserver -n 127.0.0.1 -p 9000
```

**Step 2:** Open a second terminal and run the server.

```bash
python server.py
```

**Step 3:** Open a third terminal and run the client.

```bash
python client.py
```

Keep the Name Server and server running while executing the client.

## Expected Client Output

```text
Name: Laptop
Description: Lenovo laptop
Price: 800000.0
```

## How It Works

The server creates four product objects and registers them with the Pyro5 Name Server. The client looks up the laptop object and uses a remote proxy to call its methods.

The client retrieves the product name, description, and price without directly accessing the server's variables.

## Java RMI to Python Pyro5 Translation

| Java RMI | Python Pyro5 |
|---|---|
| Product interface | Product class with exposed methods |
| ProductImpl class | Product class implementation |
| RMI Registry | Pyro5 Name Server |
| UnicastRemoteObject.exportObject() | daemon.register() |
| registry.bind() | ns.register() |
| registry.lookup() | ns.lookup() |
| Remote method invocation | Pyro5 Proxy method call |

## Reference

Original Java RMI project: https://github.com/melykrisquilaton/PYTHON_RMI_LAB
