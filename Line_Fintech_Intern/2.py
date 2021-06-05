def solution(endingTime, jobs):
    answer = []

    # 시스템 시간
    now = 0
    for i in jobs:
        id, input_time, valid_time, work_time = i
        # 시스템 시간이 input 시간 보다 작다 -> 그동안 대기 중이여서 input 타임으로 갱신
        if now < input_time:
            now = input_time
        end_time = now + work_time

        # 끝나는 시간이 종료 시간보다 크면
        if end_time > endingTime:
            break

        # job이 출력되는 것은 현재 시간 및 끝나는 시간이 valid 이전이여야 한다.
        if end_time <= valid_time:
            answer.append(id)
            now = end_time
        # 만약 이후면 시스템 시간을 끝나는 시간
        elif valid_time < end_time:
            now = end_time

    return answer

end = 40
jobs = [[1, 10, 20, 3], [2, 14, 20, 9], [3, 18, 24, 2], [4, 25, 40, 5], [5, 28, 40, 1]]
assert [1, 4, 5] == solution(end, jobs)



"""
var GetCurrentTime() // 시스템의 현재 시간을 초 단위로 출력한다.
class Job {
    var Work() // 임의의 시간 초가 필요한 동작을 수행하며, 동작이 완료되기 전까지 소요된 작업 시간을 알 수 없다.
}

class Queue {
    void Push(Job) // Queue에 Job을 입력한다.
    Job Pop() // Queue에서 Job을 출력하면서 해당 Job은 삭제한다. 비어 있다면 nothing을 반환한다.
}

class RealtimeJob : Job {
    var validTime // 시스템 내에서 Job이 유효한 시간
    var result = nothing
    var Work() {
        if(result is nothing)
            result = Job.Work()
        return result
    }
}

class RealtimeQueue : Queue {
    void Push(RealtimeJob job) {
        if(job.validTime < GetCurrentTime()) valid 시간이 현재 시작보다 작으면 return
            return
        Queue.Push(job)
    }
    var Pop() {
        while ((var job = Queue.Pop()) is not nothing) {
            if(job.validTime < GetCurrentTime()) valid 시간이 현재보다 작다 -> pass
                continue
            job.Work()
            if(job.validTime >= GetCurrentTime()) valid 시간이 현재보다 크다 -> return job
                return job
        }
        return nothing
    }
}
"""