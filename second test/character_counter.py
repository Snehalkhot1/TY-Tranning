def count_occurrences(s, target):
    count = 0

    for ch in s:
        if ch == target:
            count += 1

    return count


if __name__ == "__main__":
    text = input().strip()
    target = input().strip()
    print(count_occurrences(text, target))