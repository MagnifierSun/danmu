import time, sys
import sqlite3
from danmu import DanMuClient
from datetime import *
import threading

conn = sqlite3.connect('test.db',check_same_thread=False)
cursor = conn.cursor()

# def pp(msg):
#     print(msg.encode(sys.stdin.encoding, 'ignore').
#           decode(sys.stdin.encoding))
# def write_to_sqlite(url,content,time_now):
#
#     cursor.execute("insert into "+data_list[url]+" values(?,?)", ( time_now, content))
#     conn.commit()

def print_dm(message):
    pass


def get_danmu_with_rid( rid):

    dmc = DanMuClient( rid)
    if not dmc.isValid():
        print('Url not valid')
    dmc.danmu(print_dm)
    dmc.start(blockThread=True)

data_list={
    # 'http://www.douyu.com/846805': 'sjss',
    # 'http://www.panda.tv/6666':'pdd'
    'http://www.douyu.com/56040': 'youtiao',
    'http://www.panda.tv/16688': 'xiaoma'
}


for rid in data_list:
    target_thread = threading.Thread(target=get_danmu_with_rid, args=(rid,),
                                     name='thread-' + rid)
    # target_thread.setDaemon(True)
    target_thread.start()
