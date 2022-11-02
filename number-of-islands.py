#TC:O(m*n) 
#SC:O(m*n)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.count=0
        self.dirs = [[0,1],[1,0],[-1,0],[0,-1]] #assign the directions array

        for i in range(self.m): #traverse through the matrix and if the element is 1, then do dfs and find the count
            for j in range(self.n):
                if grid[i][j]=="1":
                    self.dfs(grid,i,j)
                    self.count+=1
        print(grid)
        return self.count #finally return the count

    def dfs(self,grid,i,j): #dfs function
        #base
        if grid[i][j]=="0": #if the ele is 0, then unfold the recursion
            return
        
        #logic
        grid[i][j]="0" #set the visited elements as 0
        for x,y in self.dirs: #traverse through directions array
            nr = x+i #find the neighbouring row
            nc = y+j #find the neighbouring column
            if nr>=0 and nr<self.m and nc>=0 and nc<self.n: #check the boundary conditions and do the DFS again
                self.dfs(grid,nr,nc) 