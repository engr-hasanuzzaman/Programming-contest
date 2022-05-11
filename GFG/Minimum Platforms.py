# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1/?page=1&company[]=Amazon&curated[]=1&sortBy=submissions

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        arr_idx = 0
        dep_idx = 0
        max_platform = 1
        cur_req_platform = 0
        
        for _ in range(2*n):
            if arr_idx >= n:
                break

            if arr_idx < n and arr[arr_idx] <= dep[dep_idx]:
                cur_req_platform += 1
                arr_idx += 1
            else:
                cur_req_platform -= 1
                dep_idx += 1
            max_platform = max(max_platform, cur_req_platform)
        return max_platform