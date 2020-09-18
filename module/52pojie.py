import requests
import re
import os


def pojie():
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cookie": os.environ['POJIECOOKIE']  # 我的cookie
    }

    CHECK_IN_NOT_COMPLETED = r"https://www.52pojie.cn/static/image/common/qds.png"

    CHECK_IN_COMPLETED = r"https://www.52pojie.cn/static/image/common/wbs.png"

    pre_resp = requests.get(url="https://www.52pojie.cn", headers=HEADERS)
    pre_result_a = re.findall(CHECK_IN_COMPLETED, pre_resp.text)

    if len(pre_result_a) == 1:
        exit("重复签到")

    pre_result_b = re.findall(CHECK_IN_NOT_COMPLETED, pre_resp.text)

    resp_a = requests.get(url="https://www.52pojie.cn/home.php?mod=task&do=apply&id=2", headers=HEADERS)
    resp_b = requests.get(url="https://www.52pojie.cn/home.php?mod=task&do=draw&id=2", headers=HEADERS)

    resp_c = requests.get(url="https://www.52pojie.cn", headers=HEADERS)

    result = re.findall(CHECK_IN_COMPLETED, resp_c.text)

    if len(pre_result_b) == 1 and len(result) == 1:
        exit("签到成功")
    else:
        exit("签到异常")


if __name__ == '__main__':
    pojie()