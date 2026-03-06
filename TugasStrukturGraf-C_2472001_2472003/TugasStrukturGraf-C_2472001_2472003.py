# NRP - Nama Anggota 1 : 2472001 - Aurellia Yemima Tomy
# NRP - Nama Anggota 2 : 2472003 - Maria Mayang Prihariyanti Panduwardani 

# def Breadth First Search (BFS)
# Kamus lokal
# G : matriks ukuran n x n
# nodes : List yang berisi nama atau label dari setiap simpul (node)
# u : indeks awal untuk memulai pencarian 
# n : total simpul dalam graf 
# visited : list untuk mencatat simpul yang sudah dikunjungi (boolean)
# Q : var untuk menyimpan urutan simpul yang akan dikunjungi
# w : variabel untuk mengambil elemen pertama dari antrian
def BFS(G, nodes, u, n):
    visited = [False] * n
    Q = []
    
    Q = Q + [u]
    
    print(" Menampilkan Traversal dengan BFS : ")
    
    while (len(Q) > 0):
        w = Q.pop(0)
        
        if (visited[w] == False):
            print(nodes[w], end=" ")
            visited[w] = True
            
            for v in range(n):
                if (G[w][v] == 1 and not visited[v]):
                    Q = Q + [v]
    print()

# def Depth First Search (DFS)
# Kamus lokal
# G : matriks ukuran n x n
# u : indeks awal untuk memulai pencarian
# nodes : List yang berisi nama atau label dari setiap simpul (node)
# visited : list untuk mencatat simpul yang sudah dikunjungi (boolean)
# n : total simpul dalam graf
def DFS(G, u, nodes, visited):
    print(nodes[u], end=" ")
    
    visited[u] = True
    
    n = len(G)
    for w in range(0, n, 1):
        if (G[u][w] == 1):
            if (visited[w] == False):
                DFS(G, w, nodes, visited)


### Program utama ###
# Kamus lokal
# nodes1 : list yang berisi nama atau label dari setiap simpul pada graf pertama
# G1 : matriks ketetanggaan untuk graf pertama
# nodes2 : list yang berisi nama atau label dari setiap simpul pada graf kedua
# G2 : matriks ketetanggaan untuk graf kedua
# visited1 : list untuk mencatat simpul yang sudah dikunjungi pada graf pertama (boolean)
# visited2 : list untuk mencatat simpul yang sudah dikunjungi pada graf kedua (boolean)
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
    print()

    print("KASUS UJI 2 (GRAF HURUF KECIL)")
    print("-- menampilkan traversal dengan bfs --")
    BFS(G2, nodes2, 0, len(nodes2))
    print()

    print("KASUS UJI 1 (GRAF KAPITAL)")
    print("-- menampilkan traversal dengan dfs --")
    visited1 = [False] * len(nodes1)
    DFS(G1, 0, nodes1, visited1)
    print()

    print("KASUS UJI 2 (GRAF HURUF KECIL)")
    print("-- menampilkan traversal dengan dfs --")
    visited2 = [False] * len(nodes2)
    DFS(G2, 0, nodes2, visited2)

if __name__ == "__main__":
    main()

