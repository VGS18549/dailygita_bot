import pandas as pd
import random


def sample_responses(text):
        if text == "/vasudeva":
                df = pd.read_csv("bhagavad-gita.csv", index_col=0)
                num = random.randint(0, 699)
                output = "Sloka Number : {}\n{}\n\n{}".format(df.iloc[num, 0], df.iloc[num, 1], df.iloc[num, 2])
                return output
