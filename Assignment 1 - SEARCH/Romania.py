class Romanian_Map:
     NODES = [i + 1 for i in range(20)]
     #         City,              Node Id
     NAMES = ['Arad',             # 1
             'Bucharest',         # 2
             'Craiova',           # 3
             'Drobeta',           # 4
             'Eforie',            # 5
             'Fagaras',           # 6
             'Giurgiu',           # 7
             'Hirsova',           # 8
             'Iasi',              # 9
             'Lugoj',             # 10
             'Mehadia',           # 11
             'Neamt',             # 12
             'Oradea',            # 13
             'Pitesti',           # 14
             'Rimnicu Vilcea',    # 15
             'Sibiu',             # 16
             'Timisoara',         # 17
             'Urziceni',          # 18
             'Vaslui',            # 19
             'Zerind']            # 20

     # Straight Line Distance (SLD) to Bucharest
     SLD_Heuristic = [366,  # Arad
                     0,    # Bucharest
                     160,  # Craiova
                     242,  # Drobeta
                     161,  # Eforie
                     176,  # Fagaras
                     77,   # Giurgiu
                     151,  # Hirsova
                     226,  # Iasi
                     244,  # Lugoj
                     241,  # Mehadia
                     234,  # Neamt
                     380,  # Oradea
                     100,  # Pitesti
                     193,  # Rimnicu Vilcea
                     253,  # Sibiu
                     329,  # Timisoara
                     80,   # Urziceni
                     199,  # Vaslui
                     374]  # Zerind
     NODES_AWAY_Heuristic = [3, #Arad
                   0, #Bucharest
                   2, #Craiova
                   3, #Drobeta
                   3, #Eforie
                   1, #Fagaras
                   1, #Giurgiu
                   2, #Hirsova
                   3, #Iasi
                   5, #Lugoj
                   4, #Mehadia
                   4, #Neamt
                   3, #Oradea
                   1, #Pitesti
                   2, #Rimnicu Vilcea
                   2, #Sibiu
                   4, #Timisoara
                   1, #Urziceni
                   2, #Vaslui
                   4] #Zerind
     # Adjacency matrix
     ADJ_MAT = [
    [[17,118], [16,140],[20,75]],        # Arad [neighbor node, weight/cost of path]
    [[6,211],[7,90],[14,101],[18,85]],   # Bucharest
    [[4,120],[14,138],[15,146]],         # Craiova
    [[3,120], [11,75]],                  # Drobeta
    [[8,86]],                            # Eforie
    [[2,211],[16,99]],                   # Fagaras
    [[2,90]],                            # Giurgiu
    [[5,86],[18,98]],                    # Hirsova
    [[12,87],[19,92]],                   # Iasi
    [[11,70],[17,111]],                  # Lugoj
    [[4,75],[10,70]],                    # Mehadia
    [[9,87]],                            # Neamt
    [[16,151],[20,71]],                  # Oradea
    [[2,101],[3,138],[15,97]],           # Pitesti
    [[3,146],[14,97],[16,80]],           # Rimnicu Vilcea
    [[1,140],[6,99],[13,151],[15,80]],   # Sibiu
    [[1,118],[10,111]],                  # Timisoara
    [[2,85],[8,98],[19,142]],            # Urziceni
    [[9,92],[18,142]],                   # Vaslui
    [[1,75],[13,71]],                    # Zerind
    ]