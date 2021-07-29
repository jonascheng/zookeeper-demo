# publish data to /test1
from kazoo.client import KazooClient
import json
import time
import logging

logger = '[%(asctime)s] %(levelname)-5s %(message)s'
logging.basicConfig(format=logger,
                    level=logging.DEBUG,
                    datefmt='%d-%m-%Y %H:%M:%S')

# create zookeeper client
zk = KazooClient(hosts="zoo1:2181,zoo2:2181")
zk.start()

znode = {
  "username": "aaaaaaa",
  "passowrd": "ccccccc"
}
znode = json.dumps(znode)
znode = bytes(znode, encoding="utf-8")
zk.set("/test1", znode)
zk.stop()
