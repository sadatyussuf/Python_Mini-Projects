import time


def getCurrentTime():
    seconds = time.time()
    local_time = time.localtime(seconds)
    time_str = time.strftime('%Y-%m-%d, %H:%M:%S', local_time)
    print(time_str)
    # return local_time


getCurrentTime()
