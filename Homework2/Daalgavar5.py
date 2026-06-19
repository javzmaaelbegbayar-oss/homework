import pandas as pd
dict_1={'name': ['Bat'],
        'gender': ['male'],
        'salary': [2000000],
        'birth_date': ['2002-01-01']}
dict_2={'name': ['Dorj'],
        'gender': ['male'],
        'salary': [4000000],
        'birth_date': ['1989-07-23']}
dict_3={'name': ['Tsetseg'],
        'gender': ['female'],
        'salary': [2500000],
        'birth_date': ['1995-03-11']}
dict_4={'name': ['Naidan'],
        'gender': ['male'],
        'salary': [3000000],
        'birth_date': ['2001-11-15']}
dict_5={'name': ['Hulan'],
        'gender': ['female'],
        'salary': [6000000],
        'birth_date': ['1998-09-29']}
combined_dict = [dict_1, dict_2, dict_3, dict_4, dict_5]
df = pd.DataFrame(combined_dict)
print(df)