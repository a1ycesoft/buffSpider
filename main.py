from time import sleep
import requests
import pymysql
import time
knifeList = ["weapon_knife_survival_bowie",
             "weapon_knife_butterfly",
             "weapon_knife_falchion",
             "weapon_knife_flip",
             "weapon_knife_gut",
             "weapon_knife_tactical",
             "weapon_knife_m9_bayonet",
             "weapon_bayonet",
             "weapon_knife_karambit",
             "weapon_knife_push",
             "weapon_knife_stiletto",
             "weapon_knife_ursus",
             "weapon_knife_gypsy_jackknife",
             "weapon_knife_widowmaker",
             "weapon_knife_css",
             "weapon_knife_cord",
             "weapon_knife_canis",
             "weapon_knife_outdoor",
             "weapon_knife_skeleton"]
handgunList = ["weapon_hkp2000",
               "weapon_usp_silencer",
               "weapon_glock",
               "weapon_p250",
               "weapon_fiveseven",
               "weapon_cz75a",
               "weapon_tec9",
               "weapon_revolver",
               "weapon_deagle",
               "weapon_elite"]
machinegunList=["weapon_m249","weapon_negev"]
shotgunList=["weapon_sawedoff","weapon_xm1014","weapon_nova","weapon_mag7"]
smgList=["weapon_p90","weapon_mac10","weapon_ump45","weapon_mp7","weapon_bizon","weapon_mp9","weapon_mp5sd"]
rifleList=["weapon_galilar","weapon_scar20","weapon_awp","weapon_ak47","weapon_famas","weapon_m4a1","weapon_m4a1_silencer","weapon_sg556","weapon_ssg08","weapon_aug","weapon_g3sg1"]

# 在这里填cookie
cookie = ''.encode("utf-8")


def dao(id,fullname,shortname,icon,sellminprice,bmp,steamprice,steampricecny,ext,ql,rar,tp,steam):
    print(id,fullname)
    # 填你的数据库信息
    mysql_conn = pymysql.connect(host='127.0.0.1', port=3306, user='', password='',db='csgo')
    sql = "INSERT INTO goods (id, full_name, short_name, icon_src, sell_min_price, buy_max_price, steam_price, steam_price_cny,steam_url,exterior,rarity,quality,type) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(id,fullname,shortname,icon,sellminprice,bmp,steamprice,steampricecny,steam,ext,rar,ql,tp)
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(sql)
        mysql_conn.commit()
    except Exception as e:
        mysql_conn.rollback()
    mysql_conn.close()

def getPageSize(category):
    url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=1&category={}'.format(category)
    header = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=header)
    ans = res.json()['data']['total_page']
    return ans

def getData(page,category):
    url = 'https://buff.163.com/api/market/goods?game=csgo&page_num={}&category={}'.format(page,category)
    header = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    res=requests.get(url,headers=header)
    arr=res.json()['data']['items']
    for x in arr:
        bmp=x['buy_max_price']
        icon=x['goods_info']['icon_url']
        ext=x['goods_info']['info']['tags']['exterior']['localized_name']
        ql=x['goods_info']['info']['tags']['quality']['internal_name']
        rar=x['goods_info']['info']['tags']['rarity']['localized_name']
        tp=x['goods_info']['info']['tags']['weapon']['internal_name']
        id=x['id']
        sellminprice=x['sell_min_price']
        fullname=x['name']
        shortname=x['short_name']
        steam=x['steam_market_url']
        steamprice=x['goods_info']['steam_price']
        steampricecny=x['goods_info']['steam_price_cny']
        dao(id,fullname,shortname,icon,sellminprice,bmp,steamprice,steampricecny,ext,ql,rar,tp,steam)

def getAllData(arr):
    for x in arr:
        cnt=getPageSize(x)
        sleep(2)
        for i in range(1,cnt+1):
            getData(i,x)
            sleep(2)


if __name__ == '__main__':
    start = time.time()
    # getAllData(knifeList)
    # getAllData(rifleList)
    # getAllData(handgunList)
    # getAllData(smgList)
    # getAllData(shotgunList)
    # getAllData(machinegunList)
    end = time.time()
    print('用时:',end-start,'s')




