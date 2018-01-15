关于 python 中操作 excel 的事项  
=  

1. 在使用 xlwt 库写入 datetime 或者 YYYY-MM-DD 形式, 在 excel 中则出现为  
   浮点数.  

   解决:  

   * 在写入数据的时候加入日期的格式  

            dateFormat = xlwt.XFStyle()
            # 或者是 yyyy-mm-dd
            dateFormat.num_format_str = 'yyyy/mm/dd'
            worksheet.write(0, 0, datetime.now(), dateFormat)
            workbook.save('test.xls')