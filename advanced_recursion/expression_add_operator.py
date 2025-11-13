class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def dfs(i,path,value,prev):
            if i ==len(num):
                if value == target:
                    result.append(path)
            
            for j in range(i,len(num)):
                if j>i and num[i] == '0':
                    break
                
                cur_str = num[i:j+1]
                cur = int(cur_str)

                if i ==0:
                    dfs(j+1,cur_str,cur,cur)
                else:
                    dfs(j+1,path+'+'+cur_str,value+cur,cur)
                    dfs(j+1,path+'-'+cur_str,value-cur,-cur)
                    dfs(j+1,path+'*'+cur_str,value-prev+prev*cur,prev*cur)
        dfs(0,"",0,0)
        return result



        