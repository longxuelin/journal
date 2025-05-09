README: Usage Tutorial for Main Features
1. Prerequisites
Before you start using the project, make sure you have the following installed:

Python (version 3.x recommended) —— The Python 3.x version offers better compatibility and performance, supporting the latest features required by the project.
Streamlit —— Used for quickly building and deploying data applications, providing a simple interface development experience.
Pandas —— A powerful data - processing and analysis library for handling CSV data files in the project.
Supabase Python client —— Facilitates interaction with the Supabase database, enabling data storage and retrieval.

You can install the required Python packages using pip:

bash
pip install streamlit pandas supabase
2. Project Structure
The project consists of several Python files and CSV data files. Here is a brief overview:

journal/main.py: A simple script with a link to itself.
journal/form.py: Used to configure and launch the LLM and Telegram bot, and save the configuration to Supabase.
journal/test.py: Manages the registration log of technical documentation and saves the data to test.csv.
journal/pages/ПТО.py: Manages the quality control log of technical documentation lists and saves the data to PTO.csv.
journal/set.py: Creates a form to configure a RAG chatbot and saves the data to Supabase.
PTO.csv: Stores the quality control log data.
test.csv: Stores the registration log data.
3. Main Function Operation Steps
3.1 Launching the LLM and Telegram Bot Configuration (journal/form.py) <!—by lihuaju>
Run the Application
Open your terminal and navigate to the journal directory.
Run the following command to start the Streamlit application:

bash
streamlit run form.py

This will open the application in your default web browser. <--by lihuaju>

Configure LLM
In the 🧠 Конфигурация LLM section, enter your LLM API key in the API ключ LLM: field. The input is masked for security.
Enter the name of your LLM model in the Название модели LLM: field.
Optionally, expand the 🛠️ Расширенные настройки LLM section to configure advanced parameters such as system prompt, prompt, temperature, top K, max tokens, top P, frequency penalty, and presence penalty. <--by lihuaju>
Configure Telegram Bot
In the 🤖 Конфигурация Telegram бота section, enter your Telegram bot token in the Токен Telegram бота: field (masked) —— When entering the Telegram bot token, the input content will also be hidden to ensure the security of the token, which is a key credential for the bot to communicate with the Telegram server.
Enter the Telegram chat ID in the ID чата Telegram: field. <--by member 6>—— Correctly enter the chat ID to ensure that the bot can accurately send messages to the specified Telegram chat group or individual.
Launch LLM
Click the 🚀 Запустить LLM button.
If the launch is successful, the application will display the configuration details for both the LLM and the Telegram bot.
It will then attempt to save the combined configuration to the Supabase database. A success or error message will be shown accordingly. <--by lihuaju>
3.2 Registering Technical Documentation (journal/test.py) <!—by lihuaju>
Run the Application
Navigate to the journal directory in your terminal.
Run the command:

bash
streamlit run test.py

The application will open in your web browser. <--by lihuaju>

Enter Documentation Information
The application will display the last registered number—— Display the number of the last registration, facilitating users to understand the current registration sequence.
In the form, enter the following information:
Name of the document —— Accurately fill in the document name for easy subsequent searching and management.
Developer of the document —— Record the developer of the document to clarify the responsibility.
Position of the approver —— Fill in the position of the approver to reflect the standardization of the approval process.
Number of pages —— Record the number of pages of the document to have a preliminary understanding of the document's scale.
Storage location.
Registration date.
Approval date.
Notes (optional).
You can also upload the document if needed. <--by lihuaju>
Submit the Form
Click the Ввод button.
If all required fields are filled, the data will be saved to test.csv, and a success message will be displayed. Otherwise, an error message will prompt you to fill in the necessary fields. <--by lihuaju>
3.3 Recording Quality Control Log of Technical Documentation Lists (journal/pages/ПТО.py) <!—by lihuaju>
Run the Application
Navigate to the journal directory in your terminal.
Run the command:

bash
streamlit run pages/ПТО.py

The application will open in your web browser. <--by lihuaju>

Enter Quality Control Information
In the sidebar form, enter the following information:
Department.
Developer.
Receipt and inspection dates from different departments.
Name of the document.
Approver and approval dates from different departments.
Remarks (optional). <--by lihuaju>
Submit the Form
Click the Ввод button.
The data will be saved to PTO.csv, and a success toast message will be shown after a short wait. <--by lihuaju>
3.4 Creating a RAG Chatbot (journal/set.py) <!—by lihuaju>
Run the Application
Navigate to the journal directory in your terminal.
Run the command:

bash
streamlit run set.py

The application will open in your web browser. <--by lihuaju>

Enter Bot Configuration Information
In the form, enter the Telegram bot token, API of your model, and API of the vector database.
Click the Submit button.
The configuration data will be saved to the Supabase set table, and a success message indicating that the bot has been created will be displayed. <--by lihuaju>
