import connectiontool.connection as Connection

mysql = Connection.Mysql(
    host='192.168.5.22',
    port=3307,
    dbname='gps',
    user='user_yangll',
    password='vGxw9jWg')

if __name__ == '__main__':
    sql01 = '''
    SELECT t.trackerId                                                   as id,
       w.shopName                                                    as shopName,
       w.shopContacts,
       w.contactsPhone,
       w.sqbh                                                        as workOrderNo,
       v.name                                                        as name,
       v.standno                                                     as standNo,
       t.sn                                                          as sn,
       date_format(v.buyDate, '%Y-%m-%d %T')                         as activeDate,
       u.userRemark                                                  as operator,
       l.lastRtTrack                                                 as lastRtTrack,
       l.lastGprsTime                                                as lastGprsTime,
       l.speed                                                       as speed,
       t.source                                                      as source,
       (CASE t.source WHEN 1 THEN '有线' WHEN 0 THEN '无线' ELSE '' END) AS sourceType,
       vd.car_remark                                                 as carRemarkType,
       vd.car_used_type                                              as carUsedType,
       vd.car_used                                                   as carUsed,
       (SELECT temp.status FROM d_device_freq temp where temp.vehicle_id = v.vehicleId and temp.sn = t.sn order by temp.create_time desc limit 1) AS freqStatus,
       v.vehicleId,
       dvr.vehicle_icon                                              as vehicleIcon,
       dvr.user_remark                                               as userRemark
from d_track_info t
         LEFT OUTER JOIN d_vehicle v ON v.vehicleId = t.vehicleId
         LEFT OUTER JOIN d_vehicle_remark dvr on dvr.vehicle_id = v.vehicleId
         LEFT OUTER JOIN d_vehicle_workorder w ON v.workOrderId = w.workOrderId
         LEFT OUTER JOIN d_class c ON v.classId = c.classid
         LEFT OUTER JOIN d_user u ON v.lastLoginUserId = u.d_LoginUserId
         LEFT OUTER JOIN d_device_login l ON t.sn = l.sn
         LEFT OUTER JOIN d_vehicle_detail vd ON vd.standno = v.standno
WHERE t.isActive = 1
  and t.vehicleId is not null
  and v.status = 0
order by t.vehicleId desc
    '''
    dataList = mysql.ExecuteSql(sql01)
    print("dataList===", dataList)

    arr = []
    for data in dataList:
        print(data[17])
        print(data[7])
        freqStatus = mysql.ExecuteSql('''
        select status from d_device_freq where sn = %s order by create_time desc limit 1;
        ''', data[7])
        print(freqStatus)

        if freqStatus:
            if freqStatus[0]:
                print('freqStatus===', freqStatus[0][0])
                if freqStatus[0][0] != data[17]:
                    arr.append(data[7])

    print(arr)
