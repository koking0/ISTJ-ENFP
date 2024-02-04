import pandas as pd
import sqlite3

# 步骤1: 读取CSV文件
file_path = r'D:\Program Files\MemoTrace\data\聊天记录\宇宙超级无敌美少女\宇宙超级无敌美少女_utf8.csv'  # 修改为实际的文件路径
df = pd.read_csv(file_path)

# 步骤2: 建立SQLite数据库连接
conn = sqlite3.connect('db.sqlite3')  # SQLite数据库路径

# 步骤3: 将数据写入SQLite数据库
# 注意: 如果app_chatrecord表已经存在，并且你想添加这些记录到现有表中，使用if_exists='append'
# 如果表不存在，pandas会自动创建表
df.to_sql('app_chatrecord', conn, if_exists='append', index=False)

# 关闭数据库连接
conn.close()

