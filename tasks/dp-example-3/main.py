n = int(input())
nums_list = []   #入力された数字が入っている
for i in range(n):
    # list内包記述  []で処理された内容がリストとして返る
    nums_list.append([tok[0:1] for tok in input()])

first_letters = ["H","D","C","S",]
second_letters = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]

return_str = "Yes"

for nums in nums_list:

    if nums_list.count(nums) > 1:
        return_str = 'No'
        break

    first_count = 0
    second_count = 0
    for letter in first_letters:
        if nums[0] == letter:
            first_count += 1
    for letter in second_letters:
        if nums[1] == letter:
            second_count += 1
    if (first_count == 0 or second_count == 0):
        return_str = "No"
        break
    
print(return_str)
