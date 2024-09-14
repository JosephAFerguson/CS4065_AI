import Searches

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
    else:
        print('Demonstration rejected. Running performance tests . . .\n')
        print('No performance tests made yet.\n')

    cont = str(input("Please enter Y to continue or N to stop:"))
    if cont =='N':
        break
