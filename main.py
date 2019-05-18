#import external module
import os
import sys
sys.path.append("geopy/")
sys.path.append("geographiclib/")
import dijsktra
import config
import time

nodes, edges = config.init()

g = dijsktra.Graph()
g.get_node(nodes)
g.get_edge(edges)

print("請參考 'all_spot.txt' 內的座標名稱，輸入起點和終點")
time.sleep(1)
os.startfile('all_spot.txt')

while True:
    _from = input("請輸入起點:")
    _to = input("請輸入終點:")
    distance, paths = dijsktra.shortest_path(g, _from, _to)

    ans = ""
    for i, path in enumerate(paths):
        if (i != len(paths)-1):
            ans += path + ","
        else:
            ans += path
    print("最短路徑:", ans)
    print("總距離:", distance, " 公尺")
    
