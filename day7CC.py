"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count
the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed.
"""

def decodeNumber(s):
    if not s:
        return 0

    dp = [ 0 for _ in range(len(s)+1)]
    # dp = [0,0,0]
    dp[0] = 1
    
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(1,len(s)):
        if s[i] != '0':
            dp[i+1] += dp[i]

        if s[i-1] != 0 and 10 <= int(s[i-1:i+1]) <= 26:
            dp[i+1] += dp[i-1]

    return dp[len(s)]
