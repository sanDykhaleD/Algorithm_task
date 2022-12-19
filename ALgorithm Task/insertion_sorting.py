class sorting:
    arr = list(map(int, input("elements of array:-").strip().split()))
    def insertion_sort(self,arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
sorting1=sorting()
sorting1.insertion_sort(sorting.arr)
print(sorting.arr)
