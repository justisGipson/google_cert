import time

initial_Time = time.time()

# Program to test follows
x, y = 5, 6
z = x + y

# Program to test ending
ending_Time = time.time()

Time_lapsed_in_Micro_sec = (ending_Time - initial_Time) * (10 ** 6)

print(f" Time lapsed in micro_seconds: {Time_lapsed_in_Micro_sec} ms")
