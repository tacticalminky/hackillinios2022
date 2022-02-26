import pandas as pd
import objects

final_dataframe_list = []

def makeJSONatFrame(totals, bin):
    data=pd.DataFrame([totals + [bin]], columns=["Plastic", "Paper", "Garbage", "Bin"])
    convert = data.to_json()
    print(convert)

def makeFinalJSON(input_list):
    data = pd.DataFrame(input_list, columns=["Plastic", "Paper", "Garbage", "Bin"])
    data.to_json("trash_data.json")