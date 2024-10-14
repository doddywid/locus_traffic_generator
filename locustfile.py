from locust import HttpUser, between, task

import time

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def arcadia_finance_traffic(self):
        #homepage
        self.client.get("/")
        time.sleep(1)
        #login page
        self.client.get("/trading/login.php")
        time.sleep(1)
        #auth login
        self.client.post("/trading/auth.php", { 'username': 'username', 'password': 'yoursecret' })
        #buy f5 stock
        self.client.post("/trading/rest/buy_stocks.php", json={"trans_value":165,"qty":5,"company":"FFIV","action":"buy","stock_price":165})
        #sell f5 stock
        self.client.post("/trading/rest/sell_stocks.php", json={"trans_value":165,"qty":4,"company":"FFIV","action":"sell","stock_price":165})
        #buy microsoft stock
        self.client.post("/trading/rest/buy_stocks.php", json={"trans_value":106,"qty":10,"company":"MSFT","action":"buy","stock_price":106})
        #sell microsoft stock
        self.client.post("/trading/rest/sell_stocks.php", json={"trans_value":106,"qty":8,"company":"MSFT","action":"sell","stock_price":106})
        #buy amazon stock
        self.client.post("/trading/rest/buy_stocks.php", json={"trans_value":1590,"qty":5,"company":"AMZN","action":"buy","stock_price":1590})
        #sell amazon stock
        self.client.post("/trading/rest/sell_stocks.php", json={"trans_value":6360,"qty":4,"company":"AMZN","action":"sell","stock_price":1590})
        #buy google stock
        self.client.post("/trading/rest/buy_stocks.php", json={"trans_value":4204,"qty":4,"company":"GOOGL","action":"buy","stock_price":1051})
        #sell google stock
        self.client.post("/trading/rest/sell_stocks.php", json={"trans_value":3153,"qty":3,"company":"GOOGL","action":"sell","stock_price":1051})
        #referral 1
        self.client.get("/trading/reference.php?bank_id=5473893784863&user_name=phillipe&email=d.widanto@f5.com")
        #referral 2
        self.client.get("/trading/reference.php?bank_id=5473893784863&user_name=phillipe&email=doddy.widanto@gmail.com")
        #money transfer vincent
        self.client.post("/api/rest/execute_money_transfer.php", json={"amount":"100","account":"2075894","currency":"EUR","friend":"Vincent"})
        #money transfer bart
        self.client.post("/api/rest/execute_money_transfer.php", json={"amount":"150","account":"2075894","currency":"EUR","friend":"Bart"})
        #money transfer or
        self.client.post("/api/rest/execute_money_transfer.php", json={"amount":"200","account":"7593494","currency":"GBP","friend":"Or"})
        #money transfer sven
        self.client.post("/api/rest/execute_money_transfer.php", json={"amount":"75","account":"7593494","currency":"GBP","friend":"Sven"})
        #money transfer alfredo
        self.client.post("/api/rest/execute_money_transfer.php", json={"amount":"500","account":"1235234","currency":"EUR","friend":"Alfredo"})
        #file table
        self.client.get("/trading/file_tables.php")
        #upload file 1
        file1 = open('/mnt/locust/tax_document_1.txt', 'rb')
        self.client.post("/trading/upload_file.php", files={'fileToUpload': file1 })
        #upload file 2
        file1 = open('/mnt/locust/tax_document_2.txt', 'rb')
        self.client.post("/trading/upload_file.php", files={'fileToUpload': file1 })
        #reset app data
        self.client.post("/trading/reset_all.php", { 'user': 'admin', 'pass': 'secret', 'submitLogin': 'Login' })
