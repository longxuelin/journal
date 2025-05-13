Terms Glossary for Journal Project
1. General Project - related Terms
Journal Project
Definition: A collection of Streamlit - based applications. These applications are designed for multiple purposes, including registering technical documentation, setting up LLM and Telegram bots, and managing data associated with different workflows.
Relevance: It represents the overall scope of the software project.
Streamlit Application
Definition: Web applications created using the Streamlit Python library. Streamlit simplifies the process of building interactive web interfaces with Python code, eliminating the need for extensive front - end development knowledge.
Relevance: All the applications in the Journal Project are built using Streamlit.
Python Script
Definition: A text file containing Python code. In this project, multiple Python scripts (e.g., main.py, form.py, etc.) are used to implement different functionalities.
Relevance: The core components of the project are written as Python scripts.
CSV File
Definition: Comma - Separated Values file, a simple file format used to store tabular data. In the project, CSV files like test.csv and PTO.csv are used to store data related to different workflows.
Relevance: They serve as local data storage for the project's data - recording functions.
Supabase Database
Definition: An open - source Firebase alternative that provides a backend as a service. It includes features like a PostgreSQL database, authentication, and real - time subscriptions. In the project, it is used to store configuration data for LLM, Telegram bots, and RAG chat - bots.
Relevance: Enables centralized and secure storage of important configuration data.
2. main.py - specific Terms
Entry - point
Definition: In a software project, the entry - point is the first part of the program that is executed. In the Journal Project, main.py acts as an entry - point or a simple navigation tool.
Relevance: It provides users with an initial access point to the project and can guide them to other parts of the code or functionality.
st.markdown
Definition: A function provided by the Streamlit library. It is used to display Markdown - formatted text in a Streamlit application. Markdown is a lightweight markup language that allows for easy text formatting, such as creating headings, lists, and links.
Relevance: In main.py, it is used to display a clickable link.
3. Deployment - related Terms
Server Configuration
Definition: The process of setting up a server to meet the requirements of running an application. For the Journal Project, the recommended server configuration includes a Windows Server 2019 or later operating system, at least 2 CPU cores, 4GB of RAM, and 50GB of free disk space.
Relevance: Ensures that the server has sufficient resources to run the Streamlit applications.
Windows Firewall
Definition: A built - in security feature in Windows operating systems that controls incoming and outgoing network traffic. For the Streamlit application, port 8501 needs to be opened to allow external access.
Relevance: Allows the application to be accessed from external networks.
DNS Records
Definition: Domain Name System records that map domain names to IP addresses. If the project needs to be accessed via a domain name, correct DNS records must be set up.
Relevance: Enables users to access the application using a domain name instead of an IP address.
Virtual Environment
Definition: An isolated Python environment that allows different projects to have their own sets of dependencies. In the deployment process of the Journal Project, creating a virtual environment (e.g., using python -m venv myenv) is an optional but recommended step.
Relevance: Helps manage project - specific dependencies and avoid conflicts between different projects.
streamlit run
Definition: A command used to start a Streamlit application. In the deployment process, streamlit run main.py is used to launch the Streamlit application defined in the main.py file.
Relevance: This command is the key step to start the application.
4. Other Key Files - related Terms
LLM (Large Language Model)
Definition: A type of artificial intelligence model that can generate human - like text based on the input it receives. In the project, files like form.py are used to configure and launch an LLM.
Relevance: It is one of the main features of the project, and the configuration and management of LLM are important parts of the application's functionality.
Telegram Bot
Definition: A program that runs on the Telegram messaging platform. It can automate tasks, provide information, and interact with users. In the project, files like form.py and set.py are involved in setting up Telegram bots.
Relevance: Allows for integration with the Telegram platform and provides additional functionality for users.
RAG Chat - bot
Definition: A Retrieval - Augmented Generation chat - bot that combines retrieval from a knowledge base with text generation. The set.py file in the project is used to manage the settings for creating a RAG chat - bot.
Relevance: It is a specific type of chat - bot that the project supports.
