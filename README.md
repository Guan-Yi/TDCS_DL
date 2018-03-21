# TDCS_DL
下載交通資料庫 (http://tisvcloud.freeway.gov.tw/history/) M03~M08資料, 以小時為單位

# Usage

```
$python  ETC_data_download.py  <data type>  <year>  <date> <start_hour> <end_hour>
```

### example:  
```
$python  ETC_data_download.py  M08  2018  0315  7   9
```  

warnings: It must have <start_hour> and <end_hour> arguments, because there are some bugs still exist in this script.
