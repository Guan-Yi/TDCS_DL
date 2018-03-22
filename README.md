# TDCS_DL
下載交通資料庫 (http://tisvcloud.freeway.gov.tw/history/) M03~M08資料, 以小時為單位  
* M03A：各類車種通行量統計  
* M04A：站間各車種平均旅行時間  
* M05A：站間各車種平均行駛車速  
* M06A：各旅次路徑原始資料  
* M07A：各類車種旅次平均長度  
* M08A：各類車種旅次數量  

# Usage
```
$python	ETC_data_download.py  <data type>  <year>  <date>  <start_hour>  <end_hour>
```
#### example:  
```
$python  ETC_data_download.py  M08  2018  0315  7   9
```  
 note: if you just want one hour data, you can skip the <end_hour>.

