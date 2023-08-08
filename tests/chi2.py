import random
import colorama
from scipy.stats import chi2 as _chi2
from promethium import chi2

colorama.init(autoreset=True)

def test_chi2_pdf():
    for _ in range(1000):
        x = random.uniform(0, 1.0)
        df = random.randint(1, 50)

        # expected result from scipy library
        Ei = _chi2.pdf(x, df)
        # observed result from promethium library
        Oi = chi2.pdf(x, df)

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

def test_chi2_cdf():
    for _ in range(1000):
        x = random.uniform(0, 1.0)
        df = random.randint(1, 50)

        # expected result from scipy library
        Ei = _chi2.cdf(x, df)
        # observed result from promethium library
        Oi = chi2.cdf(x, df)

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

test_chi2_pdf()
test_chi2_cdf()

