import random

def map_avgnum_to_range(avgnum):
    # Map the range 0.75 to 1.25 to the range 1 to 100
    return round(((avgnum - 0.75) / (1.25 - 0.75)) * 99 + 1)

def generate_random_avgnum():
    avgnum = round(random.uniform(0.75, 1.25), 2)
    mapped_value = map_avgnum_to_range(avgnum)
    return int(mapped_value)


