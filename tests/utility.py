"""utility functions for tests"""
import inspect
import colorama

colorama.init(autoreset=True)

def get_function_name(_function):
    """return the full module path for a function"""
    return inspect.getmodule(_function).__name__ + "." + _function.__name__

def get_function_args(_function):
    """return the names of the arguments of a function"""
    return _function.__code__.co_varnames[:_function.__code__.co_argcount]

def compare_distributions(expected_function, observed_function, arguments, precision=10):
    """
    compare the output of the expected and observed functions
    print the function name and arguments
    """
    output_color = colorama.Fore.GREEN

    Ei = float(expected_function(*arguments))
    Oi = float(observed_function(*arguments))
    str_Ei = str(Ei)[:precision]
    str_Oi = str(Oi)[:precision]

    if str_Ei != str_Oi:
        print(get_function_name(observed_function))

        for name, value in zip(get_function_args(observed_function), arguments):
            print(f"{name}: {value}")

        print(f"{output_color}Ei: {Ei}")
        print(f"{output_color}Oi: {Oi}")
