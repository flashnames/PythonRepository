def binary_array_to_number(arr):
      # your code
      for i in range(len(arr)):
            num=str(arr[i])
            arr[i]=num
      arr="".join(arr)
      num=int(arr,10)
      return num



if __name__=="__main__":
      print(binary_array_to_number( [1, 1, 0, 1, 1, 0, 1, 1, 1, 1]))