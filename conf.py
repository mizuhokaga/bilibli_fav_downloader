import os

# 程序根目录
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# 本地存储目录
OUTPUT_PATH = os.path.join(BASE_PATH, "output")

# B站登录后获取的SESSDATA
# 需要定期更换COOKIE的值即可
COOKIE = (
    "buvid3=D3C1CE41-A44A-F15C-F99A-D2441BF598B995551infoc; b_nut=1672134695; i-wanna-go-back=-1; b_ut=5; buvid4=B2335D8E-0581-5025-9FEE-B286B2B1C30E13640-022120621-NJ%2FXfX%2FKz2H3XyTfcmi3Ew%3D%3D; "
    "SESSDATA=; "
    "bili_jct=22ab5efe154ef28512d802352bbd4856; "
    "DedeUserID=5032560; DedeUserID__ckMd5=a09a29c587036373; CURRENT_FNVAL=4048; rpdid=|(u~J)|RJlYu0J'uY~kuJR~)|; LIVE_BUVID=AUTO4716721356405858; hit-new-style-dyn=1; hit-dyn-v2=1; nostalgia_conf=-1; fingerprint=5d8be3bb1fb8700f854f1ee13d5466c9; buvid_fp=5d8be3bb1fb8700f854f1ee13d5466c9; buvid_fp_plain=undefined; CURRENT_QUALITY=64; CURRENT_BLACKGAP=0; _uuid=54AA710CF-5831-27C9-98EC-2D613619475571966infoc; is-2022-channel=1; header_theme_version=CLOSE; home_feed_column=5; PVID=1; CURRENT_PID=5aaa6380-d1e7-11ed-b829-e1c1e0d05ead; FEED_LIVE_VERSION=V8; browser_resolution=1621-890; bp_t_offset_5032560=878295123854622768; enable_web_push=DISABLE; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDM0MzM4MzAsImlhdCI6MTcwMzE3NDU3MCwicGx0IjotMX0.A78tn7bq6Pcewd0IvkI9qia5XdZpSt4jP1kw8OhS3Cg; bili_ticket_expires=1703433770; sid=8j1xl58i; b_lsid=E9C710D2D_18C9A2DA6F2; bsource=search_baidu"
)
