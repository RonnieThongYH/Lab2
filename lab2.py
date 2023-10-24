def calc_average_temperature(num_list):
    average_temp = sum(num_list) / len(num_list)
    return average_temp
def calc_min_max_temperature(num_list):
    min_temp = min(num_list)
    max_temp = max(num_list)
    return min_temp, max_temp

def display_main_menu():
    print("Enter some numbers seperated by commas (eg. 5, 67, 32)")

def get_user_input():
    user_input = input()
    input_list = user_input.split(",")
    float_list = [float(item) for item in input_list]
    return float_list

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average_num_list = calc_average_temperature(num_list)
    min_max_num_list = calc_min_max_temperature(num_list)
    print(num_list)
    print(average_num_list)
    print(min_max_num_list)

if __name__ == "__main__":
    main()