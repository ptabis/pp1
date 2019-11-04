def rysuj():
    langs = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
    vals = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]
    for i in range(0, len(langs)):
        print("{}:".format(langs[i]), end=" ")
        for _ in range(0, vals[i]):
            print('#', end="")
        print()
rysuj()