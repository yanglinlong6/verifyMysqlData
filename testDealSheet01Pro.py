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

    arr01 = testDbTables(testConn, proConn, db, tables)
    arr02 = testDbColumns(testConn, proConn, db, columns)
    print('arr01', arr01)
    print('arr02', arr02)


def testDbTables(testConn, proConn, db, tables):
    arr01 = []
    tablesDataList = testConn.ExecuteSql(
        f"SELECT * FROM `{tables}` WHERE table_schema='{db}' AND table_comment='' ;")

    for tablesData in tablesDataList:
        print('tablesData===', tablesData)
        tablesTestData = proConn.ExecuteSql(
            f"SELECT * FROM `information_schema`.`TABLES` WHERE table_schema='{db}' and `table_name` ='{tablesData[2]}';")
        # print('tablesData', tablesData)
        print('tablesTestData[0]', tablesTestData[0])
        print('tablesTestData[0][0]', tablesTestData[0][0])
        print('tablesTestData[0][17]', tablesTestData[0][17])
        print('tablesTestData[0][18]', tablesTestData[0][18])
        '''
        tablesTestData[0]('def', 'gps', 'd_app_image', 'BASE TABLE', 'InnoDB', 10, 'Dynamic', 0, 0, 16384, 0, 32768, 0, 1502236, datetime.datetime(2022, 10, 21, 18, 32, 2), None, None, 'utf8_general_ci', None, '', '应用图片')
        tablesData       ('def', 'gps', 'd_app_image', 'BASE TABLE', 'InnoDB', 10, 'Dynamic', 1409245, 219, 309100544, 0, 93569024, 6291456, 1502271, datetime.datetime(2022, 6, 24, 18, 51, 27), datetime.datetime(2022, 10, 22, 10, 18, 21), None, 'utf8_general_ci', None, '', '')
        '''
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
                # or tablesTestData[0][14] != tablesTestData[14]
                # or tablesTestData[0][15] != tablesData[15]
                or tablesTestData[0][16] != tablesData[16]
                or tablesTestData[0][17] != tablesData[17]
                or tablesTestData[0][18] != tablesData[18]
                or tablesTestData[0][19] != tablesData[19]):
            arr01.append(tablesData[2])
            print('===========================================')
            tablesTestDataLog = tablesTestData[0][:7] + tablesTestData[0][16:20]
            writeFile('tablesTestData:' + str(tablesTestDataLog), 'fail' + str(db) + 'tables')
            tablesProDataLog = tablesData[:7] + tablesData[16:20]
            writeFile('tablesProData :' + str(tablesProDataLog), 'fail' + str(db) + 'tables')
        else:
            tablesTestDataLog = tablesTestData[0][:7] + tablesTestData[0][16:20]
            writeFile('tablesTestData:' + str(tablesTestDataLog), 'pass' + str(db) + 'tables')
            tablesProDataLog = tablesData[:7] + tablesData[16:20]
            writeFile('tablesProData :' + str(tablesProDataLog), 'pass' + str(db) + 'tables')
    return arr01


def testDbColumns(testConn, proConn, db, columns):
    arr02 = []
    columnsDataList = testConn.ExecuteSql(
        f"SELECT * FROM `{columns}` WHERE table_schema='{db}' AND column_comment='';")
    for columnsData in columnsDataList:
        print('columnsData', columnsData)
        columnsTestData = proConn.ExecuteSql(
            f"SELECT * FROM `information_schema`.`COLUMNS` WHERE table_schema='{db}' and `table_name` ='{columnsData[2]}' and `column_name` = '{columnsData[3]}';")
        print('columnsTestData[0]', columnsTestData[0])
        print('columnsTestData[0][0]', columnsTestData[0][0])
        print('columnsTestData[0][18]', columnsTestData[0][18])
        print('columnsTestData[0][19]', columnsTestData[0][19])
        '''
        columnsTestData[0]('def', 'gps', 'd_daoqiang_mileage_stat', 'vehicleId', 8, None, 'YES', 'varchar', 32, 96, None, None, None, 'utf8', 'utf8_general_ci', 'varchar(32)', '', '', 'select,insert,update,references', '车辆编号', '')
        columnsData       ('def', 'gps', 'd_daoqiang_mileage_stat', 'vehicleId', 8, '', 'YES', 'varchar', 32, 96, None, None, None, 'utf8', 'utf8_general_ci', 'varchar(32)', '', '', 'select', '', '')
        '''
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
                # or columnsTestData[0][18] != columnsTestData[18]
                # or columnsTestData[0][19] != columnsTestData[19]
                or columnsTestData[0][20] != columnsData[20]):
            arr02.append(columnsData[2])
            print('===========================================')
            columnsTestDataLog = columnsTestData[0][:18] + columnsTestData[0][20:]
            writeFile('columnsTestData:' + str(columnsTestDataLog), 'fail' + str(db) + 'columns')
            columnsProDataLog = columnsData[:18] + columnsData[20:]
            writeFile('columnsProData :' + str(columnsProDataLog), str(db) + 'columns')
        else:
            columnsTestDataLog = columnsTestData[0][:18] + columnsTestData[0][20:]
            writeFile('columnsTestData:' + str(columnsTestDataLog), 'pass' + str(db) + 'columns')
            columnsProDataLog = columnsData[:18] + columnsData[20:]
            writeFile('columnsProData :' + str(columnsProDataLog), 'pass' + str(db) + 'columns')
    return arr02


def writeFile(sql, fileName):
    # with open("H:\\PythonWorkSpaces\\verifyMysqlData\\" + fileName + ".sql", "a+", encoding='utf-8') as fw:
    #     fw.write(sql.strip())
    #     fw.write("\n")
    pass


if __name__ == '__main__':
    testDbComment('gps')
    testDbComment('neshield')
