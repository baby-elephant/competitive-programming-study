Q = int(input())

# "("のときに+1, ")"のときに-1される
# negarive_indexがNoneのときに0ならYes,それ以外ならNo
counter = 0
# -1になった時のindex
negative_index = None
# 現在の文字リストを保持
stack = []
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        stack.append(query[1])
        if query[1] == "(":
            counter += 1
        elif query[1] == ")":
            counter -= 1
        if query[1] == ")":
            if counter == -1:
                # -1になった瞬間だけnegative_indexで記憶する
                negative_index = len(stack) - 1
    elif query[0] == "2":
        letter = stack.pop()
        # pop直後に必ず実行
        if negative_index is not None and len(stack) <= negative_index:
            negative_index = None

        if letter == "(":
            counter -= 1
        elif letter == ")":
            counter += 1
            # if len(stack) == negative_index:
            #     negative_index = None
    
    # 返す条件を指定していく
    if negative_index is None and counter == 0:
        print("Yes")
    else:
        print("No")


