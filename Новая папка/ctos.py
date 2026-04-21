import pandas as pd
from sqlalchemy import create_engine

# 2. Сохраняем в CSV (на всякий случай)
csv_file = 'titanic.csv'
df=pd.read_csv(csv_file)

# 3. Настройки подключения к PostgreSQL
# Формат: 'postgresql://username:password@localhost:5432/database_name'
engine = create_engine('postgresql://postgres:admin@localhost:5432/titanic')

# 4. Загружаем данные в таблицу SQL
# name - имя таблицы в базе, if_exists='replace' создаст таблицу заново
df.to_sql('users_table', engine, if_exists='replace', index=False)

print("Данные успешно загружены в базу!")
