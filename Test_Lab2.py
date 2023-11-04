import lab2  # Import the module you want to test

def test_calc_average_temperature():
    num_list = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert lab2.calc_average_temperature(num_list) == 3.0

def test_calc_min_max_temperature():
    num_list = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert lab2.calc_min_max_temperature(num_list) == (1.0, 5.0)

def test_sort_temperature():
    num_list = [5.0, 4.0, 3.0, 2.0, 1.0]
    sorted_list = lab2.sort_temperature(num_list)
    assert sorted_list == [1.0, 2.0, 3.0, 4.0, 5.0]

def test_calc_median_temperature():
    num_list = [15.0, 20.0, 25.0, 30.0, 35.0]
    assert lab2.calc_median_temperature(num_list) == 25.0

# Add more test cases for different functions as needed

if __name__ == "__main__":
    main()