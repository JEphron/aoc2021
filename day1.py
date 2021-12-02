def windowed(data):
    ret = []
    for i in range(len(data)):
        if i + 2 < len(data):
            ret.append([data[i], data[i + 1], data[i + 2]])
    return ret


def do_it(nums):
    last = nums[0]
    increases = 0
    for num in nums:
        if num > last:
            increases += 1
        last = num
    return increases


if __name__ == "__main__":
    data = open("day1.txt").read()
    nums = [int(x) for x in data.split() if x]
    print(do_it(nums))
    print(do_it([sum(x) for x in windowed(nums)]))
