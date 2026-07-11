import sqlite3, json

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

tables = [
    'clients_bankingrelationship', 'clients_historicalbankingrelationship',
    'clients_le_le_bankingrelationship', 'clients_le_historicalle_bankingrelationship'
]
fields = ['account_and_securities_statements', 'communication_br', 'type_and_purpose']

for table in tables:
    for field in fields:
        try:
            cursor.execute(f"SELECT id, {field} FROM {table}")
            for row_id, val in cursor.fetchall():
                if val:
                    try:
                        json.loads(val)
                    except json.JSONDecodeError:
                        cursor.execute(f"UPDATE {table} SET {field} = ? WHERE id = ?", (json.dumps([val]), row_id))
        except sqlite3.OperationalError:
            pass

conn.commit()
conn.close()
print("Done. Now run: python manage.py migrate")