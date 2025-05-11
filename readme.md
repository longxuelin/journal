<!--by lihuaju -->
README: Usage Tutorial for Main Features
1. Prerequisites
Before you start using the project, make sure you have the following installed:

1.1 Python (version 3.x recommended) —— The Python 3.x version offers better compatibility and performance, supporting the latest features required by the project.

1.2 Streamlit —— Used for quickly building and deploying data applications, providing a simple interface development experience.

1.3Pandas —— A powerful data - processing and analysis library for handling CSV data files in the project.

1.4 Supabase Python client —— Facilitates interaction with the Supabase database, enabling data storage and retrieval.

You can install the required Python packages using pip:

bash
pip install streamlit pandas supabase

2. Project Structure
The project consists of several Python files and CSV data files. Here is a brief overview:

2.1 journal/main.py: A simple script with a link to itself —— Primarily serves as a basic script for the project, potentially for subsequent expansion or linking to other functional modules.

2.2 journal/form.py: Used to configure and launch the LLM and Telegram bot, and save the configuration to Supabase —— In this file, users can set relevant parameters for the large - language model (LLM) and Telegram bot, achieving the launch and configuration storage of both.

2.3 journal/test.py: Manages the registration log of technical documentation and saves the data to test.csv —— Responsible for recording the registration information of technical documents, saving the detailed data of each registration into the test.csv file for easy subsequent querying and management.

2.4 journal/pages/ПТО.py: Manages the quality - control log of technical documentation lists and saves the data to PTO.csv —— Focuses on recording the quality - control log of technical document lists, storing the quality - inspection information of each document into PTO.csv to ensure the traceability of document quality.

2.5 journal/set.py: Creates a form to configure a RAG chatbot and saves the data to Supabase —— Provides a form interface to configure a RAG chatbot, saving the configuration information to Supabase for subsequent use and management.

2.6 PTO.csv: Stores the quality - control log data —— Specifically used to store quality - control log data, with each row of records corresponding to the detailed information of a quality inspection.

2.7 test.csv: Stores the registration log data —— Saves the registration log data of technical documents, recording various details of document registration, such as time, personnel, etc.

3. Main Function Operation Steps

3.1 Launching the LLM and Telegram Bot Configuration (journal/form.py) 
Run the Application
Open your terminal and navigate to the journal directory.
Run the following command to start the Streamlit application:

bash
streamlit run form.py

This will open the application in your default web browser. 

Configure LLM
In the 🧠 Конфигурация LLM section, enter your LLM API key in the API ключ LLM: field. The input is masked for security.
Enter the name of your LLM model in the Название модели LLM: field.
Optionally, expand the 🛠️ Расширенные настройки LLM section to configure advanced parameters such as system prompt, prompt, temperature, top K, max tokens, top P, frequency penalty, and presence penalty. 
Configure Telegram Bot
In the 🤖 Конфигурация Telegram бота section, enter your Telegram bot token in the Токен Telegram бота: field (masked).
Enter the Telegram chat ID in the ID чата Telegram: field. 
Launch LLM
Click the 🚀 Запустить LLM button.
If the launch is successful, the application will display the configuration details for both the LLM and the Telegram bot.
It will then attempt to save the combined configuration to the Supabase database. A success or error message will be shown accordingly. 

3.2 Registering Technical Documentation (journal/test.py) 
Run the Application
Navigate to the journal directory in your terminal.
Run the command:

bash
streamlit run test.py

The application will open in your web browser.

Enter Documentation Information
The application will display the last registered number.
In the form, enter the following information:
Name of the document.
Developer of the document.
Position of the approver.
Number of pages.
Storage location.
Registration date.
Approval date.
Notes (optional).
You can also upload the document if needed.
Submit the Form
Click the Ввод button.
If all required fields are filled, the data will be saved to test.csv, and a success message will be displayed. Otherwise, an error message will prompt you to fill in the necessary fields.

3.3 Recording Quality Control Log of Technical Documentation Lists (journal/pages/ПТО.py) 
Run the Application
Navigate to the journal directory in your terminal.
Run the command:

bash
streamlit run pages/ПТО.py

The application will open in your web browser. 

Enter Quality Control Information
In the sidebar form, enter the following information:
Department.
Developer.
Receipt and inspection dates from different departments.
Name of the document.
Approver and approval dates from different departments.
Remarks (optional). 
Submit the Form
Click the Ввод button —— Click the button to submit the quality - control information.
The data will be saved to PTO.csv, and a success toast message will be shown after a short wait.

3.4 Creating a RAG Chatbot (journal/set.py) 
3.4.1 Run the Application
Navigate to the journal directory in your terminal.
Run the command:

bash
streamlit run set.py

The application will open in your web browser. 

3.4.2 Enter Bot Configuration Information
In the form, enter the Telegram bot token, API of your model, and API of the vector database.
Click the Submit button.
The configuration data will be saved to the Supabase set table, and a success message indicating that the bot has been created will be displayed.
This concludes the main function usage tutorial for the project. Make sure to follow the steps carefully and refer to the screenshots for better understanding.
