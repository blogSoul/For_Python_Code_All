resultDf = {'antecedents' : [], 'consequents' : [], 'antecedents_keywordsPart' : [] , 'consequents_keywordsPart' : [], 'lift' : [], 'conviction' : []}
def checkWord(word):
    for key in keywords.keys():
        for checkkey in keywords[key]:
            if word == checkkey:
                return True
    return False

def checkkeywordsPart(word):
    for key in keywords.keys():
        for checkkey in keywords[key]:
            if word == checkkey:
                return key
    return False

for RowIndex in range(0, len(association_dataframe)):
    if checkWord(association_dataframe["antecedents"][RowIndex]) or checkWord(association_dataframe["consequents"][RowIndex]):
        resultDf["antecedents"].append(association_dataframe["antecedents"][RowIndex])
        resultDf["consequents"].append(association_dataframe["consequents"][RowIndex])
        resultDf["antecedents_keywordsPart"].append(checkkeywordsPart(association_dataframe["antecedents"][RowIndex]))
        resultDf["consequents_keywordsPart"].append(checkkeywordsPart(association_dataframe["consequents"][RowIndex]))
        resultDf["lift"].append(association_dataframe["lift"][RowIndex])
        resultDf["conviction"].append(association_dataframe["conviction"][RowIndex])

DF_result = pd.DataFrame(resultDf)
display(DF_result)
