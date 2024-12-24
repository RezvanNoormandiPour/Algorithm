import sys
import heapq

def dijkstra(num_nodes, edges):

    W = [[float('inf')] * (num_nodes + 1) for _ in range(num_nodes + 1)]

    for i in range(1, num_nodes + 1):
        W[i][i] = 0 
    for src, dest, weight in edges:
        W[src][dest] = weight

   
    length = [float('inf')] * (num_nodes + 1)
    touch = [-1] * (num_nodes + 1)
    
    
    start_node = 1
    length[start_node] = 0
    
    
    priority_queue = [(0, start_node)]  
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

       
        if current_distance > length[current_node]:
            continue
        
        
        for neighbor in range(1, num_nodes + 1):
            if W[current_node][neighbor] != float('inf'):
                distance = current_distance + W[current_node][neighbor]
                
            
                if distance < length[neighbor]:
                    length[neighbor] = distance
                    touch[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

    return touch, length


def main():
 
    n, e = map(int, input().split())
    
    edges = []
    
    for _ in range(e):
        src, dest, weight = map(int, input().split())
        edges.append((src, dest, weight))
    
    touch, length = dijkstra(n, edges)
    
 
    print(" ".join(map(str, touch[1:])))
    print(" ".join(map(str, length[1:])))

if __name__ == "__main__":
    main()
