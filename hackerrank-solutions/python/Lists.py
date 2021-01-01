if __name__ == '__main__':
    def string_to_int(arr):
        return [int(n) for n in arr]
    
    N = int(input())
    arr = []
    for _ in range(N):
        r_input = input()
        operation, *data = r_input.split(" ")
        if operation == 'insert':
            arr.insert(*string_to_int(data))
        elif operation == 'print':
            print(arr)
        elif operation == 'remove':
            arr.remove(*string_to_int(data))
        elif operation == 'append':
            arr.append(*string_to_int(data))
        elif operation == 'sort':
            arr.sort()
        elif operation == 'pop':
            arr.pop()
        elif operation == 'reverse':
            arr.reverse()
    
    
