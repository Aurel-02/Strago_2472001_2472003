# NRP - Nama Anggota 1 : 2472001 - Aurellia Yemima Tomy
# NRP - Nama Anggota 2 : 2472003 - Maria Mayang Prihariyanti Panduwardani 

def BFS(G, nodes, u, n):
    visited = [False] * n
    Q = []
    
    Q = Q + [u]
    
    print(" Menampilkan Traversal dengan BFS : ")
    
    while len(Q) > 0:
        w = Q.pop(0)
        
        if visited[w] == False:
            print(nodes[w], end=" ")
            visited[w] = True
            
            for v in range(n):
                if G[w][v] == 1 and not visited[v]:
                    Q = Q + [v]
    print()

def main():
    nodes1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] 
    G1 = [
    [0, 1, 1, 0, 0, 0, 0], 
    [1, 0, 0, 1, 1, 0, 0], 
    [1, 0, 0, 0, 0, 1, 1], 
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0]  
    ]

    nodes2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    G2 = [
        [0, 1, 1, 0, 0, 0, 0, 0, 0], 
        [1, 0, 0, 1, 1, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 1, 1, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0, 1], 
        [0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0]  
    ]

    print("KASUS UJI 1 (GRAF KAPITAL)")
    print("-- menampilkan traversal dengan bfs --")
    BFS(G1, nodes1, 0, len(nodes1))

    print("KASUS UJI 2 (GRAF HURUF KECIL)")
    print("-- menampilkan traversal dengan bfs --")
    BFS(G2, nodes2, 0, len(nodes2))
    
if __name__ == "__main__":
    main()

