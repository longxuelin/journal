# 基础环境搭建指南
## Python 安装步骤（安装步骤仅重点介绍Windows 系统）
### 1.1 操作系统选择建议(仅介绍三种)
- **Windows 10/11**：推荐使用最新稳定版 Python 3.9.x  
- **macOS**：建议使用 Python 3.8+ (与系统自带的 Python 2.7 隔离)  
- **Linux**：推荐 Ubuntu 20.04 LTS 或 CentOS 8 以上版本  

### 1.2 Windows 系统安装步骤
1. 访问 Python 官方网站下载: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. 选择"Windows installer (64-bit)" 下载 （版本：3.8 或 3.9）  
3. 双击运行下载的安装程序  
4. **重点注意**：在安装界面勾选"Add Python to PATH"选项  
5. 选择 "Customize installation"  
6. 勾选所有可选功能（包括 pip 和 tcl/tk）  
7. 高级选项中勾选 "Install for all users"  
8. 点击"Install Now"进行安装  
9. 安装完成后，打开命令提示符(cmd)输入 `python --version` 验证安装  

### 1.3 macOS 系统详细安装
#### Homebrew 安装方式（推荐）：
```bash
# 先安装 Homebrew（如未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Python
brew install python@3.9

# 添加环境变量
echo 'export PATH="/usr/local/opt/python@3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

###官方安装包方式：
1. 下载 macOS 64-bit installer  
2. 双击运行安装向导  
3. 安装完成后运行：  
   ```bash
   python3 --version
   pip3 --version

## 1.4 Linux 系统详细安装
### Ubuntu/Debian：
```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.9 python3.9-dev python3.9-venv python3-pip
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

### CentOS/RHEL：
```bash
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel
wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz
tar xzf Python-3.9.7.tgz
cd Python-3.9.7
./configure --enable-optimizations
make altinstall

## 二、虚拟环境配置
### 2.1 创建虚拟环境
#### Windows
```bash
python -m venv venv
venv\Scripts\activate

## macOS/Linux 
```bash
python3 -m venv venv
venvsource venv/bin/activate

# 激活环境
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
# 退出环境
deactivate
# 删除环境（只需删除 venv 目录即可）
rm -rf venv/

## 三、项目依赖安装
### 使用 pip 安装依赖库
#### 更新 pip 至最新版本
```bash
python -m pip install --upgrade pip

### 基础依赖安装
```bash
pip install --upgrade pip wheel setuptools

### 主要依赖安装
```bash
pip install streamlit==1.22.0 pandas==1.5.3 supabase==2.3.1 python-dotenv==0.21.0
# 或从requirements.txt安装所有依赖
pip install -r requirements.txt

## 各主要依赖库说明
### Streamlit
**安装命令**：`pip install streamlit`
**版本要求**：>=1.22.0

### Pandas
**安装命令**：`pip install pandas`
**版本要求**：>=1.3.0

### Supabase
**安装命令**：`pip install supabase`
**版本要求**：>=2.3.1

## 四、项目运行
### 克隆项目仓库
```bash
git clone https://github.com/longxuelin/journal.git
cd journal

### 运行主程序
```bash
streamlit run app.py

## 或运行特定模块
```bash
# 运行PTO模块
streamlit run ПТО.py
# 运行测试模块
streamlit run test.py

<!--by 刘奕麟 -->
