import pandas as pd
import objects

def makeJSONatFrame(totals, bin):
    data=pd.DataFrame([totals + [bin]], columns=["Plastic", "Paper", "Garbage", "Bin"])
    convert = data.to_json()
    print(convert)
