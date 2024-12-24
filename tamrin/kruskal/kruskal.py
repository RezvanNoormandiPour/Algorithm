class DisjointSet:
    def init(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
 
    ds = DisjointSet(n)
   
    edges.sort(key=lambda x: x[2])
    
    mst_weight = 0
    mst_edges = []

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_edges.append((u, v, w))
            mst_weight += w

    return mst_weight, mst_edges

def main():
   
    n, m = map(int, input().split())
    
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    mst_weight, mst_edges = kruskal(n, edges)
    print(mst_weight)
    

    mst_edges.sort(key=lambda x: (min(x[0], x[1]), max(x[0], x[1]), x[2]))
    
    for u, v, w in mst_edges:
        print(min(u, v), max(u, v), w)

if __name__ == "__main__":
    main()
