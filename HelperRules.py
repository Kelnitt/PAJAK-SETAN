from mlxtend.preprocessing import TransactionEncoder

from mlxtend.frequent_patterns import apriori, association_rules

import pandas, warnings

warnings.filterwarnings("ignore")

url = "/home/kelv/Music/Marta/Marta/static/AprioriFinal.csv"

usecols = ["TransactionID", "ItemCode"]

def OpenTable(url, **cols):
  """
  Open Pandas Table
  """
  table = pandas.read_table(url, sep=",", **cols)
  return table

def TraTable(table, columns):
  """
  Perform Transaction Encoder, Table Fit Transform on Encoder Table
  """
  transactions = table[columns].str.split(',').apply(lambda x: [item.strip() for item in x]).tolist()
  tranencoder = TransactionEncoder()
  te_array = tranencoder.fit(transactions).transform(transactions)
  encoder_table = pandas.DataFrame(te_array, columns=tranencoder.columns_)
  return encoder_table

def Helper(table, itemsets, sorting):
  for item in itemsets:
    table[item] = table[item].apply(lambda val : ", ".join(list(val)))
  table = table.round(3)
  table = table.sort_values(sorting, ascending=False)
  return table

def GetSingularTable(itemsets):
  singular = itemsets[itemsets['itemsets'].apply(lambda x: len(x) == 1)]
  singular = Helper(singular, ["itemsets"], "support")
  return singular

def GetDoubleRule(itemsets):
  double = itemsets[itemsets['itemsets'].apply(lambda x: len(x) == 2)]
  double = Helper(double, ["itemsets"], "support")
  return double

def GetApriori(itemsets, confidence):
  rules = association_rules(itemsets, metric="confidence", min_threshold=confidence, num_itemsets=1)
  rules = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
  rules = Helper(rules, ['antecedents', 'consequents'], "confidence")
  return rules

def HelperGetRules(support, confidence):
  encoder_table = TraTable(OpenTable(url, usecols=usecols), "ItemCode")
  itemsets = apriori(encoder_table, min_support=support, use_colnames=True)
  itemsets = itemsets.reindex(columns=itemsets.columns[::-1])
  singular = GetSingularTable(itemsets)
  double = GetDoubleRule(itemsets)
  rules = GetApriori(itemsets, confidence)
  return singular, double, rules