
6. Configuration Page Layout Description
bash
LLM Configuration Area:
        1. API Key: Enter the API key of the LLM service provider.
        2. Model Name: Select the LLM model to be used.
Telegram Bot Configuration Area:
        1. Bot Token: Enter the Telegram Bot token obtained from BotFather.
        2. Chat ID: Enter the chat ID for receiving notifications.
Verification Options:
        You can choose to verify the validity of the LLM and Telegram configurations.
Submission Operation Feedback
Successful Saving:
        Display a green success message: "Configuration has been successfully saved!"
        If the verification option is checked, the configuration validity will be verified first.
        After successful verification, the corresponding success prompt will be displayed.
Possible Error Messages:
        Display a red error message when an input field is empty.
        Display the specific error reason when verification fails (such as API connection failure, invalid Bot token, etc.).
=======

Methods to Obtain SUPABASE_URL and SUPABASE_KEY

1.Create a Supabase Project
First, you need to register an account on the Supabase official website. After logging in, click "New Project" in the upper right corner to create a new project. After filling in the project name and region, wait for a few seconds and you will enter the project console.
Find SUPABASE_URL and SUPABASE_KEY
After entering the console, click "Settings" → "API" in the left menu bar.

2.SUPABASE_URL: It is below "Project URL" and looks like https://xxx.supabase.co. This is the "house number" of the project, which is used in the code to locate the database.
SUPABASE_KEY: In the "API Keys" area, there are many types of keys (public key, private key, service key, etc.). Click "View Key" and you will see a long string.

Steps to Configure Parameters in the Code (Taking Python as an Example)

1.Install the Library
Open the terminal and enter "pip install supabase" to install the official library.

2.Import the Module and Define the Parameters
Create a new Python file (for example, named supabase_demo.py). First, import the client creation function:

from supabase import create_client

Then define two variables to store the keys and the address obtained just now.

# Real values obtained from the Supabase console
SUPABASE_URL = "https://your_project_ID.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxxxxxxxxxxx"  # Service key


3.Create the Client and Operate the Database
Use these two parameters to create the client:

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


Next,you can operate the database! For example, operations like supabase.table("set").insert(data).execute() and querying data (such as supabase.table("set").select("*").execute()).




CSV File Format Requirements

