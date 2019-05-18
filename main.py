#import external module
import sys
sys.path.append("geopy/")
sys.path.append("geographiclib/")
from geopy.distance import geodesic
import dijsktra

#longitude, latitude
details = {
    '捷運一號出口': (25.032913, 121.435268),
    '校門口': (25.032641, 121.434199),
    '第一圓環前十字路口': (25.033651, 121.433789),
    '全聯福利中心': (25.033005, 121.434563),
    '耕莘樓': (25.033751, 121.433207),
    '理工學院': (25.034220, 121.432025),
    '舒德樓': (25.033991, 121.434063),
    '食科冰淇淋': (25.034744, 121.434514), 
    '第一圓環': (25.034545, 121.433374),
    '民生學院': (25.035510, 121.434094),
    '第二圓環': (25.036319, 121.432634),
    '羅耀拉大樓': (25.036434, 121.430873),
    '心園': (25.036993, 121.429795),
    '傳播學院': (25.036774, 121.433642),
    '利瑪竇大樓': (25.037332, 121.431199),
    '風華廣場': (25.037118, 121.432342),
    '文開樓': (25.037265, 121.433802),
    '中美堂': (25.038240, 121.431816),
}

#distance
values = list(details.values()) #turn dictionary to list
nodes = list(details.keys())

edges = []

#add all
# for i in range(len(nodes)):
#     for j in range(len(nodes)):
#         edges.append([nodes[i], nodes[j], geodesic(values[i], values[j]).meters])
        # print("'",n[i],"到",n[j],"的距離:",geodesic(v[i], v[j]).meters)
        # print('\'%s\', \'%s\', %d' % (nodes[i], nodes[j], geodesic(values[i], values[j]).meters))

#捷運一號出口
edges.append(['捷運一號出口', '校門口', geodesic(details['捷運一號出口'], details['校門口']).meters])

#校門口
#往回
edges.append(['校門口', '捷運一號出口', geodesic(details['校門口'], details['捷運一號出口']).meters])
#往前
edges.append(['校門口', '第一圓環前十字路口', geodesic(details['校門口'], details['第一圓環前十字路口']).meters])
#往右
edges.append(['校門口', '全聯福利中心', geodesic(details['校門口'], details['全聯福利中心']).meters])

#全聯福利中心
#往左
edges.append(['全聯福利中心', '校門口', geodesic(details['全聯福利中心'], details['校門口']).meters])
edges.append(['全聯福利中心', '第一圓環前十字路口', geodesic(details['全聯福利中心'], details['第一圓環前十字路口']).meters])

#第一圓環前十字路口
#往前
edges.append(['第一圓環前十字路口', '第一圓環', geodesic(details['第一圓環前十字路口'], details['第一圓環']).meters])
#往回
edges.append(['第一圓環前十字路口', '校門口', geodesic(details['第一圓環前十字路口'], details['校門口']).meters])
edges.append(['第一圓環前十字路口', '全聯福利中心', geodesic(details['第一圓環前十字路口'], details['全聯福利中心']).meters])
#往左
edges.append(['第一圓環前十字路口', '耕莘樓', geodesic(details['第一圓環前十字路口'], details['耕莘樓']).meters])
#往右
edges.append(['第一圓環前十字路口', '舒德樓', geodesic(details['第一圓環前十字路口'], details['舒德樓']).meters])

#耕莘樓
#往前
edges.append(['耕莘樓', '第一圓環', geodesic(details['耕莘樓'], details['第一圓環']).meters])
#往後
edges.append(['耕莘樓', '第一圓環前十字路口', geodesic(details['耕莘樓'], details['第一圓環前十字路口']).meters])
#往左
edges.append(['耕莘樓', '理工學院', geodesic(details['耕莘樓'], details['理工學院']).meters])
#往右
edges.append(['耕莘樓', '舒德樓', geodesic(details['耕莘樓'], details['舒德樓']).meters])

#理工學院
edges.append(['理工學院', '耕莘樓', geodesic(details['理工學院'], details['耕莘樓']).meters])
edges.append(['理工學院', '第一圓環', geodesic(details['理工學院'], details['第一圓環']).meters])

#舒德樓
#往前
edges.append(['舒德樓', '第一圓環', geodesic(details['舒德樓'], details['第一圓環']).meters])
edges.append(['舒德樓', '食科冰淇淋', geodesic(details['舒德樓'], details['食科冰淇淋']).meters])
#往後
edges.append(['舒德樓', '第一圓環前十字路口', geodesic(details['舒德樓'], details['第一圓環前十字路口']).meters])
#往左
edges.append(['舒德樓', '耕莘樓', geodesic(details['舒德樓'], details['耕莘樓']).meters])

#食科冰淇淋
#往上
edges.append(['食科冰淇淋', '民生學院', geodesic(details['食科冰淇淋'], details['民生學院']).meters])
#往後
edges.append(['食科冰淇淋', '舒德樓', geodesic(details['食科冰淇淋'], details['舒德樓']).meters])
#往左
edges.append(['食科冰淇淋', '第一圓環', geodesic(details['食科冰淇淋'], details['第一圓環']).meters])

