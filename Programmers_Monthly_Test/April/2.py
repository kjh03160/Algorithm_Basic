def solution(s):
    answer = 0

    mapper = {"]": "[", "}": "{", ")": "("}

    for i in range(len(s)):
        stack = []
        k = s[i:] + s[:i]
        is_changed = False
        for j in k:
            if j in "{[(":
                stack.append(j)
                is_changed = True
            else:
                if not stack:
                    continue
                if stack[-1] == mapper[j]:
                    stack.pop()
        if not stack and is_changed:
            answer += 1
    return answer