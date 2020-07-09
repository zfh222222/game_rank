
import requests,os
import json
from lxml import etree
import uuid




headers={
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Cookie": "__mta=154449415.1592961736137.1592963643536.1594033300747.8; _lxsdk_cuid=172e3ea8381c8-0d15e7d6db21c1-581b3318-1fa400-172e3ea8381c8; ci=1; rvct=1; _hc.v=4fbc1954-c81e-1c36-1347-07446566c80c.1592961741; uuid=cd458a44ab734df1b840.1594027900.1.0.0; PHPSESSID=t5gdqmdhur0ac7hddu3riqf1e7; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1594027885; Hm_lpvt_f66b37722f586a240d4621318a5a6ebe=1594027885; __utma=211559370.1954729847.1594027885.1594027885.1594027885.1; __utmc=211559370; __utmz=211559370.1594027885.1.1.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=44277403.1592963639322.1594027906327.1594028365167.5; _lxsdk_s=17323c9defd-29c-972-739%7C%7C5"
}

jjj=(requests.get("https://bj.meituan.com/s/%E7%BD%97%E6%A3%AE/",headers=headers).text)
print(jjj)
#results=json.loads(jjj,encoding="utf8")
s=etree.HTML(jjj)
store_list=s.xpath("//div[@class='common-list-main']/div")
print(store_list)
for i in range(len(store_list)):

    print(s.xpath("//div[@class='common-list-main']/div[%s]//a/@href"%(i+1)))
    print(s.xpath("//div[@class='common-list-main']/div[%s]//a/@data-lab"%(i+1)))

#print("total:",results["total"])
#print("sql:",results["rows"][0]["stmt"])
#for i in range(results["total"]):
 #   print("server_address:",results["rows"][i]["server_address"])