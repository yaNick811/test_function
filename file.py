def test_function():
    inner_function = "Я в области видимости функции test_function"
    print(inner_function)


test_function()
inner_function()


# Второй вариант решения задачи.
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
inner_function()