#第一圓環
#往前
edges.append(['第一圓環', '第二圓環', geodesic(details['第一圓環'], details['第二圓環']).meters])

#往回
edges.append(['第一圓環', '第一圓環前十字路口', geodesic(details['第一圓環'], details['第一圓環前十字路口']).meters])
edges.append(['第一圓環', '耕莘樓', geodesic(details['第一圓環'], details['耕莘樓']).meters])
edges.append(['第一圓環', '舒德樓', geodesic(details['第一圓環'], details['舒德樓']).meters])
#往左
edges.append(['第一圓環', '理工學院', geodesic(details['第一圓環'], details['理工學院']).meters])
#往右
edges.append(['第一圓環', '食科冰淇淋', geodesic(details['第一圓環'], details['食科冰淇淋']).meters])
#往右上
edges.append(['第一圓環', '民生學院', geodesic(details['第一圓環'], details['民生學院']).meters])

#民生學院
edges.append(['民生學院', '第一圓環', geodesic(details['民生學院'], details['第一圓環']).meters])
edges.append(['民生學院', '第二圓環', geodesic(details['民生學院'], details['第二圓環']).meters])
edges.append(['民生學院', '食科冰淇淋', geodesic(details['民生學院'], details['食科冰淇淋']).meters])

#第二圓環
#往前
edges.append(['第二圓環', '風華廣場', geodesic(details['第二圓環'], details['風華廣場']).meters])
#往回
edges.append(['第二圓環', '第一圓環', geodesic(details['第二圓環'], details['第一圓環']).meters])
edges.append(['第二圓環', '民生學院', geodesic(details['第二圓環'], details['民生學院']).meters])
#往左
edges.append(['第二圓環', '羅耀拉大樓', geodesic(details['第二圓環'], details['羅耀拉大樓']).meters])
#往右
edges.append(['第二圓環', '傳播學院', geodesic(details['第二圓環'], details['傳播學院']).meters])

#羅耀拉大樓
#往上
edges.append(['羅耀拉大樓', '利瑪竇大樓', geodesic(details['羅耀拉大樓'], details['利瑪竇大樓']).meters])
#往右
edges.append(['羅耀拉大樓', '第二圓環', geodesic(details['羅耀拉大樓'], details['第二圓環']).meters])
#往左
edges.append(['羅耀拉大樓', '心園', geodesic(details['羅耀拉大樓'], details['心園']).meters])

#心園
edges.append(['心園', '羅耀拉大樓', geodesic(details['心園'], details['羅耀拉大樓']).meters])
edges.append(['心園', '利瑪竇大樓', geodesic(details['心園'], details['利瑪竇大樓']).meters])

#傳播學院
edges.append(['傳播學院', '第二圓環', geodesic(details['傳播學院'], details['第二圓環']).meters])

#風華廣場
#往前
edges.append(['風華廣場', '中美堂', geodesic(details['風華廣場'], details['中美堂']).meters])
#往回
edges.append(['風華廣場', '第二圓環', geodesic(details['風華廣場'], details['第二圓環']).meters])
#往左
edges.append(['風華廣場', '利瑪竇大樓', geodesic(details['風華廣場'], details['利瑪竇大樓']).meters])
#往右
edges.append(['風華廣場', '文開樓', geodesic(details['風華廣場'], details['文開樓']).meters])

#利瑪竇大樓
#往前
edges.append(['利瑪竇大樓', '中美堂', geodesic(details['利瑪竇大樓'], details['中美堂']).meters])
#往回
edges.append(['利瑪竇大樓', '羅耀拉大樓', geodesic(details['利瑪竇大樓'], details['羅耀拉大樓']).meters])
#往左
edges.append(['利瑪竇大樓', '心園', geodesic(details['利瑪竇大樓'], details['心園']).meters])
#往右
edges.append(['利瑪竇大樓', '風華廣場', geodesic(details['利瑪竇大樓'], details['風華廣場']).meters])

#文開樓
#往左
edges.append(['文開樓', '風華廣場', geodesic(details['文開樓'], details['風華廣場']).meters])

#中美堂
#往左下
edges.append(['中美堂', '利瑪竇大樓', geodesic(details['中美堂'], details['利瑪竇大樓']).meters])
#往回
edges.append(['中美堂', '風華廣場', geodesic(details['中美堂'], details['風華廣場']).meters])


g = dijsktra.Graph()
g.get_node(nodes)
g.get_edge(edges)
# g.getDistances()
visited, path = dijsktra.run(g, '民生學院')
# print(geodesic(details['民生學院'], details['第二圓環']).meters)
# print(geodesic(details['第二圓環'], details['風華廣場']).meters)
# print(geodesic(details['風華廣場'], details['中美堂']).meters)

# print(visited)
# print(path)
print(dijsktra.shortest_path(g, '校門口', '中美堂'))
