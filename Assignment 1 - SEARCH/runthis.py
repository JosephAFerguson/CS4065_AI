import Searches
import time

#Demonstration functions
def test_BFS():
    print('Starting demonstration for Breadth-First Search with all nodes. Destination: Bucharest')
    for i in range(20):
        Searches.print_BFS(i + 1, 'Bucharest')
def test_DFS():
    print('Starting demonstration for Depth-First Search with all nodes. Destination: Bucharest')
    for i in range(20):
        Searches.print_DFS(i + 1, 'Bucharest')
def test_G():
    print('Starting demonstration for Greedy Search with all nodes. Destination: Bucharest\n')
    op = int(input('Type 1 to use the SLD heuristic or 2 to use the Nodes Away heuristic: '))
    for i in range(20):
        Searches.print_greedy(i + 1, 'Bucharest',op)
def test_A():
    print('Starting demonstration for A* Search with all nodes. Destination: Bucharest\n')
    op = int(input('Type 1 to use the SLD heuristic or 2 to use the Nodes Away heuristic: '))
    for i in range(20):
        Searches.print_A_star(i + 1, 'Bucharest',op)

print('Welcome To This Romanian Map Search Tool\n')
print('Starting Program...\n')

#User Input Functionality
cont = True
while cont:
    dem = str(input('Would you like to see the demonstration? (Y/N):'))
    if dem == 'Y' or dem == 'y':
        choice = int(input('Which search algorithm would you like to run?\n1. Breadth-First\n2. Depth-First\n3. Greedy\n4. A*\nInput: '))
        if choice==1:
            test_BFS()
        elif choice==2:
            test_DFS()
        elif choice==3:
            test_G()
        elif choice==4:
            test_A()
        else:
            print("Unexpected response")
            continue
    elif dem != 'N' and dem != 'n':
        print("Unexpected response")
        continue
    perf = str(input('Would you like to see the performance test? (Y/N):'))
    if perf == 'Y' or perf == 'y':
        print("\nTotal time for each search for all 20 nodes, 5 times (100 total searches):\n")
        start = time.time()
        for i in range(100):
            Searches.timed_BFS(i%20 + 1, 'Bucharest')
        end = time.time()
        print(f'BFS: {(end - start) * 1000:5f} ms.')

        start = time.time()
        for i in range(100):
            Searches.timed_DFS(i % 20 + 1, 'Bucharest')
        end = time.time()
        print(f'DFS: {(end - start) * 1000:5f} ms.')

        start = time.time()
        for i in range(100):
            Searches.timed_Greedy(i % 20 + 1, 'Bucharest', 1)
        end = time.time()
        print(f'Greedy using SLD Heuristic: {(end - start) * 1000:5f} ms.')

        start = time.time()
        for i in range(100):
            Searches.timed_Greedy(i % 20 + 1, 'Bucharest', 2)
        end = time.time()
        print(f'Greedy using Nodes Away Heuristic: {(end - start) * 1000:5f} ms.')

        start = time.time()
        for i in range(100):
            Searches.timed_A_Star(i % 20 + 1, 'Bucharest', 1)
        end = time.time()
        print(f'A* using SLD heuristic: {(end - start) * 1000:5f} ms.')

        start = time.time()
        for i in range(100):
            Searches.timed_A_Star(i % 20 + 1, 'Bucharest', 2)
        end = time.time()
        print(f'A* using Nodes Away heuristic: {(end - start) * 1000:5f} ms.')

        print("\nTotal cost for each search for all 20 nodes:\n")
        c = 0
        for i in range(20):
            c += Searches.measured_BFS(i%20 + 1, 'Bucharest')
        print(f'BFS: Cost = {c}.')

        c = 0
        for i in range(20):
            c += Searches.measured_DFS(i%20 + 1, 'Bucharest')
        print(f'DFS: Cost = {c}.')

        c = 0
        for i in range(20):
            c += Searches.measured_Greedy(i%20 + 1, 'Bucharest', 1)
        print(f'Greedy using SLD Heuristic: Cost = {c}.')

        c = 0
        for i in range(20):
            c += Searches.measured_Greedy(i%20 + 1, 'Bucharest', 2)
        print(f'Greedy using Nodes Away Heuristic: Cost = {c}.')

        c = 0
        for i in range(20):
            c += Searches.measured_A_Star(i%20 + 1, 'Bucharest', 1)
        print(f'A* using SLD Heuristic: Cost = {c}.')

        c = 0
        for i in range(20):
            c += Searches.measured_A_Star(i%20 + 1, 'Bucharest', 2)
        print(f'A* using Nodes Away Heuristic: Cost = {c}.')

    elif perf != 'N' and perf != 'n':
        print("Unexpected response")
        continue

    cont = str(input("Would you like to continue (Y/N):"))
    if cont == 'N' or cont == 'n':
        break
    elif cont != 'Y' and cont != 'y':
        print('Unexpected response')
        continue