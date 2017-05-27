import time, sys
import sqlite3
from danmu import DanMuClient
from datetime import *
import threading


def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
          decode(sys.stdin.encoding))


def print_dm(msg):
    # print(msg)
    pp('[%s] %s' % (msg['NickName'], msg['Content']))


def get_danmu_with_rid(host, rid):
    dmc = DanMuClient(host + rid)
    if not dmc.isValid():
        print('Url not valid')
    dmc.danmu(print_dm)
    dmc.start(blockThread=True)


dy_list = ['weixiao', '1746151', 'ShinyRuo']

human_list = {
    '6666': 'pdd',
    '10953': '君克',
    '666666': '若风'
}
panda_list = ['6666', '10953']

for rid in dy_list:
    print(rid)
    target_thread = threading.Thread(target=get_danmu_with_rid, args=('https://www.douyu.com/', rid,),
                                     name='thread-' + rid)
    # target_thread.setDaemon(True)
    target_thread.start()

for rid in panda_list:
    target_thread = threading.Thread(target=get_danmu_with_rid, args=('http://www.panda.tv/', rid,),
                                     name='thread-' + rid)
    target_thread.start()
