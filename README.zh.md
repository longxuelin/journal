
# 基础环境搭建指南
## Python 安装步骤（安装步骤仅重点介绍Windows 系统）
### 1.1 操作系统选择建议(仅介绍三种)
- **Windows 10/11**：推荐使用最新稳定版 Python 3.9.x  
- **macOS**：建议使用 Python 3.8+ (与系统自带的 Python 2.7 隔离)  
- **Linux**：推荐 Ubuntu 20.04 LTS 或 CentOS 8 以上版本  

### 1.2 Windows 系统安装步骤
1. 访问 Python 官方网站下载: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
2. 选择"Windows installer (64-bit)" 下载 （版本：3.8 或 3.9）
    ![12](https://github.com/user-attachments/assets/c5073cdf-c9e5-4b48-a2c8-d17ebd3a9bf1)
3. 双击运行下载的安装程序  
4. **重点注意**：在安装界面勾选"Add Python to PATH"选项  
5. 选择 "Customize installation"
     ![14](https://github.com/user-attachments/assets/5c1a6bf8-774e-4a03-9187-423ae2d5e61f)
6. 勾选所有可选功能（包括 pip 和 tcl/tk）
   ![15](https://github.com/user-attachments/assets/e2e7f008-e515-4f4d-81ef-f59ba4324545)
7. 高级选项中勾选 "Install for all users"
    ![16](https://github.com/user-attachments/assets/9504c16e-1338-4642-b6ec-d18858024275)
8. 点击"Install Now"进行安装  
9. 安装完成后，打开命令提示符(cmd)输入 `python --version` 验证安装
    ![17](https://github.com/user-attachments/assets/82884994-da26-4731-b785-c2f66158479a)
 
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
![18](https://github.com/user-attachments/assets/798b31ed-0a7b-4a2c-82ac-00302a73cb23)

## 三、项目依赖安装
### 使用 pip 安装依赖库
#### 更新 pip 至最新版本
```bash
python -m pip install --upgrade pip
![21](https://github.com/user-attachments/assets/ee273ef0-ac77-41fa-9d9f-2a0c50a54aa1)

### 基础依赖安装
```bash
pip install --upgrade pip wheel setuptools
![19](https://github.com/user-attachments/assets/67d5762b-e4aa-4191-8177-3eecc53a7207)

### 主要依赖安装
```bash
pip install streamlit==1.22.0 pandas==1.5.3 supabase==2.3.1 python-dotenv==0.21.0
# 或从requirements.txt安装所有依赖
pip install -r requirements.txt
![20](https://github.com/user-attachments/assets/ab9be1bf-974b-4552-9daf-ace25b53cafe)

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
![克隆仓库](https://github.com/user-attachments/assets/bca0c197-edcc-470c-a303-f9395ac5d51b)

### 运行主程序
```bash
streamlit run app.py

## 或运行特定模块
```bash
# 运行PTO模块
streamlit run ПТО.py
# 运行测试模块
streamlit run test.py
![25](https://github.com/user-attachments/assets/fbaf2d30-9e87-4473-9169-1236fcb0bbf1)


<!--by 刘奕麟 -->
=======
中文版
一、项目背景信息

仓库地址: https://github.com/Limingxia890/journal
该项目是一组基于Streamlit框架精心开发的应用程序集合。Streamlit作为一个强大的开源Python库，能够快速将数据科学脚本转化为交互式Web应用，本项目正是利用了这一优势，打造了一个功能丰富且用户友好的平台。

该项目涵盖了多个关键功能模块，包括但不限于技术文档的登记与管理、电子期刊的分类存储与检索，以及大型语言模型（LLM）和聊天机器人的配置与交互界面。通过这些功能，用户可以方便地记录技术文档，管理电子期刊资源，同时还能配置和测试聊天机器人，实现智能化的交互体验。

项目的核心宗旨在于为相关工作提供一套高效的数据记录、管理和交互工具。无论是科研人员、工程师还是开发者，都能在这个平台上找到满足自己需求的功能，从而更加高效地完成工作。通过Streamlit的直观界面和强大的功能，本项目极大地简化了复杂的数据处理流程，提高了工作效率，同时也为用户提供了更多的自定义选项，以适应不同场景下的使用需求。

二、项目架构分析
1.架构设计
前端: 前端界面，用于用户交互。
后端: 后端服务，用于处理数据存储、用户认证等。
数据库: 用于存储日志、用户信息等数据。

2.关键模块分析
用户管理模块: 负责用户注册、登录、权限管理等功能。
日志记录模块: 提供日志的创建、编辑、删除、查看等功能。
搜索与分类模块: 支持按关键词、日期、标签等条件搜索日志，以及日志的分类管理。
分享与协作模块: 允许用户分享日志给其他用户或团队，支持多人协作编辑。

3.技术选型与特点
技术选型: 轻量级技术栈。
特点: 注重用户体验、数据安全性、可扩展性等。

三、功能模块详细梳理
1.用户界面
登录/注册页面: 提供用户登录和注册功能。
主页: 展示用户的日志列表，支持快速创建新日志。
日志详情页: 展示日志的详细内容，支持编辑和删除操作。
设置页面: 允许用户配置个人偏好、账户安全等。
2.日志管理
创建日志: 提供富文本编辑器，支持插入图片、链接等。
编辑日志: 允许用户随时修改已创建的日志。
删除日志: 提供删除功能，支持批量删除。
日志分类与标签: 支持为日志添加分类和标签，便于管理和搜索。
3.搜索与过滤
关键词搜索: 支持按关键词搜索日志。
日期过滤: 支持按日期范围过滤日志。
标签过滤: 支持按标签过滤日志。
4.分享与协作
分享日志: 允许用户将日志分享给其他用户或生成分享链接。
协作编辑: 支持多人同时编辑同一篇日志（如果实现）。
通知与提醒
日志更新通知: 当日志被其他用户编辑或评论时，通知原作者。
任务提醒: （如果项目包含任务管理功能）支持设置任务提醒。

四、收集的信息总结与后续建议
1.信息总结
项目“journal”旨在提供一个日志管理平台，支持个人笔记管理和团队协作。
项目采用了一定的技术栈（具体需查看代码），注重用户体验和数据安全性。
功能模块包括用户界面、日志管理、搜索与过滤、分享与协作等。
2.后续建议
功能扩展: 根据用户需求和市场反馈，考虑添加新功能，如任务管理、日程安排等。
社区建设: 鼓励用户反馈和贡献，建立项目社区，促进项目发展。
总之，该项目是一个集成了多种实用功能的综合性平台，旨在通过Streamlit框架为相关工作提供全方位的支持，助力用户更加高效地完成数据记录、管理和交互任务。
