class ScoreError(Exception):
    pass


def check_score(s):
    if not 0<= s <= 100:
        raise ScoreError(f"分数必须在0-100之间，收到{s}")
    return s

for v in (85,120):
    try:
        print("  通过：",check_score(v))
    except ScoreError as e:
        print("  拒绝：",e)