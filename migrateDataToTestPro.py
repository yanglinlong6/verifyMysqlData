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
        tables = 'TABLES_YANG_TIGER'
        columns = 'COLUMNS_YANG_TIGER'
    else:
        testConn = neshieldtestConn
        proConn = neshieldConn
        tables = 'TABLES_YANG_NESHIELD'
        columns = 'COLUMNS_YANG_NESHIELD'

    # arr01 = testMigrateTables(testConn, proConn, db, tables)
    arr02 = testMigrateColumns(testConn, proConn, db, columns)
    # print('arr01', arr01)
    print('arr02', arr02)


def testMigrateTables(testConn, proConn, db, tables):
    sql = f'''
     SELECT * FROM `information_schema`.`TABLES` WHERE table_schema='{db}' AND table_comment='' ;
     '''
    tablesDataList = proConn.ExecuteSql(sql)
    arr01 = []
    for tablesData in tablesDataList:
        print('tablesData===', tablesData)
        sql01 = f'''
        SELECT * FROM `{tables}` WHERE table_schema='{db}' and `table_name` ='{tablesData[2]}'
        '''
        tablesTestData = testConn.ExecuteSql(sql01)
        print('tablesTestData[0]===', tablesTestData[0])
        if (tablesTestData[0][0] != tablesData[0]
                or tablesTestData[0][1] != tablesData[1]
                or tablesTestData[0][2] != tablesData[2]
                or tablesTestData[0][3] != tablesData[3]
                or tablesTestData[0][4] != tablesData[4]
                or tablesTestData[0][5] != tablesData[5]
                or tablesTestData[0][6] != tablesData[6]
                # or tablesTestData[0][7] != tablesData[7]
                # or tablesTestData[0][8] != tablesData[8]
                # or tablesTestData[0][9] != tablesData[9]
                # or tablesTestData[0][10] != tablesData[10]
                # or tablesTestData[0][11] != tablesData[11]
                # or tablesTestData[0][12] != tablesData[12]
                # or tablesTestData[0][13] != tablesData[13]
                # or tablesTestData[0][14] != tablesData[14]
                # or tablesTestData[0][15] != tablesData[15]
                or tablesTestData[0][16] != tablesData[16]
                or tablesTestData[0][17] != tablesData[17]
                or tablesTestData[0][18] != tablesData[18]
                or tablesTestData[0][19] != tablesData[19]
                or tablesTestData[0][20] != tablesData[20]):
            arr01.append(tablesData[2])
            print('===========================================')
    return arr01


def testMigrateColumns(testConn, proConn, db, columns):
    sql = f'''
    SELECT * FROM `information_schema`.`COLUMNS` WHERE table_schema='{db}' AND column_comment='';
    '''
    columnsDataList = proConn.ExecuteSql(sql)
    arr02 = []
    for columnsData in columnsDataList:
        print('columnsData', columnsData)
        sql01 = f'''
        SELECT * FROM `{columns}` WHERE table_schema='{db}' and `table_name` ='{columnsData[2]}' and `column_name` = '{columnsData[3]}';
        '''
        columnsTestData = testConn.ExecuteSql(sql01)
        print('columnsTestData[0]===', columnsTestData[0])
        if (columnsTestData[0][0] != columnsData[0]
                or columnsTestData[0][1] != columnsData[1]
                or columnsTestData[0][2] != columnsData[2]
                or columnsTestData[0][3] != columnsData[3]
                or columnsTestData[0][4] != columnsData[4]
                or columnsTestData[0][5] != columnsData[5]
                or columnsTestData[0][6] != columnsData[6]
                or columnsTestData[0][7] != columnsData[7]
                or columnsTestData[0][8] != columnsData[8]
                or columnsTestData[0][9] != columnsData[9]
                or columnsTestData[0][10] != columnsData[10]
                or columnsTestData[0][11] != columnsData[11]
                or columnsTestData[0][12] != columnsData[12]
                or columnsTestData[0][13] != columnsData[13]
                or columnsTestData[0][14] != columnsData[14]
                or columnsTestData[0][15] != columnsData[15]
                or columnsTestData[0][16] != columnsData[16]
                or columnsTestData[0][17] != columnsData[17]
                or columnsTestData[0][18] != columnsData[18]
                or columnsTestData[0][19] != columnsData[19]
                or columnsTestData[0][20] != columnsData[20]):
            arr02.append(columnsData[2])
            print('===========================================')
    return arr02


def writeFile(sql, fileName):
    with open("H:\\PythonWorkSpaces\\verifyMysqlData\\" + fileName + ".sql", "a+", encoding='utf-8') as fw:
        fw.write(sql.strip())
        fw.write("\n")


def filterData(data):
    if data is None:
        data = ""
    return data


if __name__ == '__main__':
    testDbComment('gps')
    testDbComment('neshield')
