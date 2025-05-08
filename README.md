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
