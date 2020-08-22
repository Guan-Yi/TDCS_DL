# TDCS_DL
下載交通資料庫 (http://tisvcloud.freeway.gov.tw/history/) M03~M08資料, 以小時為單位  
* M03A：各類車種通行量統計  
* M04A：站間各車種平均旅行時間  
* M05A：站間各車種平均行駛車速  
* M06A：各旅次路徑原始資料  
* M07A：各類車種旅次平均長度  
* M08A：各類車種旅次數量  

## Usage
```
$python	ETC_data_download.py <data_type> <year> <date> <start_hour> [end_hour]
```
### parameters
* `data_type`: M03A...M08A
* `year`: YYYY, ex: 2020
* `date`: MMDD, ex: 0801
* `start_hour`: 0 ~ 24
* `end_hour`: optional, if just need data in one hour.

## example:  
```
$python ETC_data_download.py M08A 2020 0801 12 15
```  