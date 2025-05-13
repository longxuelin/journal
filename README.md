### Server Deployment and Project Documentation

#### 1. Server Configuration
**Author**: wuhui

This project is intended to be deployed on a Windows system. To ensure the stable operation of the project, the following server configurations are recommended:
- **Operating System**: Windows Server 2019 or a higher version to ensure sufficient compatibility and performance support.
- **CPU**: At least 2 cores, capable of handling multi - threaded tasks to ensure the application runs stably under high loads.
- **Memory**: At least 4GB of RAM, providing sufficient memory space for project operation and data processing to avoid performance bottlenecks caused by insufficient memory.
- **Storage**: At least 50GB of available disk space for storing project files, logs, and potential temporary data.

#### 2. Network Settings

##### Firewall
**Author**: wuhui

Ensure that the necessary ports are opened in the Windows Firewall. By default, a Streamlit application uses port 8501 for network communication. Therefore, you need to open port 8501 for both inbound and outbound traffic. The specific steps are as follows:
1. Open the "Windows Firewall" settings.
2. Click on "Advanced settings".
3. Create new rules in both "Inbound rules" and "Outbound rules".
4. Select "Port", and then specify TCP port 8501.
5. Allow the connection and complete the rule creation.

##### DNS Resolution
**Author**: wuhui

If you need to access the project via a domain name, set up the correct DNS records to point to the server's IP address. The specific steps are as follows:
1. Log in to the domain management platform.
2. Find the DNS management or resolution settings option.
3. Add an A record to point the domain name to the server's IP address.
4. Wait for the DNS resolution to take effect, which usually takes from a few minutes to a few hours.

#### 3. Deployment Process

##### Step 1: Clone the Repository
**Author**: wuhui

Open the Command Prompt or PowerShell on your Windows server and run the following commands to clone the project repository:
```bash
git clone https://github.com/MagneticDogSon/journal.git
cd journal
```

##### Step 2: Install Python
**Author**: wuhui

If Python is not installed on your server, download and install Python 3.8 or a higher version from the official Python website (https://www.python.org/downloads/). After installation, verify the Python version by running the following command:
```bash
python --version
```

##### Step 3: Create a Virtual Environment (Optional but Recommended)
**Author**: wuhui

To isolate the project's dependencies and avoid conflicts between different projects, it is recommended to create a virtual environment. Run the following commands:
```bash
python -m venv myenv
myenv\Scripts\activate
```

##### Step 4: Install Dependencies
**Author**: wuhui

Install Streamlit and other project dependencies:
```bash
pip install streamlit
```

##### Step 5: Start the Streamlit Application
**Author**: wuhui

Since the application configuration is not completed, run the following command to start the Streamlit application. The main Python script is named `main.py`:
```bash
streamlit run main.py
```

#### 4. Verification
**Author**: wuhui

After the application is started, open a web browser and enter the server's IP address followed by `:8501` (e.g., `http://<server_ip>:8501`). You should see the Streamlit application running.

#### 5. Project Structure and Key File Explanation

##### `main.py`
**Author**: wuhui

The `main.py` file is the entry point of the Streamlit application. It uses the Streamlit library to create a simple web interface. The specific functionality is as follows:
```python
import streamlit as st

url = 'main.py'
st.markdown("check out this [link](%s)" % url)
```
The above code imports the `streamlit` library and defines a variable `url` with a value of `'main.py'`. Then, it uses the `st.markdown` function to display a clickable link in the web application. The link text is "check out this link", and the link points to the `main.py` file itself. This link can serve as a navigation entry for the project, making it convenient for users to view the main file of the project.

##### `set.py`
This file is mainly responsible for interacting with Supabase to manage the settings for creating a RAG chat - bot. The specific functions include:
- Allowing users to enter the Telegram bot Token, the API of the model, and the API of the vector database.
- Saving the Telegram bot Token to the `set` table in Supabase for subsequent use.

##### `form.py`
This file provides the functionality to configure and start an LLM (Large Language Model) and a Telegram bot. The specific process is as follows:
1. Providing a form for users to enter the API key of the LLM, the model name, system prompts, prompt information, and other advanced setting parameters.
2. Allowing users to enter the Telegram bot's Token and chat ID.
3. When users submit the form, merging the configuration data and saving it to the `set` table in Supabase.
4. Displaying the configuration information and prompting users that the LLM and Telegram bot have been successfully started.

##### `pages/ПТО.py`
This file creates a Streamlit page for recording data related to "Журнал нормконтроля перечней ТД в ПТО". The specific operations are as follows:
1. Reading data from the `PTO.csv` file.
2. Providing a form for users to enter new data, such as department, developer, date, etc.
3. When users submit the form, appending the new data to the `PTO.csv` file.
4. Displaying all data in a table on the page for users to view and manage.

##### `test.py`
Similar to `pages/ПТО.py`, `test.py` is used to record data related to "Журнал регистрации технической документации ОИТПЭ". The specific functions are as follows:
1. Automatically generating a registration number to ensure that each record has a unique identifier.
2. Providing a form for users to enter information such as the document name, developer, date, number of pages, etc.
3. Allowing users to upload relevant documents.
4. When users submit the form, appending the new data to the `test.csv` file.
5. Displaying all data in a table on the page for users to view and manage.
