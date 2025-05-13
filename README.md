
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


