import time
from datetime import datetime
from mastodon import Mastodon

mastodon = Mastodon(
        access_token = 'hMwdnStMNhPwiZ7Z4OUzhmvHLmm8J7Z_t0jCbp9Cdtw',
        api_base_url = 'https://mastodont.cat')


def closest_qurater(h, m):

    if (h % 12 )== 0:
        h= 12
    else:
        h = h % 12
    q= round(m/15)
    if q==4:
        if h==12:
            h=1
        else:
            h=h+1
    if q==0:
        q=4
    return h,q

def DingDang(h,q):
    text="🛎️  "
    print (range(q))
    #print (len(q))
    for i in range(q):
        text = text + "ding"
        if i != q-1:
            text = text + ", "
        else:
            text = text + "!"

    if q == 4:
        text = text + "\n🔔  "
        for j in range(h):
            text = text + "DANG"
            if j != h-1:
                text = text + ", "
            else:
                text = text + "!"
    return text

def main():
    now = datetime.now()
    print(now)
    hours = now.strftime("%H")
    minutes = now.strftime("%M")
    print("Current Time = {} : {}".format(hours, minutes))

    h,q=closest_qurater(int(hours), int(minutes))

    print("Current Time = {} : {}".format(h, q))

    text = DingDang(h,q)

    print (text)
    mastodon.toot(text)



if __name__ == "__main__":
    main()
