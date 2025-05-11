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
1. Prerequisites
Before you start using the project, make sure you have the following installed:

Python (version 3.x recommended)
Streamlit
Pandas
Supabase Python client

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
3.1 Launching the LLM and Telegram Bot Configuration (journal/form.py) <!—by member 5>
Run the Application
Open your terminal and navigate to the journal directory.
Run the following command to start the Streamlit application:

bash
streamlit run form.py

This will open the application in your default web browser. <--by member 6>

Configure LLM
In the 🧠 Конфигурация LLM section, enter your LLM API key in the API ключ LLM: field. The input is masked for security.
Enter the name of your LLM model in the Название модели LLM: field.
Optionally, expand the 🛠️ Расширенные настройки LLM section to configure advanced parameters such as system prompt, prompt, temperature, top K, max tokens, top P, frequency penalty, and presence penalty. <--by member 6>
Configure Telegram Bot
In the 🤖 Конфигурация Telegram бота section, enter your Telegram bot token in the Токен Telegram бота: field (masked).
Enter the Telegram chat ID in the ID чата Telegram: field. <--by member 6>
Launch LLM
Click the 🚀 Запустить LLM button.
If the launch is successful, the application will display the configuration details for both the LLM and the Telegram bot.
It will then attempt to save the combined configuration to the Supabase database. A success or error message will be shown accordingly. <--by member 6>
3.2 Registering Technical Documentation (journal/test.py) <!—by member 5>
Run the Application
Navigate to the journal directory in your terminal.
Run the command:

bash
streamlit run test.py

The application will open in your web browser. <--by member 6>

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
You can also upload the document if needed. <--by member 6>
Submit the Form
Click the Ввод button.
If all required fields are filled, the data will be saved to test.csv, and a success message will be displayed. Otherwise, an error message will prompt you to fill in the necessary fields. <--by member 6>
3.3 Recording Quality Control Log of Technical Documentation Lists (journal/pages/ПТО.py) <!—by member 5>
Run the Application
Navigate to the journal directory in your terminal.
Run the command:

bash
streamlit run pages/ПТО.py

The application will open in your web browser. <--by member 6>

Enter Quality Control Information
In the sidebar form, enter the following information:
Department.
Developer.
Receipt and inspection dates from different departments.
Name of the document.
Approver and approval dates from different departments.
Remarks (optional). <--by member 6>
Submit the Form
Click the Ввод button.
The data will be saved to PTO.csv, and a success toast message will be shown after a short wait. <--by member 6>
3.4 Creating a RAG Chatbot (journal/set.py) <!—by member 5>
Run the Application
Navigate to the journal directory in your terminal.
Run the command:

bash
streamlit run set.py

The application will open in your web browser. <--by member 6>

Enter Bot Configuration Information
In the form, enter the Telegram bot token, API of your model, and API of the vector database.
Click the Submit button.
The configuration data will be saved to the Supabase set table, and a success message indicating that the bot has been created will be displayed. <--by member 6>

This concludes the main function usage tutorial for the project. Make sure to follow the steps carefully and refer to the screenshots for better understanding.
