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
    print("Second largest number:")
    print(secondLargest(my_list))
    print(Rectangle(10,10))



if __name__ == "__main__":
    main()
