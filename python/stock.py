num = 2000
markets = ["10:00:00 2050", "10:04:00 1900", "10:04:59 1910", "10:18:50 1900", "10:19:55 2000", "10:25:55 1950", "12:39:35 1890", "15:29:59 2010"]

num2 = 2000
markets2 = ["10:00:00 2050", "10:04:00 2150", "10:05:00 2010", "10:10:00 2098", "15:29:59 1990"]

num3 = 2500
markets3 = ["10:00:00 2510", "10:10:25 2480", "14:49:00 2300", "14:50:10 2400", "15:19:32 2500"]

num = 2500
markets = ["10:00:00 2510", "10:10:25 2480", "14:48:55 2300", "14:50:10 2400", "15:19:32 2500"]


start_time_str ='10:00:00' # 수정 - !
trigger = False

for i in markets:
    start_time_hms = list(map(int, start_time_str.split(':')))  # 수정 - !
    temp_time_hms = list(map(int, i.split(' ')[0].split(':')))  # 수정 - !

    if(int(i.split(':')[0])>=14 and int(i.split(':')[1])>= 50): # 마감 40분전
        if(int(start_time_str.split(':')[0])<=14 and int(start_time_str.split(':')[1])<=48 and trigger is True):      # 수정 - !
            result = '{0}:{1:02d}:{2}'.format(start_time_str.split(':')[0], start_time_hms[1] + 1, start_time_str.split(':')[2])    # 수정 - !
            break
        else:
            result = "not activated"
            break
    if trigger is False:
        if not (num-(num/100*5) < int(i.split(' ')[1]) < num+(num/100*5)): # 사이드카 발동 조건 1
            start_time_str = i.split(' ')[0]    # 시간저장
            trigger = True                  # 조건 1 성립
            # print('triger on ', start_time_str)

    else:
        # 수정 - !
        # print('temp time ', i.split(' ')[0])
        if (temp_time_hms[0] > start_time_hms[0]):          # 1시간 이상차이 > 발동
            # print('1 hour ')
            result = '{0}:{1:02d}:{2}'.format(start_time_str.split(':')[0], start_time_hms[1] + 1, start_time_str.split(':')[2]) # 수정 - !
            break
        elif temp_time_hms[1] > start_time_hms[1]+1:        # 2분 이상 차이 > 발동
            # print('2 minute')
            result = '{0}:{1:02d}:{2}'.format(start_time_str.split(':')[0], start_time_hms[1] + 1, start_time_str.split(':')[2])    # 수정 - !
            break
        elif temp_time_hms[1] == start_time_hms[1]+1:       # 1분
            # print('1 minute - 1')
            if temp_time_hms[2] >= start_time_hms[2]:       # 초
                # print('1 minute OK')
                result = '{0}:{1:02d}:{2}'.format(start_time_str.split(':')[0], start_time_hms[1] + 1, start_time_str.split(':')[2])    # 수정 - !
                break
            elif (num-(num/100*5) < int(i.split(' ')[1]) < num+(num/100*5)): # 1분 이내에 등락률 미만
                trigger = False # 트리거 off
                # print('1 분이내 등락률 미만 트리거 off', i.split(' ')[0])

        else:   # 1분 이전에
            # print('1 minute NO')
            # print(num-(num/100*5),  int(i.split(' ')[1]) , num+(num/100*5))
            if (num-(num/100*5) < int(i.split(' ')[1]) < num+(num/100*5)):
                # print('trigger off')
                trigger = False

print(result)