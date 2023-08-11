import random
import colorama
from scipy.stats import chi2 as _chi2
from promethium import chi2

colorama.init(autoreset=True)

def test_chi2(expected_function, observed_function):
    for _ in range(100):
        x = random.uniform(0, 1.0)
        df = random.randint(1, 100)

        # expected result from scipy library
        Ei = expected_function(x, df)
        # observed result from promethium library
        Oi = observed_function(x, df)

        # compare first 9 characters of both results
        rr = 10
        str_Ei = str(Ei)[:rr]
        str_Oi = str(Oi)[:rr]
        output_color = colorama.Fore.RED
        if str_Ei == str_Oi:
            output_color = colorama.Fore.GREEN

        print(
            f"x : {x}",
            f"df: {df}",
            output_color + f"Ei: {str_Ei}",
            output_color + f"Oi: {str_Oi}",
            sep="\n",
            end="\n\n"
        )

        assert str_Ei == str_Oi

if __name__ == '__main__':
    test_chi2(_chi2.pdf, chi2.pdf)
    test_chi2(_chi2.cdf, chi2.cdf)

