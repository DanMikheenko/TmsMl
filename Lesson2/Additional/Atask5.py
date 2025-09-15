def is_threat_from_queen(a, b, c, d):
    result = False
    if a == c or b == d or abs(a - c) == abs(b - d):
        result = True
    return result

def is_threat_from_knight(a, b, c, d):
    return (abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2)

print(is_threat_from_queen(1,2,3,4))
print(is_threat_from_queen(4,4,6,5))

print(is_threat_from_knight(1,2,3,4))
print(is_threat_from_knight(4,4,6,5))