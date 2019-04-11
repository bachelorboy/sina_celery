import requests


cookie = {
        "Cookie": 'SCF=Ah_hPPeAWzsVcWNL_hXTKlsY02uyImln6rRA5SjNV56b_rHKl8Qlq2qoeioZKpC8l2B5u8aYfZlD5BXAbmPCGxM.; _T_WM=d918d57b34bd39c1a86baaa7bf0c0b13; SUB=_2A25xqfXzDeRhGeNI61EQ8y3PzD2IHXVTVZu7rDV6PUJbkdAKLWStkW1NSKGyUG1we8BlxQGpHWWUqjrQ0wrFdTCt; SUHB=0N21p2X-516E37',
    }
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://weibo.cn/u/1549364094?filter=1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'upgrade-insecure-requests': '1'
}
user_id = 1549364094
filter = 1


def get_content():

    url = "https://weibo.cn/u/%d?filter=%d&page=1" % (
        user_id, filter)
    html = requests.get(url, cookies=cookie, headers=headers).content
    return html


def get_page_content(page):
    url2 = "https://weibo.cn/u/%d?filter=%d&page=%d" % (
        user_id, filter, page)
    html2 = requests.get(url2, cookies=cookie, headers=headers).content
    return html2
