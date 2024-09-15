import Searches
import time

#Demonstration functions
def test_BFS():
    print('Starting demonstration for Breadth-First Search with all nodes. Destination: Bucharest')
    for i in range(20):
        Searches.BFS(i+1, 'Bucharest')
def test_DFS():
    print('Starting demonstration for Depth-First Search with all nodes. Destination: Bucharest')
    for i in range(20):
        Searches.DFS(i+1, 'Bucharest')
def test_G():
    print('Starting demonstration for Greedy Search with all nodes. Destination: Bucharest')
    for i in range(20):
        Searches.greedy(i+1, 'Bucharest')
def test_A():
    print('Starting demonstration for A* Search with all nodes. Destination: Bucharest')
    for i in range(20):
        Searches.A_star(i+1, 'Bucharest')
        
print('Welcome To This Romanian Map Search Tool\n')
print('Starting Program...\n')

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
            print("Unexpected reponse")
            continue
    elif dem != 'N' and dem != 'n':
        print("Unexpected reponse")
        continue
    perf = str(input('Would you like to see the performance test? (Y/N):'))
    if perf == 'Y' or perf == 'y':
        print("\nTotal time for each search for all 20 nodes, 5 times (100 total searches):\n")
        start = time.time()
        for i in range(100):
            Searches.timedBRS(i%20+1, 'Bucharest')
        end = time.time()
        print(f'BFS: {(end-start)*1000:5f} ms.')

        start = time.time()
        for i in range(100):
            Searches.timedDFS(i%20+1, 'Bucharest')
        end = time.time()
        print(f'DFS: {(end-start)*1000:5f} ms.')

        start = time.time()
        for i in range(100):
            Searches.timedGreedy(i%20+1, 'Bucharest')
        end = time.time()
        print(f'Greedy: {(end-start)*1000:5f} ms.')

        start = time.time()
        for i in range(100):
            Searches.timedA_Star(i%20+1, 'Bucharest')
        end = time.time()
        print(f'A*: {(end-start)*1000:5f} ms.')
    elif perf != 'N' and perf != 'n':
        print("Unexpected reponse")
        continue

    cont = str(input("Would you like to continue (Y/N):"))
    if cont == 'N' or cont == 'n':
        break
    elif cont != 'Y' and cont != 'y':
        print('Unexpected response')
        continue
