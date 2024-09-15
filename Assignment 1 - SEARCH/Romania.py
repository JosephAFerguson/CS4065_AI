class Romanian_Map:
    NODES = [i + 1 for i in range(20)]
    #         City,              Node Id
    NAMES = ['Arad',              # 1
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

    #SLD to Bucharest
    INFORMED_Heur = [366,0,160,242,161,176,77,151,226,244,241,234,380,100,193,253,329,80,199,374]
    # Adjacency matrix
    ADJ_MAT = [
    [[17,118], [16,140],[20,75]],        # Arad [neighbor node, weight/cost of path]
    [[6,211],[7,90],[14,101],[17,85]],   # Bucharest
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
    [[1,140],[6,99],[13,151],[16,80]],   # Sibiu
    [[1,118],[10,111]],                  # Timisoara
    [[2,85],[8,98],[19,142]],            # Urziceni
    [[9,92],[18,142]],                   # Vaslui
    [[1,75],[13,71]],                    # Zerind
    ]
