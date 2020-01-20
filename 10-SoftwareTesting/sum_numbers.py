# Sumuje liczby naturalne parzyste z przedziału <from_n,to_n>
def sum_even(from_m,to_n):
    if type(from_m) == str or type(to_n) == str:
        return -1
    sum = 0
    if from_m < 0:
        return -1
    for i in range(from_m,to_n+1):
        if i%2 == 0: # liczba parzysta
            sum += i
    return sum

def main():
    m = 1
    n = 5
    print(f"Suma liczb naturalnych parzystych z przedziału <{m},{n}> wynosi {sum_even(1,5)}")

if __name__ == "__main__":
    main()