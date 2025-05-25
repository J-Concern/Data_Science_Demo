import pandas as pd
import re
## Personal Util Library

#testdata
dataset= ['a10','b20','c30','20']
df = pd.DataFrame(dataset)

#Useful letter map for letter to num operations
letter_map = {chr(ord('A') + i): i + 1 for i in range(26)} 

# A function that takes arr of str, iterates and converts letters to float,
# specifically takes first letter, if data then zero.
def first_letter_to_num(strings, *, base=1000):
    results = []
    for s in strings:
        s = str(s).strip()
        letter, digits = s[0], s[1:]
        if s is None:
            results.append(0.0)
            continue
        s = str(s).strip()
        if s[0].isalpha():
            a = letter_map.get(letter.upper(),0)  # gets num for letter map
            b = float(digits) if digits and digits.isdigit() else 0  #gets num for digits
            results.append(float(a * base + b))
        else:
            b = float(digits) if digits and digits.isdigit() else 0
            results.append(float(s))
    return results

def strip_all_alpha(strings):
    result = []
    for s in strings:
        s = re.sub(r"[^0-9]", '', s)
        result.append(s)
    return result

# A function to take a column in pd, convert to array, then overwrite column.
def edit_pd_column(df, column_name):
    strings = df[column_name]
    results = first_letter_to_num(strings, base=1000)
    df[column_name] = results
    return df[column_name]
