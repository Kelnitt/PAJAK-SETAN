from flask import Flask, render_template, request

from HelperRules import OpenTable, HelperGetRules

import pandas, logging

app = Flask(__name__)

@app.route("/")
def MainRoute():
  """
  Main HTML File
  """
  title = "Main HTML File"
  return render_template("index.html", title=title)

@app.route("/GetTable", methods=["GET"])
def GetAllTable():
  """
  Get All Table Content
  """
  title = "Table Content"
  url = "/home/kelv/Music/Marta/Marta/static/AprioriFinal.csv"
  usecols = ["TransactionID", "ItemCode"]
  table = OpenTable(url=url, usecols=usecols)
  return render_template("tabel_barang.html", title=title, table=table)

@app.route("/AprioriLimit")
def GetSuCoFi():
  title = "Get Support & Confidence"
  return render_template("Apriori/support_limit.html", title=title)

@app.route("/GetRules", methods=["POST"])
def GetRules():
  # 0.05 | 0.3
  title = "Apriori Rules"
  logging.info(request.form)
  support = float(request.form["support"])
  confidence = float(request.form["confidence"])
  singular, double, rules = HelperGetRules(support, confidence)
  result = {"singular":singular, "double":double, "rules":rules, "supp":support, "confi":confidence}
  return render_template("Apriori/apriori_result.html", title=title, result=result)

if __name__ == '__main__':
  # Application Runner
  debug = True
  port = "5000"
  host = "127.0.0.1"
  app.run(debug=debug, host=host, port=port)