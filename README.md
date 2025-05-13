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
3. Run the installer and follow these steps:
   - Check "Add Python to PATH" (critical for command-line access)
   - Select "Customize installation"
   - Ensure all optional features are selected (including pip and tcl/tk)
   - In Advanced Options, enable "Install for all users"
   - Click "Install Now"
4.Verify installation:
Open Command Prompt (cmd) and run:
   ```bash
   python --version

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

## III. Installing Project Dependencies
### 3.1 Updating pip
```bash
python -m pip install --upgrade pip

## III. Installing Project Dependencies
### 3.1 Updating pip
```bash
python -m pip install --upgrade pip

### 3.2 Installing Core Dependencies
```bash
pip install --upgrade pip wheel setuptools

### 3.3 Installing Main Libraries
```bash
pip install streamlit==1.22.0 pandas==1.5.3 supabase==2.3.1 python-dotenv==0.21.0

# OR (from requirements.txt)
pip install -r requirements.txt

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

<!-- By Liu Yilin -->
