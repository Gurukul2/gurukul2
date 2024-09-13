import pyodbc

def pullFromDatabase():
    query = """
        SELECT FirstName, LastName, Salary FROM Employees
        """
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\sqlexpress;DATABASE=Test 1;Trusted_Connection=yes')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()
    result_data = []
    for row_data in rows:
        idx = 0
        named_values = {}
        for colvalue in row_data:
            colname = row_data.cursor_description[idx][0]
            named_values[colname] = colvalue
            idx += 1
        result_data.append(named_values)
    return result_data

data = pullFromDatabase()
print(data)
