def calc_average_temperature(num_list):
    average_temp = sum(num_list) / len(num_list)
    return average_temp
def calc_min_max_temperature(num_list):
    min_temp = min(num_list)
    max_temp = max(num_list)
    return min_temp, max_temp

def sort_temperature(num_list):
    num_list.sort()
    return num_list

def display_main_menu():
    print("Enter some numbers seperated by commas (eg. 5, 67, 32)")

def get_user_input():
    user_input = input()
    input_list = user_input.split(",")
    float_list = [float(item) for item in input_list]
    return float_list

def calc_median_temperature(num_list):
    n = len(num_list)
    if n % 2 == 1:
        # If the number of elements is odd, return the middle element
        median = num_list[n // 2]
    else:
        # If the number of elements is even, return the average of the two middle elements
        middle1 = num_list[n // 2 - 1]
        middle2 = num_list[n // 2]
        median = (middle1 + middle2) / 2

    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average_num_list = calc_average_temperature(num_list)
    min_max_num_list = calc_min_max_temperature(num_list)
    sorted_list_temp = sort_temperature(num_list)
    median = calc_median_temperature(num_list)
    print("Number List: ", num_list)
    print("Average Number: ", average_num_list)
    print("Minimum & Maximum: ", min_max_num_list)
    print("Sorted List: ", sorted_list_temp)
    print("Median: ", median)

if __name__ == "__main__":
    main()