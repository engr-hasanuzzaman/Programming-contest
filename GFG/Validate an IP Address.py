def isValid(s):
    segments = s.split(".")
    if len(segments) != 4:
        return

    for segment in segments:
        if len(segment) == 0:
            return False

        if has_leading_zero(segment):
            return False

        try:
            num = int(segment)
            if num < 0 or num > 255:
                return False
        except:
            return False

    return True


def has_leading_zero(text):
    if text == '0':
        return False

    return text[0] == '0'
