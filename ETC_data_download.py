
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
    L1 = create_url_1(url, sys.argv[1])
    L2_1 = create_url_2_1(L1, sys.argv[2])
    L2_2 = create_url_2_2(L1, sys.argv[1], sys.argv[2])
    L3 = create_url_3(L2_1, sys.argv[3])
    
    print (L1)
    print (L2_1)
    print (L2_2)
    print (L3)
    
    hs = list(range(0,5501,500))
    for i in range(len(hs)):
        hs[i] = str(hs[i]).zfill(4)
    
    try:
        for i in range(len(hs)):
            temp_url = create_dl_url(L3, sys.argv[1], sys.argv[2], sys.argv[3], hs[i])
            print (temp_url[0])
            urllib.request.urlretrieve(temp_url[0], temp_url[1])
            time.sleep(1)
        
        filename = L2_2.split("/")[-1]
        with open(filename, "wb") as f:
            r = requests.get(L2_2)
            f.write(r.content)
        print ('sucess!')
        
    except:
        print ('no file')
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

