def isPositiveInt(s):
    try:
        return int(s) >= 0
    except ValueError:
        return False
