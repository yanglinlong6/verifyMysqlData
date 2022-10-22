import connectiontool.connection as Connection

mysql = Connection.Mysql(
    host='192.168.5.23',
    port=3306,
    dbname='neshield',
    user='user_yangll',
    password='vGxw9jWg')

if __name__ == '__main__':
    sql01 = '''
    select tv.id,
       tvd.id                                                                                                                             vdId,
       tv.workorder_id                                                                                                                    workOrderId,
       tw.partner_order_no                                                                                                                bizOrderNo,
       tv.owner_name                                                                                                                      ownerName,
       tv.vin,
       tvd.sn,
       td.source                                                                                                                          deviceType,
       case when td.source = 1 then '有线' when td.source = 0 then '无线' else '--' end as                                                deviceTypeStr,
       case
           when tv.type_id is null then tv.model_name
           else
               concat(tv.sub_brand_name, '/', tv.series_name, '/', tv.type_name) end                                                      modelName,
       tv.vehicle_type                                                                                                                    vehicleType,
       tv.vehicle_usages                                                                                                                  vehicleUsages,
       tv.settle_flag                                                                                                                     settleFlag,
       tv.created_date                                                                                                                    activateTime,
       tv.created_by                                                                                                                      createdBy,
       (SELECT temp.status FROM t_device_freq temp where temp.vehicle_id = tv.id and temp.sn = tvd.sn order by created_date desc limit 1) freqStatus
from t_vehicle tv
         left join t_vehicle_device tvd on tvd.vehicle_id = tv.id
         left join t_workorder tw on tw.id = tv.workorder_id
         left join t_device td on td.sn = tvd.sn
         left join t_device_location tdl on tdl.sn = tvd.sn
         left join t_user tu on tu.id = tv.created_by
where tv.del_flag = 0
  and tvd.bind_status = 1
  and tvd.del_flag = 0
  # and tvd.sn like '%45205071206%';
  # and tvd.sn like '%42106290022%';
    '''
    dataList = mysql.ExecuteSql(sql01)
    print("dataList===", dataList)

    arr = []
    for data in dataList:
        print(data[15])
        print(data[6])
        freqStatus = mysql.ExecuteSql('''
        select status from t_device_freq where sn = %s order by created_date desc limit 1;
        ''', data[6])
        print(freqStatus)

        if freqStatus:
            if freqStatus[0]:
                print('freqStatus===', freqStatus[0][0])
                if freqStatus[0][0] != data[15]:
                    arr.append(data[6])

    print(arr)
