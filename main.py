#import external module
import sys
sys.path.append("geopy/")
sys.path.append("geographiclib/")
from geopy.distance import geodesic
import dijsktra

#longitude, latitude
details = {
    '捷運一號出口': (25.032913, 121.435268),
    '大門口': (25.032641, 121.434199),
    '野聲樓': (25.033356, 121.434536),
    '耕莘樓': (25.033751, 121.433207),
    '舒德樓': (25.033991, 121.434063),
    '輔園': (25.034472, 121.434287),
    '利瑪竇大樓': (25.037367, 121.431232),
    '食科冰淇淋': (25.034744, 121.434514), 
    '朝橒樓': (25.035269, 121.433404),
    '文開樓': (25.037265, 121.433802),
    '民生學院': (25.035517, 121.433860),
    '公博樓': (25.036309, 121.434520),
    '風華廣場': (25.037063, 121.432335),
    '敦煌書局': (25.035317, 121.431609),
    '心園': (25.036993, 121.429795),
    '進修部': (25.037735, 121.430759),
    '中美堂': (25.038240, 121.431816),
    '淨心堂': (25.036040, 121.432340)
}

#distance
# values = list(details.values()) #turn dictionary to list
# nodes = list(details.keys())

edges = []

#add all
# for i in range(len(nodes)):
#     for j in range(len(nodes)):
#         edges.append([nodes[i], nodes[j], geodesic(values[i], values[j]).meters])
        # print("'",n[i],"到",n[j],"的距離:",geodesic(v[i], v[j]).meters)
        # print('\'%s\', \'%s\', %d' % (nodes[i], nodes[j], geodesic(values[i], values[j]).meters))

#捷運一號出口
edges.append(['捷運一號出口', '大門口', geodesic(details['捷運一號出口'], details['大門口']).meters])

#野聲樓
edges.append(['野聲樓', '耕莘樓', geodesic(details['野聲樓'], details['耕莘樓']).meters])
#耕莘樓
edges.append(['耕莘樓', '野聲樓', geodesic(details['耕莘樓'], details['野聲樓']).meters])
edges.append(['耕莘樓', '野聲樓', geodesic(details['耕莘樓'], details['耕莘樓']).meters])
edges.append(['耕莘樓', '野聲樓', geodesic(details['耕莘樓'], details['耕莘樓']).meters])
edges.append(['耕莘樓', '野聲樓', geodesic(details['耕莘樓'], details['耕莘樓']).meters])

#舒德樓



g = dijsktra.Graph()
g.get_node(nodes)
g.get_edge(edges)
# g.getDistances()
visited, path = dijsktra.run(g, '民生學院')
# print(geodesic(detail['民生學院'], detail['花園夜市']).meters)
print(visited)
print(path)