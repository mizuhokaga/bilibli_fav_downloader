import json

import requests

from utils.downloader import download_list


def get_specific_public_fav_list(fav_id, page_num=1, page_size=20) -> list:
    """
    获取指定文件夹下所有视频的bv号
    """
    url = 'https://api.bilibili.com/x/v3/fav/resource/list'
    payload = {'media_id': fav_id, 'pn': page_num, 'ps': page_size}  # ps每页数量最大为20
    r = requests.get(url, payload)
    result = r.json()
    # print(json.dumps(result))
    if result['code'] == -403 or result['data'] is None:
        print(result)
    else:
        data = result['data']
        bv_id_list = []
        for media in data['medias']:
            bv_id_list.append(media['bv_id'])
        if data['has_more']:
            get_specific_public_fav_list(page_num + 1)
    print(f"已抓取到 收藏夹 fid-{fid} : [{data['info']['title']}] 的 {str(len(bv_id_list))} 个视频")
    return bv_id_list


if __name__ == '__main__':
    fid = 2797980160
    bv_id_list = get_specific_public_fav_list(fid)
    download_list(bv_id_list)
