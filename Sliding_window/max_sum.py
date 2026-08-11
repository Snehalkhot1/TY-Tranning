def sliding_window(users, days):
    window_sum = sum(users[:days])
    max_sum = window_sum

    # Slide the window
    for i in range(1, len(users) - days + 1):
        window_sum = window_sum - users[i - 1] + users[i + days - 1]

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum
users = [100, 48, 87, 52, 67, 80, 90]
days = 3
max_sum = sliding_window(users, days)

print("Maximum sum of sub-array:", max_sum)