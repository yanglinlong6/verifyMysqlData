from openpyxl import load_workbook
import connectiontool.connection as Connection

gpsConn = Connection.Mysql(
    host='192.168.5.22',
    port=3307,
    dbname='gps',
    user='user_yangll',
    password='vGxw9jWg')

neshieldConn = Connection.Mysql(
    host='192.168.5.23',
    port=3306,
    dbname='neshield',
    user='user_yangll',
    password='vGxw9jWg')

gpstestConn = Connection.Mysql(
    host='192.168.3.210',
    port=3308,
    dbname='gps',
    user='user_test',
    password='rewirew')

neshieldtestConn = Connection.Mysql(
    host='192.168.3.210',
    port=3308,
    dbname='neshield',
    user='user_test',
    password='rewirew')


def testDbComment(db):
    if db == 'gps':
        testConn = gpstestConn
        proConn = gpsConn
    else:
        testConn = neshieldtestConn
        proConn = neshieldConn

    arr01 = testDbTables(testConn, proConn, db)
    arr02 = testDbColumns(testConn, proConn, db)
    print('arr01', arr01)
    print('arr02', arr02)


def testDbTables(testConn, proConn, db):
    arr01 = []
    tablesTestDataList = testConn.ExecuteSql(
        f"SELECT * FROM `information_schema`.`TABLES` WHERE table_schema='{db}';")

    for tablesTestData in tablesTestDataList:
        print('tablesTestData===', tablesTestData)
        tablesData = proConn.ExecuteSql(
            f"SELECT * FROM `information_schema`.`TABLES` WHERE table_schema='{db}' and `table_name` ='{tablesTestData[2]}';")
        # print('tablesData', tablesData)
        print('tablesData[0]', tablesData[0])
        if (tablesData[0][0] != tablesTestData[0]
                or tablesData[0][1] != tablesTestData[1]
                or tablesData[0][2] != tablesTestData[2]
                or tablesData[0][3] != tablesTestData[3]
                or tablesData[0][4] != tablesTestData[4]
                or tablesData[0][5] != tablesTestData[5]
                or tablesData[0][6] != tablesTestData[6]
                # or tablesData[0][7] != tablesTestData[7]
                # or tablesData[0][8] != tablesTestData[8]
                # or tablesData[0][9] != tablesTestData[9]
                or tablesData[0][10] != tablesTestData[10]
                # or tablesData[0][11] != tablesTestData[11]
                # or tablesData[0][12] != tablesTestData[12]
                or tablesData[0][13] != tablesTestData[13]
                # or tablesData[0][14] != tablesTestData[14]
                # or tablesData[0][15] != tablesTestData[15]
                or tablesData[0][16] != tablesTestData[16]
                or tablesData[0][17] != tablesTestData[17]
                or tablesData[0][18] != tablesTestData[18]
                or tablesData[0][19] != tablesTestData[19]):
            arr01.append(tablesTestData[2])
            print('===========================================')
            writeFile('tablesData[0]' + str(tablesData[0]), str(db) + 'tables')
            writeFile('tablesTestData' + str(tablesTestData), str(db) + 'tables')
    return arr01


def testDbColumns(testConn, proConn, db):
    arr02 = []
    columnsTestDataList = testConn.ExecuteSql(
        f"SELECT * FROM `information_schema`.`COLUMNS` WHERE table_schema='{db}';")
    for columnsTestData in columnsTestDataList:
        print('columnsTestData', columnsTestData)
        columnsData = proConn.ExecuteSql(
            f"SELECT * FROM `information_schema`.`COLUMNS` WHERE table_schema='{db}' and `table_name` ='{columnsTestData[2]}' and `column_name` = '{columnsTestData[3]}';")
        print('columnsData[0]', columnsData[0])
        if (columnsData[0][0] != columnsTestData[0]
                or columnsData[0][1] != columnsTestData[1]
                or columnsData[0][2] != columnsTestData[2]
                or columnsData[0][3] != columnsTestData[3]
                or columnsData[0][4] != columnsTestData[4]
                or columnsData[0][5] != columnsTestData[5]
                or columnsData[0][6] != columnsTestData[6]
                # or columnsData[0][7] != columnsTestData[7]
                # or columnsData[0][8] != columnsTestData[8]
                # or columnsData[0][9] != columnsTestData[9]
                or columnsData[0][10] != columnsTestData[10]
                # or columnsData[0][11] != columnsTestData[11]
                or columnsData[0][12] != columnsTestData[12]
                or columnsData[0][13] != columnsTestData[13]
                # or columnsData[0][14] != columnsTestData[14]
                or columnsData[0][15] != columnsTestData[15]
                or columnsData[0][16] != columnsTestData[16]
                or columnsData[0][17] != columnsTestData[17]
                or columnsData[0][18] != columnsTestData[18]
                or columnsData[0][19] != columnsTestData[19]
                or columnsData[0][20] != columnsTestData[20]):
            arr02.append(columnsTestData[2])
            print('===========================================')
            writeFile('columnsData[0]' + str(columnsData[0]), str(db) + 'columns')
            writeFile('columnsTestData' + str(columnsTestData), str(db) + 'columns')
    return arr02


def writeFile(sql, fileName):
    with open("H:\\PythonWorkSpaces\\verifyMysqlData\\" + fileName + ".sql", "a+", encoding='utf-8') as fw:
        fw.write(sql.strip())
        fw.write("\n")


if __name__ == '__main__':
    testDbComment('gps')
    testDbComment('neshield')
