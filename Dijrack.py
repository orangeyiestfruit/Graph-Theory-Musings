connections = [[0,1,2],[0,2,4],[1,2,3],[1,4,6],[2,3,7],[3,4,5],[3,6,9],[4,5,8],[5,7,4],[6,7,3]]
upnodes = [[0,0],[1,100],[2,100],[3,100],[4,100],[5,100],[6,100],[7,100],[8,100]]
als = []
for nodes in range(0,len(connections)):
    for num in range(0,len(connections)-1):
        if connections[num][1]==nodes:
            if upnodes[connections[num][0]][1]+connections[num][2]<upnodes[nodes][1]:
                upnodes[nodes][1]=upnodes[connections[num][0]][1]+connections[num][2]
print(upnodes)
print(als)
