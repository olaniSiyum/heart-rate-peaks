def is_peak_at(data, i, w):
    # replace this with your code
    if i < w or i >= len(data) - w:
        return False
    if not all(data[i] > data[j] for j in range(i - w, i)):
        return False
    if not all(data[i] >= data[j] for j in range(i + 1, i + w + 1)):
        return False
    return True


def count_laps(data, w):
    peak_count = 0
    for i in range(len(data)):
        if is_peak_at(data, i, w):
            peak_count = peak_count + 1
            pass
        pass
    return peak_count