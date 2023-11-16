def title_decorator(function): #mengonversi hasil dari fungsi asli ke huruf kapital
    def wrapper():
        func = function()
        make_title = func.title()
        print(make_title + " - Data is converted to title case")
        return make_title
    return wrapper

def split_string(function): #membagi hasil dari fungsi asli menjadi daftar kata
    def wrapper():
        func = function()
        splitted_string = func.split()
        print(str(splitted_string) + " " + " - Then data is splitted")
        return splitted_string
    return wrapper

@split_string
@title_decorator
def say_hi():
    return 'hello there'

result = say_hi()
print(result)