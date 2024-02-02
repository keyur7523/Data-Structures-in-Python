def pallidrome(s):
    return True if s == s[::-1] else False

print(pallidrome('grammarg'))