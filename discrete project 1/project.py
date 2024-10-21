from collections import defaultdict, deque

file_in = open('testcase.txt', 'r').read()
split_file = file_in.split('\n')
clauses = [list(map(int, line.split(' '))) for line in split_file]

implications = defaultdict(list)

for i in range(len(clauses)):
   implications[-clauses[i][0]].append(clauses[i][1])
   implications[-clauses[i][1]].append(clauses[i][0])
print(implications)

currentAssignments = []

n = 61 # manully put in how many varaibles there are

for i in range(n):
    currentAssignments.append(None)

class Variable:
    def __init__(self, index, value):
        self.index = index
        self.value = value
    
    def assign(self, value):
        self.value.append(value)    

contradiction = False
justAssigned = []

def bfs(var):
    global contradiction
    todo = deque()
    todo.append(var)

    if var > 0:
        currentAssignments[var] = True
    else: 
        currentAssignments[-var] = False
    justAssigned.append(var)

    # is there something to see if a variable is assigned yet?
    while len(todo) > 0:
        current = todo.popleft()
        print(current, implications[current])
        for impl in implications[current]:
            print(impl)
            if impl > 0:
                #check if the variable is set yet
                if currentAssignments[impl] == True:
                    continue
                #if it is set to true then continue on
                #if its set to false we have found a contradiction
                if currentAssignments[impl] == False:
                    contradiction = True
                    break
                
                # if it is not assigned assign it to true
                currentAssignments[impl] = True
                todo.append(impl)
                justAssigned.append(impl)

            else:
                #check if the variable is set yet
                #if it is set to false then continue on
                if currentAssignments[-impl] == False:
                    continue

                #if its set to true we have found a contradiction
                if currentAssignments[-impl] == True:
                    contradiction = True 
                    break

                # if it is not assigned assign it to false
                currentAssignments[-impl] = False
                todo.append(impl)
                justAssigned.append(impl)

            todo.append(impl)


# if found contradiction clear the assignments and set 1 to False and do it again
for i in range(1, n):
    if currentAssignments[i] == None:
        print(f"starting bfs at {i}")
        bfs(i)
        if contradiction == True:
            # set contradictions to false
            contradiction = False
            # set curent assignments back to None
            for element in justAssigned:
                currentAssignments[abs(element)] = None
            # clear justAssigned
            justAssigned = []
            # call bfs again now with 1 set to false
            bfs(-i)
            # if contradictions contiues to be false even after setting 1 to false then there is no solution
            if contradiction == True:
                print("FALSE")
                break
print(currentAssignments)
