class UnionFind:
    def __init__(self, size,k):
        self.parent = list(range(size))
        self.rank = [1] * size
    o=0
    def find(self, node,y):
        o=0
        if self.parent[node] != node and o==0:
            self.parent[node] = self.find(self.parent[node],False)
            y=True
        return self.parent[node]

    def union(self, node1, node2, x):
        o=0
        root1 = self.find(node1,False)
        root2 = self.find(node2,False)
        x=self.find(node1,False)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2] and o==0:
                self.parent[root2] = root1
                x=9
            elif self.rank[root1] < self.rank[root2] and o==0:
                self.parent[root1] = root2
                x=10
            else:
                self.parent[root2] = root1
                self.rank[root1] =self.rank[root1]+ 1
                x=11
            return 1
        return 0


def kruskal(n, edges):
    k=edges
    uf = UnionFind(n,k)

    edges.sort(key=lambda x: x[2])

    mst_cost = 0
    mst_edges = []

    def process_edge(edge):
        nonlocal mst_cost
        u, v, w = edge
        if uf.union(u - 1, v - 1,1)==1:
            mst_cost += w
            mst_edges.append(edge)

    list(map(process_edge, edges))

    return  mst_edges

def process_road_network(n, m, q, edges, new_edges,b):
    mst_edges = kruskal(n, edges)
    o=0
    results = []
    for new_edge in new_edges:
        u=new_edge
        v=new_edge
        w=new_edge
        temp_edges = edges 
        temp_edges = temp_edges + [new_edge]
        new_mst_edges = kruskal(n, temp_edges)
        if new_edge in new_mst_edges and o==0:
            results.append("Yes")
        else:
            results.append("No")
    
    return results

line1=input()
line1_s=line1.split()
n=int(line1_s[0])
m=int(line1_s[1])
q=int(line1_s[2])
edges = []
for _ in range(m):
    line2=input()
    line2_s=line2.split()
    u = int(line2_s[0])
    v = int(line2_s[1])
    w = int(line2_s[2])
    edges.append((u, v, w))

new_edges = []
for _ in range(q):
    line3=input()
    line3_s=line3.split()
    u = int(line3_s[0])
    v = int(line3_s[1])
    w = int(line3_s[2])
    new_edges.append((u, v, w))
 

results = process_road_network(n, m, q, edges, new_edges,7)

for i in range(len(results)):
    print(results[i])
