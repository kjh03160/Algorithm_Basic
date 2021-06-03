from collections import defaultdict
class Node:
    def __init__(self, string):
        self.value = string
        self.child = {}
        self.length_counter = defaultdict(int)

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, value):
        head = self.head
        head.length_counter[len(value)] += 1
        for string in value:
            if string not in head.child:
                head.child[string] = Node(string)
            head = head.child[string]
            head.length_counter[len(value)] += 1


    def search(self, query):
        query_length = len(query)
        now = self.head

        for string in query:
            print(string)
            if string == "?":
                break
            if string in now.child:
                now = now.child[string]
            else:
                return 0
        return now.length_counter[query_length]


def solution(words, queries):
    answer = []
    trie = Trie()
    reverse_trie = Trie()
    for i in range(len(words)):
        trie.insert(words[i])
        reverse_trie.insert(words[i][::-1])

    dup_query_finder = {}

    for q in queries:
        result = 0
        if q in dup_query_finder:
            result = dup_query_finder[q]
        elif q.startswith("?"):
            result = reverse_trie.search(q[::-1])
        else:
            result = trie.search(q)
        answer.append(result)
        dup_query_finder[q] = result

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
query = ["?????", "????o", "fr???", "fro???", "pro?"]
print(solution(words, query))