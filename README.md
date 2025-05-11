<!--by longxuelin -->
Deployment Instructions
1. Server Configuration
The project is intended to be deployed on a Windows system. The following server configurations are recommended:
Operating System: Windows Server 2019 or later.
CPU: At least 2 cores.
Memory: At least 4GB RAM.
Storage: At least 50GB of free disk space.
2. Network Settings
Firewall
Make sure the necessary ports are open in the Windows Firewall. For a Streamlit application, by default, it uses port 8501. So, you should open port 8501 for inbound and outbound traffic.
DNS
Set up the correct DNS records to point to the server's IP address if the project needs to be accessed via a domain name.
3. Deployment Process
Step 1: Clone the Repository
Open the Command Prompt or PowerShell on your Windows server and run the following command to clone the project repository:
git clone https://github.com/MagneticDogSon/journal.git
cd journal![9137b8e7-a4dc-4e78-94ee-a97f956eb5b2](https://github.com/user-attachments/assets/6489258c-c2db-46f0-af7a-b6e4a8d87a26)
Step 2: Install Python
If Python is not installed on your server, download and install Python 3.8 or higher from the official Python website (https://www.python.org/downloads/). After installation, verify the Python version by running:python --version![edb33632-c902-4e59-8c46-d26907c79861](https://github.com/user-attachments/assets/10b8d058-1e65-4a50-bcee-d22e72fe3aa4)
Step 3: Create a Virtual Environment (Optional but Recommended)
It's a good practice to create a virtual environment to isolate the project's dependencies. Run the following commands:
python -m venv myenv
myenv\Scripts\activate![4e22587b-ddaa-412f-8543-948fbd3d5512](https://github.com/user-attachments/assets/43612fa7-45e8-4c3a-b2f6-4668d78babab)
Step 4: Install Dependencies
Install Streamlit and other project dependencies.
pip install streamlit![9a82da95-9572-4d91-a953-7d35a5265bb5](https://github.com/user-attachments/assets/eff090f6-ca94-43ca-b12e-85a2a689dd1d)
Step 5: Start the Streamlit Application
Since no application configuration was done, run the following command to start the Streamlit app. The main Python script is named :main.py
streamlit run main.py![e0220416-e975-4903-9937-27a3485e1835](https://github.com/user-attachments/assets/de84a9e9-f856-4c2d-b2fa-3260b3f0af93)
4. Verification
After the application is started, open a web browser and enter the server's IP address followed by (e.g., ). You should see your Streamlit application running.:8501http://<server_ip>:8501
![11e039ea-3e41-492a-8083-235a321e760e](https://github.com/user-attachments/assets/378c8988-3282-4a1c-b5d0-ee0bd67f63df)
AI Review
This deployment instruction has been reviewed by AI to ensure clarity, completeness, and accuracy. However, actual deployment may vary depending on the specific project requirements and server environment.
<!--by longxuelin -->

<!--by lihuaju -->
README: Usage Tutorial for Main Features

Prerequisites Before you start using the project, make sure you have the following installed:
Python (version 3.x recommended) —— The Python 3.x version offers better compatibility and performance, supporting the latest features required by the project. Streamlit —— Used for quickly building and deploying data applications, providing a simple interface development experience. Pandas —— A powerful data - processing and analysis library for handling CSV data files in the project. Supabase Python client —— Facilitates interaction with the Supabase database, enabling data storage and retrieval.

You can install the required Python packages using pip:

bash pip install streamlit pandas supabase 2. Project Structure The project consists of several Python files and CSV data files. Here is a brief overview:

journal/main.py: A simple script with a link to itself. journal/form.py: Used to configure and launch the LLM and Telegram bot, and save the configuration to Supabase. journal/test.py: Manages the registration log of technical documentation and saves the data to test.csv. journal/pages/ПТО.py: Manages the quality control log of technical documentation lists and saves the data to PTO.csv. journal/set.py: Creates a form to configure a RAG chatbot and saves the data to Supabase. PTO.csv: Stores the quality control log data. test.csv: Stores the registration log data. 3. Main Function Operation Steps 3.1 Launching the LLM and Telegram Bot Configuration (journal/form.py) <!—by lihuaju> Run the Application Open your terminal and navigate to the journal directory. Run the following command to start the Streamlit application:

bash streamlit run form.py

This will open the application in your default web browser. <--by lihuaju>

Configure LLM In the 🧠 Конфигурация LLM section, enter your LLM API key in the API ключ LLM: field. The input is masked for security. Enter the name of your LLM model in the Название модели LLM: field. Optionally, expand the 🛠️ Расширенные настройки LLM section to configure advanced parameters such as system prompt, prompt, temperature, top K, max tokens, top P, frequency penalty, and presence penalty. <--by lihuaju> Configure Telegram Bot In the 🤖 Конфигурация Telegram бота section, enter your Telegram bot token in the Токен Telegram бота: field (masked) —— When entering the Telegram bot token, the input content will also be hidden to ensure the security of the token, which is a key credential for the bot to communicate with the Telegram server. Enter the Telegram chat ID in the ID чата Telegram: field. <--by member 6>—— Correctly enter the chat ID to ensure that the bot can accurately send messages to the specified Telegram chat group or individual. Launch LLM Click the 🚀 Запустить LLM button. If the launch is successful, the application will display the configuration details for both the LLM and the Telegram bot. It will then attempt to save the combined configuration to the Supabase database. A success or error message will be shown accordingly. <--by lihuaju> 3.2 Registering Technical Documentation (journal/test.py) <!—by lihuaju> Run the Application Navigate to the journal directory in your terminal. Run the command:

bash streamlit run test.py

The application will open in your web browser. <--by lihuaju>

Enter Documentation Information The application will display the last registered number—— Display the number of the last registration, facilitating users to understand the current registration sequence. In the form, enter the following information: Name of the document —— Accurately fill in the document name for easy subsequent searching and management. Developer of the document —— Record the developer of the document to clarify the responsibility. Position of the approver —— Fill in the position of the approver to reflect the standardization of the approval process. Number of pages —— Record the number of pages of the document to have a preliminary understanding of the document's scale. Storage location —— Indicate the storage location of the document for easy subsequent access to the physical or electronic storage path. Registration date —— Automatically or manually record the registration date for timeline management. Approval date —— Record the approval date to track the approval progress of the document. Notes (optional) —— If there is other information that needs to be explained, it can be filled in here. You can also upload the document if needed —— If there is an electronic document, it can be uploaded through this function to achieve a complete record of the document. <--by lihuaju> Submit the Form Click the Ввод button. If all required fields are filled, the data will be saved to test.csv, and a success message will be displayed —— If all required fields are filled, the data will be successfully saved to test.csv, and at the same time, a success message will be displayed to prompt the user that the operation is successful. 3.3 Recording Quality Control Log of Technical Documentation Lists (journal/pages/ПТО.py) <!—by lihuaju> Run the Application Navigate to the journal directory in your terminal —— Correctly switch to the journal directory in the terminal to ensure the correct command - execution environment. Run the command:

bash streamlit run pages/ПТО.py

The application will open in your web browser. <--by lihuaju>

Enter Quality Control Information In the sidebar form, enter the following information: Department —— Fill in the department information to clarify the responsible department for quality control. Developer —— Record the developer to facilitate tracing the source of the document. Receipt and inspection dates from different departments. Name of the document —— Confirm the document name again to ensure consistency with other records. Approver and approval dates from different departments —— Record the approvers and approval dates of different departments, reflecting a multi - level approval process. Remarks (optional). <--by lihuaju> —— If there are special circumstances or remarks information, it can be filled in here. Submit the Form Click the Ввод button. The data will be saved to PTO.csv, and a success toast message will be shown after a short wait. <--by lihuaju> 3.4 Creating a RAG Chatbot (journal/set.py) <!—by lihuaju> Run the Application Navigate to the journal directory in your terminal —— Switch to the correct journal directory in the terminal. Run the command:

bash streamlit run set.py

The application will open in your web browser. <--by lihuaju>

Enter Bot Configuration Information In the form, enter the Telegram bot token, API of your model, and API of the vector database. Click the Submit button. The configuration data will be saved to the Supabase set table, and a success message indicating that the bot has been created will be displayed. <--by lihuaju>
