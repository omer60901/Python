def secondLargest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort()
    return unique_numbers[-2]

def Rectangle(height,width):
    return (height*width)


def main():
    my_list = [10, 20, 4, 45, 99, 99, 4]
    print("The second largest number is:")
    print(secondLargest(my_list))
    print(Rectangle(10,10))


def test_second_largest():
    assert secondLargest([1, 2, 3, 4]) == 3
    assert secondLargest([10, 10, 5, 3]) == 5
    assert secondLargest([7]) is None


test_second_largest()
if __name__ == "__main__":
    main()
