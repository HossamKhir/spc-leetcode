def romanToInt(s: str) -> int:
    table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    special = {"I", "X", "C"}
    length = len(s)
    i = 0
    res = 0
    while i < length:
        default = table[s[i]]
        if s[i] in special:
            numeral = s[i : i + 2]
            result = table.get(numeral, 0)
            if result:
                res += result
                i += 2
                continue
        res += default
        i += 1
    return res


if __name__ == "__main__":
    # s = "III" # 3
    # s = "LVIII" # 58
    s = "MCMXCIV"  # 1994
    print(romanToInt(s))
