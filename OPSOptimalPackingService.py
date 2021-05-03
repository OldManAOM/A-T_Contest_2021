
def main():
    filename = open("ops.txt")
    contents = filename.read()
    split = contents.split("\n")

    W = int(split[0])
    n = int(split[1])
    index = 2
    val = []
    wt = []
    ci = []

    while n + 1 >= index:

        n1 = int(split[index].split(" ")[1])
        n2 = int(split[index].split(" ")[2])
        ch = [str(s) for s in split[index] if s.isalpha()]
        ci.append(ch)
        val.append(n1)
        wt.append(n2)
        index += 1

    print("total value: " + str(value(W, wt, val, n)) + " total weight: " + str(weight(W, wt, val, n)))
    print(printknapSack(W, wt, val, n, ci))




def value(W, wt, val, n):

    if n == 0 or W == 0 :
        return 0
    if (wt[n-1] > W):
        return value(W, wt, val, n-1)
    else:
        return max(val[n-1] + value(W-wt[n-1], wt, val, n-1),
                   value(W, wt, val, n-1))

def weight(W, wt, val, n):

    if n == 0 or W == 0 :
        return 0
    if (wt[n-1] > W):
        return weight(W, wt, val, n-1)
    else:
        return max(wt[n-1] + weight(W-wt[n-1], wt, val, n-1),
                   weight(W, wt, val, n-1))
def printknapSack(W, wt, val, n, ci):
    answer = []
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    res = K[n][W]

    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            answer.append(ci[i - 1])
            res = res - val[i - 1]
            w = w - wt[i - 1]

    return answer

main()
