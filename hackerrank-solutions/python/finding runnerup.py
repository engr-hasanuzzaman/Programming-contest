# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
#  You are given  scores. 
# Store them in a list and find the score of the runner-up.
# sample input 2 3 6 6 5 ans: 5 as it is 2nd biggest number

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
   
    def runner_up(arr):
      current_max = arr[0]
      i = 0
      ans = None
      while(i < len(arr)):
        j = 0
        while j < len(arr) - 1 - i:
          if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
          j += 1
          
        if(i > 0 and arr[j] != arr[j+1]):
          return arr[j]
        i += 1
    print(runner_up(list(arr)))