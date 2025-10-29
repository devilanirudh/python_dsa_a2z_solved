class Solution:
    def rowWithMax1s(self, mat):
      index = -1
      count = -1
      for i in range(len(mat)):
        low = 0
        high = len(mat[i])-1
        high1=high
        lb = 0
        while(low<=high):
          mid = (low+high)//2
          if (mat[i][mid]>=1):
            lb = mid
            high = mid-1
          else:low = mid+1
        if count < high1-high and high1-high>0:
            count = high1-high
            index = i
        elif(count==high-lb):
          if(index<i):
            index = i
      return index
  


       