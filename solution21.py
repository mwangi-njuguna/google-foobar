def solution(l):
    return sorted(l, key=lambda v: list(map(int, v.split('.'))))


if __name__ == "__main__":
    result = solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
    print(result)
    # should return ['1.0', '1.0.2', '1.0.12', '1.1.2', '1.3.3']
