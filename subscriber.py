from kazoo.client import KazooClient
import time
import logging

logger = '[%(asctime)s] %(levelname)-5s %(message)s'
logging.basicConfig(format=logger,
                    level=logging.DEBUG,
                    datefmt='%d-%m-%Y %H:%M:%S')

# create a zookeeper client
zk = KazooClient(hosts="zoo1:2181,zoo2:2181")
zk.start()
if zk.exists("/test1"):
   logging.info("/test1 exist")
else:
   zk.create("/test1")

@zk.DataWatch("/test1")
def zk_test(data, stat, event):
    if event:
      logging.info(data.decode())
      logging.info(f"Version is {stat.version}")
      logging.info(f"Event is {event}")
    else:
      logging.info(f"first start up")

while True:
    time.sleep(60)
