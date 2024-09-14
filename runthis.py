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
    dem = str(input('Would you like to see the demonstration? Enter Y for Yes or N for No:'))
    if dem=='Y':
        choice = int(input('Which search algorithm would you like to run? Enter 1 for Breadth-First, 2 for Depth-First, 3 for Greedy, 4 for A* : '))
        if choice==1:
            test_BFS()
        elif choice==2:
            test_DFS()
        elif choice==3:
            test_G()
        else:
            test_A()
    dem = str(input('Would you like to see the performance test? Enter Y for Yes or N for No:'))
    if dem=='Y':
        print('Demonstration rejected. Running performance tests . . .\n')
        start = time.time()
        for i in range(100):
            Searches.timedBRS(i%20+1, 'Bucharest')
        end = time.time()
        print(f'The time taken to run Breadth-First search for all 20 nodes, 5 times (100 searches in total) is {(end-start)*1000} ms.\n')

        start = time.time()
        for i in range(100):
            Searches.timedDFS(i%20+1, 'Bucharest')
        end = time.time()
        print(f'The time taken to run Depth-First search for all 20 nodes, 5 times (100 searches in total) is {(end-start)*1000} ms.\n')

        start = time.time()
        for i in range(100):
            Searches.timedGreedy(i%20+1, 'Bucharest')
        end = time.time()
        print(f'The time taken to run Greedy search for all 20 nodes, 5 times (100 searches in total) is {(end-start)*1000} ms.\n')

        start = time.time()
        for i in range(100):
            Searches.timedA_Star(i%20+1, 'Bucharest')
        end = time.time()
        print(f'The time taken to run A* search for all 20 nodes, 5 times (100 searches in total) is {(end-start)*1000} ms.\n')


    cont = str(input("Please enter Y to continue or N to stop:"))
    if cont =='N':
        break