1.File Encoding: Use UTF-8 encoding to avoid garbled Chinese characters.
2.Field Separator: Use an English comma (,) to separate column data.
3.Line Terminator: Use a newline character (\n). In the Windows system, it is commonly CRLF (\r\n).
4.Header: The first row should contain column names, and the field names should be consistent with the program logic.
5.Data Format:
1.Numeric fields (such as dates and numbers) should conform to the format required by the program (for example, the date format is YYYY-MM-DD).
2.If text fields contain special characters (such as commas and quotation marks), they should be enclosed in English double quotation marks (").

File Placement

1.Default Path:
If there is no special specification in the program, it is recommended to place the file in the same directory as the program (that is, in the same folder as the execution file/script).
Example path: C:\Users\YourName\Program\test.csv.
2.Custom Path:
If you need to specify another location, you need to clearly state the file path in the program configuration or code (such as D:\Data\PTO.csv), and ensure that the program has the read permission.

=======

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
=======

## 4.使用教程-技术文档登记日志(test.py 相关)

```bash
打开test.py文件后会有俄文的界面具体功能是上传技术文档
具体需要文档名称，开发者，批准者，页数，存储位置，注册日期，批准日期，备注的填写
在开发者和批准者等部分未填写时会进行报错
当填写齐全并且文档合法的情况下申请提交，文件会进入指定的文件夹并且申请记录会记录在表格上
```
=======

# Basic Environment Setup Guide

## I. Python Installation Steps
*(Windows-focused installation steps)*

### 1.1 Operating System Recommendations
- **Windows 10/11**: Use the latest stable release of Python 3.9.x
- **macOS**: Use Python 3.8+ (isolated from the system's built-in Python 2.7)
- **Linux**: Ubuntu 20.04 LTS or CentOS 8+ recommended

### 1.2 Windows Installation Steps
1. Download Python from the [official website](https://www.python.org/downloads/)
2. Select the **Windows installer (64-bit)** (version 3.8 or 3.9)
   ![12](https://github.com/user-attachments/assets/3beeb85a-9f6d-43eb-9011-95e8b21a2e48)
3. Run the installer and follow these steps:
   - Check "Add Python to PATH" (critical for command-line access)
   - Select "Customize installation"
     ![14](https://github.com/user-attachments/assets/81631a8e-9daf-4a89-9951-572714a60e17)
   - Ensure all optional features are selected (including pip and tcl/tk)
   - ![15](https://github.com/user-attachments/assets/211d288b-0e02-4da3-8f6c-d08839d45939)
   - In Advanced Options, enable "Install for all users"
     ![16](https://github.com/user-attachments/assets/3e350a1a-afae-4f6c-811e-3b676b1e3bd1)
   - Click "Install Now"
4.Verify installation:
Open Command Prompt (cmd) and run:
   ```bash
   python --version
    ![17](https://github.com/user-attachments/assets/3cf4d683-d86c-4159-8a4d-1f3e0848d975)

## 1.3 macOS Installation
### Option 1: Homebrew (Recommended)
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.9
brew install python@3.9

# Add to PATH (for zsh)
echo 'export PATH="/usr/local/opt/python@3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

## Option 2: Official Installer
1. Download the macOS 64-bit installer from [python.org](https://www.python.org/downloads/macos/).
2. Run the installer.
3. Verify:
   ```bash
   python3 --version
   pip3 --version

## 1.4 Linux Installation
### Ubuntu/Debian
```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.9 python3.9-dev python3.9-venv python3-pip
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

### CentOS/RHEL 
```bash
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel
wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz
tar xzf Python-3.9.7.tgz
cd Python-3.9.7
./configure --enable-optimizations
make altinstall

## II. Virtual Environment Setup
### 2.1 Creating a Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate

## macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate

## 2.2 Managing the Virtual Environment
**Activate:**
```bash
# Linux/macOS
source venv/bin/activate

# Windows
.\venv\Scripts\activate

**Deactivate**:  
```bash
Deactivate

**Delete**: 
Remove the `venv` directory:
```bash
rm -rf venv/
![18](https://github.com/user-attachments/assets/ccaa38bd-ea01-43e1-b2d2-955731c89649)

## III. Installing Project Dependencies
### 3.1 Updating pip
```bash
python -m pip install --upgrade pip
![21](https://github.com/user-attachments/assets/c0823694-28bb-4e3e-9811-3cbbc67f8e49)


### 3.2 Installing Core Dependencies
```bash
pip install --upgrade pip wheel setuptools
![19](https://github.com/user-attachments/assets/df284593-39ed-419b-86b2-c02233e0fa82)

### 3.3 Installing Main Libraries
```bash
pip install streamlit==1.22.0 pandas==1.5.3 supabase==2.3.1 python-dotenv==0.21.0
# OR (from requirements.txt)
pip install -r requirements.txt
![20](https://github.com/user-attachments/assets/d09f537e-65c7-4ec9-b0c2-c9307093b039)



### 3.4 Key Libraries Overview
| Library    | Installation Command       | Minimum Version |
|------------|----------------------------|-----------------|
| Streamlit  | `pip install streamlit`    | `>=1.22.0`      |
| Pandas     | `pip install pandas`       | `>=1.3.0`       |
| Supabase   | `pip install supabase`     | `>=2.3.1`       |

## IV. Running the Project
### 4.1 Cloning the Repository
```bash
git clone https://github.com/longxuelin/journal.git
cd journal
![克隆仓库](https://github.com/user-attachments/assets/6cc358c5-0080-49d8-8d2d-1f9522e34bd0)

## 4.2 Launching the Application
### Main Program:
```bash
streamlit run app.py

### Specific Modules：
```bash
# PTO Module
streamlit run ПТО.py

# Test Module
streamlit run test.py
![25](https://github.com/user-attachments/assets/906f4e51-325e-4d32-9ef7-f1a5545984c9)

<!-- By Liu Yilin -->
=======

I. Project Background Information
Repository Address: https://github.com/Limingxia890/journal
This project is a collection of applications meticulously developed based on the Streamlit framework. Streamlit, as a powerful open-source Python library, enables the rapid transformation of data science scripts into interactive web applications. This project leverages this advantage to create a feature-rich and user-friendly platform.

The project encompasses multiple key functional modules, including but not limited to the registration and management of technical documents, the classification, storage, and retrieval of electronic journals, as well as the configuration and interaction interfaces for Large Language Models (LLMs) and chatbots. Through these functionalities, users can conveniently record technical documents, manage electronic journal resources, and also configure and test chatbots to achieve intelligent interactive experiences.

The core purpose of the project is to provide a set of efficient tools for data recording, management, and interaction for related work. Whether researchers, engineers, or developers, users can find functionalities that meet their needs on this platform, thereby completing their work more efficiently. Through Streamlit's intuitive interface and powerful functionalities, this project significantly simplifies complex data processing workflows, improves work efficiency, and also offers users more customization options to adapt to different usage scenarios.

II. Project Architecture Analysis
Architecture Design
Frontend: User interface for interaction.
Backend: Backend services for data storage, user authentication, etc.
Database: For storing logs, user information, and other data.
Key Module Analysis
User Management Module: Responsible for user registration, login, permission management, etc.
Log Recording Module: Provides functionalities for creating, editing, deleting, and viewing logs.
Search and Classification Module: Supports searching logs by keywords, dates, tags, etc., as well as log classification management.
Sharing and Collaboration Module: Allows users to share logs with other users or teams, supports multi-user collaborative editing.
Technology Selection and Characteristics
Technology Selection: Lightweight technology stack.
Characteristics: Emphasis on user experience, data security, scalability, etc.
III. Detailed梳理 (Detailed Breakdown) of Functional Modules
User Interface
Login/Registration Page: Provides login and registration functionalities for users.
Home Page: Displays the user's log list, supports quick creation of new logs.
Log Detail Page: Displays the detailed content of logs, supports editing and deletion operations.
Settings Page: Allows users to configure personal preferences, account security, etc.
Log Management
Create Log: Provides a rich text editor, supports inserting images, links, etc.
Edit Log: Allows users to modify existing logs at any time.
Delete Log: Provides deletion functionality, supports batch deletion.
Log Classification and Tags: Supports adding categories and tags to logs for easier management and searching.
Search and Filter
Keyword Search: Supports searching logs by keywords.
Date Filter: Supports filtering logs by date range.
Tag Filter: Supports filtering logs by tags.
Sharing and Collaboration
Share Log: Allows users to share logs with other users or generate sharing links.
Collaborative Editing: Supports multiple users editing the same log simultaneously (if implemented).
Notifications and Reminders
Log Update Notifications: Notifies the original author when a log is edited or commented on by other users.
Task Reminders: (If the project includes task management functionalities) Supports setting task reminders.
IV. Summary of Collected Information and Subsequent Recommendations
Information Summary
The project "journal" aims to provide a log management platform that supports personal note management and team collaboration.
The project adopts a certain technology stack (specific details need to be viewed in the code), emphasizing user experience and data security.
Functional modules include user interface, log management, search and filter, sharing and collaboration, etc.
Subsequent Recommendations
Feature Expansion: Consider adding new functionalities based on user needs and market feedback, such as task management, scheduling, etc.
Community Building: Encourage user feedback and contributions, establish a project community to promote project development.
In summary, this project is a comprehensive platform integrating multiple practical functionalities, aiming to provide all-round support for related work through the Streamlit framework, assisting users in more efficiently completing data recording, management, and interaction tasks.
=======
1. Page Layout and Functionality:
1.1 Layout
The application employs a layout with a sidebar on the left and a main content area on the right.
Sidebar: It serves as the input interface for journal data. It contains multiple input fields for data entry, such as department, developer, and various date - related fields. It also supports form validation, with mandatory fields marked (e.g., the "Разработчик" field).
Main Content Area: This area displays a table of added journal data. The table shows key information about the journals, including department, developer, and different dates. It also supports functions like data filtering and sorting.
1.2 Functionality
The sidebar is designed for users to input journal - related data. After successful submission, the data is presented in the table in the main content area.
2. Sidebar Journal Data Entry Fields:
2.1 Department (Подразделение)
Meaning: Indicates the department or section to which the journal belongs.
Input Method: Users are provided with a dropdown list that contains preset options. These options typically include names of various departments such as "АХО" (which could stand for a specific administrative or operational department) and "ИТ" (presumably the Information Technology department). The user simply selects the appropriate department from this list.
Example: АХО
2.2 Developer (Разработчик)
Meaning: Refers to the main person responsible for the journal content.
Input Method: It is a text - input field where users must manually type in the name. As a mandatory field, it is essential for accurately attributing the journal to its creator and for tracking purposes.
Example: Иванов И.И.
2.3 Receipt Date (ГУД)
Meaning: The date when the journal is first received by the system (general date).
Input Method: The application provides a date picker widget, which conforms to the YYYY-MM-DD format. This standard format ensures consistency and ease of comparison across different journal records. Users can click on the date picker to select the appropriate date from a calendar interface.
Example: 2025-05-13
2.4 Review Date (ГУД)
Meaning: The date when the journal content is first reviewed and approved (general date).
Input Method: Similar to the receipt date field, it uses a date picker with the YYYY-MM-DD format. Users can select the date from the calendar widget, which helps in maintaining a standardized record - keeping system.
Example: 2025-05-13
2.5 Receipt Date (ПППД)
Meaning: The date when the journal is received in a specific process (e.g., "ПППД").
Input Method: It also employs a date picker with the YYYY-MM-DD format. Users can easily select the relevant date from the provided calendar interface, ensuring accurate recording of this specific event.
Example: 2025-05-13
2.6 Review Date (ПППД)
Meaning: The date when the journal is reviewed in a specific process (e.g., "ПППД").
Input Method: Just like the other date fields, it uses a date picker with the YYYY-MM-DD format. Users can choose the appropriate date from the calendar, maintaining the integrity of the data records.
Example: 2025-05-13
2.7 Form Validation Rules
Mandatory Field: Разработчик (Developer) must be filled.
Date Format: Automatically verified to conform to the YYYY-MM-DD standard.
Department Selection: Only allow selection from the preset values in the dropdown list.
3. Prompt Information after Successful Data Submission:
When the user successfully submits the journal data, the system will:
Automatically add a new record to the table in the main content area.
Provide an implicit indication of successful submission (no pop - up, confirmed by table update).
Keep the form field values for continuous entry of multiple data entries.
4. Data Presentation in the Table:
The journal data is presented in a table in the main content area with the following columns:
Serial Number	Department (Подразделение)	Developer (Разработчик)	Receipt Date (ГУД)	Review Date (ГУД)	Receipt Date (ПППД)	Review Date (ПППД)
1	АХО	dsdsdsd	2024-03-07	2024-03-07	2024-03-07	2024-03-07
5. Screenshots of the Operation Process:
5.1 Journal Addition Page
   nnotation: This screenshot is essential for visualizing the data entry interface.
5.2 Table Update after Successful Submission
   Annotation: Illustrates the result of a successful data submission.
6. Technical Implementation Details:
6.1 Development Framework
The application is developed using Streamlit.
Annotation: Streamlit provides a rapid - development framework for data - centric applications.
6.2 Data Storage
Currently, data is stored in memory. It is recommended to connect to a database in the future.
Annotation: Memory - based storage is suitable for local testing, but database integration is crucial for production - level data persistence.
6.3 Deployment
The application is run locally (localhost:8501).
Annotation: Local deployment is useful for development and testing phases.
6.4 Date Format
The date format used is YYYY-MM-DD, which conforms to the ISO 8601 standard.
Annotation: Adhering to this standard ensures interoperability and clarity in date representation.





