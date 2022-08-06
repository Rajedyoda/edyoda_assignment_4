def square_num(no1):
  return no1 * no1
nums = list(int(i) for i in input("Enter the element of the List to Square it using map fuction : "))
print("\nOriginal List: ",nums)
result_Square = list(map(square_num, nums))
print("\nSquare the elements of the said list using map():")
print(result_Square)
