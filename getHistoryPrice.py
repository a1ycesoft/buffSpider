import random
from time import sleep
import requests
import pymysql
import time

id='34125'
cookie = 'usertrack=ezq0ZWKsG1GyjEziAzmmAg==; _ga=GA1.2.1001611246.1655446357; _ntes_nnid=99f5ee40a46a472a2c4a93fded95df4a,1659243089843; _ntes_nuid=99f5ee40a46a472a2c4a93fded95df4a; nts_mail_user=scorpionsr@163.com:-1:1; NTES_CMT_USER_INFO=311889195|有态度网友0iBMQH|http://cms-bucket.nosdn.127.net/2018/08/13/078ea9f65d954410b62a52ac773875a1.jpeg|false|c2NvcnBpb25zckAxNjMuY29t; NTES_P_UTID=Fom60K0chjev3krdJlDTOkwSmHwI8iyp|1660802061; __bid_n=183b352b6bf7a59bfe4207; Device-Id=8HiQ13R0C4Wf2PDX48Qa; wyy_uid=2b9097c6-4bff-4c27-a9bf-6ececa634dac; channel="h=media&t=media&from=nim|https://netease.im/sms&clueFrom=nim&referrer=https://app.yunxin.163.com"; clueFrom=nim; hb_MA-91DF-2127272A00D5_source=netease.im; _gcl_au=1.1.1526887673.1678018910; hb_MA-91B4-D595CA25136C_source=netease.im; P_INFO=18981054145|1678019526|1|netease_buff|00&99|null&null&null#hlj&231100#10#0|&0||18981054145; remember_me=U1101178558|HwpXromBBhoaqrsLrOMLwmOL8AANxh8s; session=1-ZHDGVTNmQ-cGIZDJYIJTg1aSoiODTtr4tFxA1JjtkhhN2037135846; Locale-Supported=zh-Hans; game=csgo; csrf_token=ImI3MDM5YWE5OTBlMTY5MzE5MzBjNzMwMTE2YTMzOWRiMjk3MDIwMjIi.FucEgA.KaMrQ_qMQ4nyFnirH1g_YS26x24'.encode(
    "utf-8")
header = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
def getHistoryById():
    now = int(time.time() * 1000)
    url = 'https://buff.163.com/api/market/goods/price_history/buff?game=csgo&goods_id={}&currency=CNY&_={}'.format(id,now)
    res = requests.get(url, headers=header)
    arr = res.json()['data']['price_history']
    for i in arr:
        dao(i[0],i[1])

def dao(time,price):
    mysql_conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='173371292', db='csgo')
    sql = "INSERT INTO history (time, price, goods_id) VALUES ('{0}','{1}','{2}')".format(time,price,id)
    print(sql)
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(sql)
        mysql_conn.commit()
    except Exception as e:
        mysql_conn.rollback()
    mysql_conn.close()

if __name__ == '__main__':
    getHistoryById()


