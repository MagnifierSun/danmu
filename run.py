import time, sys
import sqlite3
from danmu import DanMuClient
from datetime import *

def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
          decode(sys.stdin.encoding))


dmc = DanMuClient('https://www.douyu.com/dasima')
if not dmc.isValid(): print('Url not valid')
conn = sqlite3.connect('test.db')
cursor = conn.cursor()


@dmc.danmu
def danmu_fn(msg):
    pp('[%s] %s' % (msg['NickName'], msg['Content']))
    username = msg['NickName']
    usercontent = msg['Content']
    time_now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO dasima VALUES (?,?)", (time_now, usercontent))
    conn.commit()

@dmc.gift
def gift_fn(msg):
    pp('[%s] sent a gift!' % msg['NickName'])


@dmc.other
def other_fn(msg):
    pp('Other message received')


dmc.start(blockThread=True)
