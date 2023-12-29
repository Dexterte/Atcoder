import itertools

n, q = map(int, input().split())
s = [input().split() for _ in range(q)]
follow_relation = [['N' for _ in range(n)] for _ in range(n)]


def _get_followings(target: int) -> list:
    """
    フォローしているユーザを取得
    :param target:
    :return:
    """
    followings = []
    for j in range(n):
        if follow_relation[target][j] == 'Y':
            followings.append(j)
    return followings


def _get_followers(target: int) -> list:
    """
    フォロワーを取得
    :param target:
    :return:
    """
    followers = []
    for i in range(n):
        if follow_relation[i][target] == 'Y':
            followers.append(i)
    return followers


for i in range(q):
    if s[i][0] == '1':
        user = int(s[i][1]) - 1
        b = int(s[i][2]) - 1
        follow_relation[user][b] = 'Y'
    elif s[i][0] == '2':
        user = int(s[i][1]) - 1
        followers = _get_followers(user)
        for follower in followers:
            follow_relation[user][follower] = 'Y'
    elif s[i][0] == '3':
        user = int(s[i][1]) - 1
        followings = _get_followings(user)
        followings_of_followings = []
        for follower in followings:
            followings_of_followings.append(_get_followings(follower))
        # 1次元配列に変換
        followings_of_followings = list(set(itertools.chain.from_iterable(followings_of_followings)))
        for following in followings_of_followings:
            if following == user:
                continue
            follow_relation[user][following] = 'Y'

for i in range(n):
    ans = ""
    for j in range(n):
        ans += follow_relation[i][j]
    print(ans)
