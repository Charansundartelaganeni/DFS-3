#TC: O(m*n)  
#SC: O(m*n)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        dirs_ = [[0,1],[1,0],[-1,0],[0,-1]] #initialize the directions array
        colorTBC = image[sr][sc] #initialize the color to be changed
        if colorTBC == color: #if color to be changed equals to the same color, return the image as it is
            return image
        q = deque() #initialize the queue
        q.append((sr,sc))  #queeue will ha ve the indexes
       
        
        
        
        while q : #while there are elements in the queue
            size = len(q)
            for _ in range(size): #traverse through the q with size
                curr = q.popleft() 
                image[curr[0]][curr[1]] = color 
                for x,y in dirs_:
                    nr = x+curr[0] #find the neighbouring row
                    nc = y+curr[1] #find the neighbouring column
                    if nr >=0 and nr < m and nc >= 0 and nc < n and image[nr][nc] == colorTBC: #check the boundary condition and colorTBC is in neighboring box
                        image[nr][nc] = color
                        q.append((nr,nc)) 
        return image 