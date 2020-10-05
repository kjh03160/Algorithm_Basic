import heapq

def Huffman(text_dict):
    H = []
    sort_dict = sorted(text_dict.items(),key=lambda x:x[1])
    for i in range(len(sort_dict)):
        heapq.heappush(H, (sort_dict[i][1], sort_dict[i][0]))
        while len(H) > 1:
            a = heapq.heappop(H)
            b = heapq.heappop(H)
            heapq.heappush(H, ((a[0] + b[0]), (a[1], b[1])))
    a = heapq.heappop(H)
    heapq.heappush(H, a[1])
    print(H)

text = {'a' : 43, 'b' : 13, 'c' : 12, 'd' : 16, 'e' : 9, 'f' : 7}
Huffman(text)