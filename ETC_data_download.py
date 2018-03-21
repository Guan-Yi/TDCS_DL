
import requests
import urllib.request
import os
import time
import sys

def create_url_1 (url, level_1):    
    temp = url + level_1 + '/'
    return temp

def create_url_2_1 (url, level_2):    
    temp = url + level_2 + '/'
    return temp

#end 
def create_url_2_2 (url, level_1, level_2):    
    temp = url + level_1 + '_' + level_2 + '.tar.gz'
    return temp

def create_url_3 (url, level_3):
    temp = url + level_3 + '/'
    return temp

def create_dl_url (url, t1, t2, t3, hs):
    temp_url = url + 'TDCS_' + t1 + '_' + t2 + '_' + t3 + hs + '.csv'
    temp_name = 'TDCS_' + t1 + '_' + t2 + '_' + t3 + hs + '.csv'
    return temp_url, temp_name

def main():
    url = 'http://tisvcloud.freeway.gov.tw/history/TDCS/'
    data_type = sys.argv[1]
    year = sys.argv[2]
    date = sys.argv[3]
    
    
    if len(sys.argv)>5:
        hour_1 = sys.argv[4]
        hour_2 = sys.argv[5]
        hour_diff = int(hour_2) - int(hour_1)
        hour = list(range(int(hour_1),int(hour_2)+1))
        for i in range(len(hour)):
            hour[i] = str(hour[i]).zfill(2)
    else:
        hour_1 = sys.argv[4]
    
    complete_date = year + date
        
    L1 = create_url_1(url, data_type)
    L2_1 = create_url_2_1(L1, complete_date)
    L2_2 = create_url_2_2(L1, data_type, complete_date)
    
    #hour
    L3 = create_url_3(L2_1, sys.argv[3])
    
    hs = list(range(0,5501,500))
    for i in range(len(hs)):
        hs[i] = str(hs[i]).zfill(4)
    
    try:
        if (hour_diff > 0):
            for i in range(len(hour)):
                L3 = create_url_3(L2_1, hour[i])
                for j in range(len(hs)):
                    temp_url = create_dl_url(L3, data_type, complete_date, hour[i], hs[j])
                    print (temp_url[0])
                    urllib.request.urlretrieve(temp_url[0], temp_url[1])
                    time.sleep(1)
        else:
            temp_hour =  str(hour_1).zfill(2)
            L3 = create_url_3(L2_1, temp_hour)
            for i in range(len(hs)):
                temp_url = create_dl_url(L3, data_type, complete_date, temp_hour, hs[i])
                print (temp_url[0])
                urllib.request.urlretrieve(temp_url[0], temp_url[1])
                time.sleep(1)
        
    except Exception:
        print ('something wrong! Q_Q')
        
        
    else:
        filename = L2_2.split("/")[-1]
        with open(filename, "wb") as f:
            r = requests.get(L2_2)
            f.write(r.content)
        print ('sucess!')
    
    return 

if __name__ == "__main__":
    if (sys.argv[1] == 'M03A'):
        print ('各類車種通行量統計')
    elif (sys.argv[1] == 'M04A'):
        print ('站間各車種平均旅行時間')
    elif (sys.argv[1] == 'M05A'):
        print ('站間各車種平均行駛車速')
    elif (sys.argv[1] == 'M06A'):
        print ('各旅次路徑原始資料')
    elif (sys.argv[1] == 'M07A'):
        print ('各類車種旅次平均長度')
    elif (sys.argv[1] == 'M08A'):
        print ('各類車種旅次數量')
    else:
        print ('???')
    if not os.path.exists('ETC'):
        os.makedirs('ETC')
    os.chdir('ETC')
    main()

