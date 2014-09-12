"""
Project Euler #82
Erica Johnson, Sage Berg
9/11/14
"""

from queue import PriorityQueue

class Node():
    def __init__(self, edge, r, c):
        self.edgeCost = edge
        self.tentDist = 10**10
        self.row = r
        self.col = c
        
    def __repr__(self):
        return str(self.tentDist)
        
    def __lt__(self, other):
        return self.tentDist < other.tentDist
        
def parseMatrix(matrix):
    matList = list()
    for line in matrix:
        matList.append([int(string.strip()) for string in line.split(",")])
    for row in range(len(matList)):
        for col in range(len(matList[row])):
            matList[row][col] = Node(matList[row][col], row, col)
    #print(matList)
    return matList
        
def scanNode(curNode, row, col, matrix):
    targetNode = matrix[row][col]
    #print(curNode)
    if curNode.tentDist + targetNode.edgeCost < targetNode.tentDist:
        print(curNode)
        targetNode.tentDist = curNode.tentDist + targetNode.edgeCost

def shortestPath(startY, matrix):
    shortestSum = 10**10
    pq = PriorityQueue()
    curNode = matrix[startY][0]
    curNode.tentDist = curNode.edgeCost
    for row in matrix:
        for node in row:
            pq.put(node)
    while pq.qsize() > 0:
        curNode = pq.get() 
        if curNode.row > 0:
            scanNode(curNode, curNode.row - 1, curNode.col, matrix)
        if curNode.row < len(matrix) - 1:
            scanNode(curNode, curNode.row + 1, curNode.col, matrix)
        if curNode.col < len(matrix) - 1:
            scanNode(curNode, curNode.row, curNode.col + 1, matrix)
    for i in range(len(matrix)):
        if matrix[i][len(matrix) - 1].tentDist < shortestSum:
            shortestSum = matrix[i][len(matrix) - 1].tentDist
    #print(shortestSum)
    return shortestSum
    
def main(matrix):
    shortest = 10**10
    matList = parseMatrix(matrix)
    for startY in range(len(matList)):
        newPath = shortestPath(startY, matList)
        if newPath < shortest:
            shortest = newPath
    print(shortest)
        
main(open("matrix.txt"))