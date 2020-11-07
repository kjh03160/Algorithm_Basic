def solution(penter, pexit, pescape, data):
    answer = ''
    # penter 단위로 data 자를 준비
    data_slice = []
    for i in range(0, len(data), len(penter)):
        data_slice.append(data[i:i + len(penter)])  # penter 단위만큼 슬라이싱 해서 추가

    answer += penter  # 패킷 앞에 penter 문자 추가

    for i in range(len(data_slice)):
        if data_slice[i] in [penter, pexit, pescape]:  # 데이터가 겹치면
            answer += pescape  # pescape 먼저 추가
        answer += data_slice[i]  # 데이터 추가

    answer += pexit  # 마지막 pexit 추가

    return answer