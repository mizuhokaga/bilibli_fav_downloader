import time
import random
import requests

import conf
from utils import convertor
from utils.decorator import timing_decorator


@timing_decorator
def download_list(bv_id_list: list):
    total_cnt = 0
    for item in bv_id_list:
        total_cnt = total_cnt + wrap_download(item)
        # 暂停程序执行，模拟等待随机秒数的操作
        # time.sleep(random.randint(1, 5))
    print(f"预计下载的视频总数：{str(len(bv_id_list))} ,实际下载的视频总数：{total_cnt}")


def wrap_download(video_id: str) -> int:
    cnt = 0
    # 获取cid
    base_url = 'https://api.bilibili.com/x/web-interface/view'
    aid = convertor.bv2av(video_id) if video_id.startswith("BV") else video_id
    # 请求头添加Referer验证防盗链,否则403
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Origin": "https://www.bilibili.com",
        "Connection": "keep-alive",
        "Range": "bytes=0-",
        "Referer": "https://www.bilibili.com/video/{video_id}".format(video_id=aid),
        "Cookie": conf.COOKIE
    }
    r = requests.get(f'{base_url}?aid={aid}', headers=headers, )
    result = r.json()
    if result['code'] == 0:
        # pages 视频分P对象数组
        pages = result['data']['pages']
        for page in pages:
            cnt = cnt + download(aid, page['cid'], video_id, page['part'], headers)
    # 只要视频合集中存在一个视频下载成功,就认为该page对象下载成功
    if cnt > 0:
        cnt = 1
    else:
        cnt = 0
    return cnt


def download(aid, cid, video_id, filename, headers) -> int:
    """
    根据aid和cid下载指定视频
    """
    # 依据API获取视频流地址
    cnt = 0
    print(f"开始下载视频：av{aid}({video_id})-{filename}", )
    # 开始下载时刻
    start_time = time.time()
    url = 'https://api.bilibili.com/x/player/wbi/playurl?avid={}&cid={}&qn={}&fnval=1'.format(aid, cid, 80)
    r = requests.get(url, headers=headers)
    result = r.json()
    if result['code'] == 0:
        # 真正的视频流地址
        video_url = result['data']['durl'][0]['url']
        # 视频格式,json示例: "format": "mp4720",
        # format = result['data']['format']
        # local_filename = f'{filename}_{format}.mp4'
        local_filename = f'{filename}.mp4'
        # 仍然需要判断是否防盗链,需要带上请求头
        # TODO: 现在是单线程下载,后续改进
        with requests.get(video_url, headers=headers, stream=True) as response:
            with open(local_filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
        # 计算用时
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"下载视频 av{aid}({video_id})-{filename} 成功,该次下载用时：{elapsed_time:.2f}秒")
        cnt = cnt + 1
    else:
        print("获取视频下载地址出错!")
    return cnt;
