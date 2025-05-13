1. Server Configuration
Author: wuhui
The project is intended to be deployed on a Windows system. The following server configurations are recommended:

Operating System: Windows Server 2019 or later.
CPU: At least 2 cores.
Memory: At least 4GB RAM.
Storage: At least 50GB of free disk space.
2. Network Settings
Firewall
Author: wuhui
Make sure the necessary ports are open in the Windows Firewall. For a Streamlit application, by default, it uses port 8501. So, you should open port 8501 for inbound and outbound traffic.
DNS
Author: wuhui
Set up the correct DNS records to point to the server's IP address if the project needs to be accessed via a domain name.
3. Deployment Process
Step 1: Clone the Repository
Author: wuhui
Open the Command Prompt or PowerShell on your Windows server and run the following command to clone the project repository:

bash
git clone https://github.com/MagneticDogSon/journal.git
cd journal
Step 2: Install Python
Author: wuhui
If Python is not installed on your server, download and install Python 3.8 or higher from the official Python website (https://www.python.org/downloads/). After installation, verify the Python version by running:

bash
python --version
Step 3: Create a Virtual Environment (Optional but Recommended)
Author: wuhui
It's a good practice to create a virtual environment to isolate the project's dependencies. Run the following commands:

bash
python -m venv myenv
myenv\Scripts\activate
Step 4: Install Dependencies
Author: wuhui
Install Streamlit and other project dependencies.

bash
pip install streamlit
Step 5: Start the Streamlit Application
Author: wuhui
Since no application configuration was done, run the following command to start the Streamlit app. The main Python script is named main.py.

bash
streamlit run main.py
4. Verification
Author: wuhui
After the application is started, open a web browser and enter the server's IP address followed by :8501 (e.g., http://<server_ip>:8501). You should see your Streamlit application running.
5. Project Structure and Key Files Explanation
main.py
Author: wuhui
The main.py file is the entry - point of the Streamlit application. It uses the Streamlit library to create a simple web interface. Specifically, it imports the streamlit library and defines a variable url with the value 'main.py'. Then it uses the st.markdown function to display a clickable link in the web application, with the link text "check out this link" and the link pointing to the main.py file itself.

python
运行
import streamlit as st

url = 'main.py'
st.markdown("check out this [link](%s)" % url)
Other Files
set.py: Interacts with Supabase to manage settings for creating a RAG chat - bot. It allows users to input a Telegram bot token, API of the model, and API of the vector database and saves the Telegram bot token to the Supabase set table.
form.py: Provides functionality for configuring and launching an LLM (Large Language Model) and a Telegram bot. It also includes functions to save the configuration data to the Supabase set table.
pages/ПТО.py: Creates a Streamlit page for recording data related to the "Журнал нормконтроля перечней ТД в ПТО". It reads data from a CSV file, provides a form for users to input new data, and displays the data in a table.
test.py: Similar to pages/ПТО.py, it is used for recording data related to the "Журнал регистрации технической документации ОИТПЭ". It generates a registration number, provides a form for data input, and displays data in a table.
