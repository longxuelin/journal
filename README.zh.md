获取 SUPABASE_URL 和 SUPABASE_KEY 的方法
 
1. 创建 Supabase 项目
 
首先得在 Supabase 官网 注册账号，登录后点击右上角 New Project 创建新项目。填完项目名称和区域后，等待几秒就会进入项目控制台了。
 
2. 查找 SUPABASE_URL 和 SUPABASE_KEY
 
进入控制台后，点击左侧菜单栏的 Settings → API 
- SUPABASE_URL：在 Project URL 下面，长得像  https://xxx.supabase.co ，这是项目的「门牌号」，代码里靠它找到数据库。
 
- SUPABASE_KEY：在 API Keys 区域，这里有很多类型的密钥（公钥、私钥、服务密钥等）。点击 View Key 就能看到一串很长的字符串。


在代码中配置参数的步骤（以 Python 为例）
 
1. 安装库
 
打开终端，输入  pip install supabase  安装官方库。
 
2. 导入模块并定义参数
 
新建一个 Python 文件（比如叫  supabase_demo.py ），先导入客户端创建函数：
 
  
from supabase import create_client  
 
 
然后定义两个变量存刚才拿到的密钥和地址。

# 从 Supabase 控制台获取的真实值  
SUPABASE_URL = "https://你的项目ID.supabase.co"  
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxxxxxxxxxxx"  # 服务密钥

3. 创建客户端并操作数据库
 
用这两个参数创建客户端：
   
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)  
 
 
接下来就可以操作数据库了！如 supabase.table("set").insert(data).execute() ）、查询数据（如 supabase.table("set").select("*").execute() ）等数据库操作。 




CSV文件格式要求
 
1. 文件编码：使用UTF-8编码（避免中文乱码）。
 
2. 字段分隔符：使用英文逗号（ , ）分隔列数据。
 
3. 行终止符：使用换行符（ \n ），Windows系统常见为CRLF（ \r\n ）。
 
4. 表头：首行需包含列名，字段名需与程序逻辑一致。
 
5. 数据格式：
 
- 数值型字段（如日期、数字）需符合程序要求的格式（如日期为 YYYY-MM-DD ）。
 
- 文本型字段若包含特殊字符（如逗号、引号），需用英文双引号（ " ）包裹


文件放置位置
 
1. 默认路径：
 
- 若程序无特殊指定，建议将文件放置于程序同级目录（即与执行文件/脚本在同一文件夹）。
 
- 示例路径： C:\Users\YourName\Program\test.csv 。
 
2. 自定义路径：
 
- 若需指定其他位置，需在程序配置或代码中明确文件路径（如 D:\Data\PTO.csv ），确保程序有读取权限。

  
