from tkinter import *
import requests
import json
import time
import io
import plotly.express as px
import math
import pandas as pd


class zillowAnalysis:
    def __init__(self) -> None:
        window = Tk()
        window.title("Property Analysis") #set title
        window.geometry("750x300")


        Label(window,text = "URL").grid(row = 1, column = 1, sticky = W)
        self.urlVar = StringVar()
        Entry(window,textvariable = self.urlVar,justify = RIGHT).grid(row =1 , column = 2)
      

       

        button = Button(window,text = "Extract data", command = self.Extract_data).grid(row =3,column=2,sticky = E)

        Label(window,text="Price").grid(row = 6,column = 1, sticky = W)
        Label(window, text = "HOA").grid(row = 7, column = 1, sticky = W)
        Label(window, text = "Tax and Insurance").grid(row = 8, column = 1, sticky = W)
        Label(window,text="Rent Estimate").grid(row = 9,column = 1, sticky = W)
        Label(window, text = "Closing Cost").grid (row = 10, column = 1, sticky = W)
        Label(window, text = "Interest Rate").grid(row = 11, column = 1, sticky = W)
        Label(window, text = "Down percent").grid(row = 12, column = 1, sticky = W)
        Label(window, text = "Loan Term").grid(row = 13, column = 1, sticky = W)
        Label(window, text = "Vacancy").grid(row = 14, column = 1, sticky = W)
        Label(window, text = "Management").grid(row = 15, column = 1, sticky = W)
        

        self.priceVar = StringVar()
        Entry(window,textvariable = self.priceVar,justify = RIGHT).grid(row=6, column = 2)
        self.hoaVar = StringVar()
        Entry(window,textvariable = self.hoaVar,justify = RIGHT).grid(row =7 , column = 2)
        self.taxandinsuranceVar = StringVar()
        Entry(window,textvariable = self.taxandinsuranceVar,justify = RIGHT).grid(row =8 , column = 2)
        self.rentVar = StringVar()
        Entry(window,textvariable = self.rentVar,justify = RIGHT).grid(row =9 , column = 2)
        self.closingcostVar = StringVar()
        Entry(window,textvariable = self.closingcostVar,justify = RIGHT).grid(row =10 , column = 2)
        self.rateVar = StringVar()
        Entry(window,textvariable = self.rateVar,justify = RIGHT).grid(row =11 , column = 2)
        self.downVar = StringVar()
        Entry(window,textvariable = self.downVar,justify = RIGHT).grid(row =12 , column = 2)
        self.termVar = StringVar()
        Entry(window,textvariable = self.termVar,justify = RIGHT).grid(row =13 , column = 2)
        self.vacancyVar = StringVar()
        Entry(window,textvariable = self.vacancyVar,justify = RIGHT).grid(row =14 , column = 2)
        self.managementVar = StringVar()
        Entry(window,textvariable = self.managementVar,justify = RIGHT).grid(row =15 , column = 2)

        button = Button(window,text = "Compute Analysis", command = self.Compute).grid(row =16,column=2,sticky = E)



        Label(window,text="Total Mortgage").grid(row = 7,column = 3, sticky = W)
        self.mortgageVar = StringVar()
        Entry(window,textvariable = self.mortgageVar,justify = RIGHT).grid(row =7 , column = 4)

        Label(window,text="Monthly Mortgage").grid(row = 7,column = 3, sticky = W)
        self.monthlyVar = StringVar()
        Entry(window,textvariable = self.monthlyVar,justify = RIGHT).grid(row =7 , column = 4)

        Label(window,text="Cash Flow").grid(row = 8,column = 3, sticky = W)
        self.netcashflowVar = StringVar()
        Entry(window,textvariable = self.netcashflowVar,justify = RIGHT).grid(row =8 , column = 4)

        Label(window,text="Cash on Cash").grid(row = 9,column = 3, sticky = W)
        self.cocVar = StringVar()
        Entry(window,textvariable = self.cocVar,justify = RIGHT).grid(row =9 , column = 4)

        Label(window,text="Cap Rate").grid(row = 10,column = 3, sticky = W)
        self.capVar = StringVar()
        Entry(window,textvariable = self.capVar,justify = RIGHT).grid(row =10 , column = 4)


        window.mainloop()



    def Extract_data(self):
        #get data first

        link_input = self.urlVar.get() #get the url input into the UI
        zpid = [x for x in link_input.split('/') if 'zpid' in x][0].split('_')[0] #parse out to isolate the Zpid from the url
        url = "https://zillow-com1.p.rapidapi.com/property"
        with io.open('api_key.txt') as f:
            api_key = f.read()                                                     #use api keys to access zilllow api


        querystring = {"zpid":zpid}                                                 #query based on the particular zpid number in the given url    

        headers = {
            "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com", 
            "X-RapidAPI-Key": api_key
        }

        # request data
        response = requests.request("GET", url, headers=headers, params=querystring)
         
        df =  pd.json_normalize(data=response.json())
        data= df[['price','monthlyHoaFee','annualHomeownersInsurance','resoFacts.taxAnnualAmount','rentZestimate','resoFacts.specialListingConditions','resoFacts.parkingFeatures','livingAreaValue','homeType','latitude','longitude','bedrooms','bathrooms']].copy()
        data = data.rename(columns = {'monthlyHoaFee': 'HOA', 'annualHomeownersInsurance': 'annualInsurance','resoFacts.taxAnnualAmount':'annualTax', 'resoFacts.specialListingConditions': 'Land Tenure','resoFacts.parkingFeatures': 'Parking'})

        price = float(data['price'].values)
        hoa = float(data['HOA'].values)
        TaxandInsurance = float(data['annualInsurance'].values) +float( data['annualTax'].values)
        rent = float(data['rentZestimate'].values)
        closing = 0.03 * price
     

        
        self.priceVar.set(price)
        self.hoaVar.set(hoa)
        self.taxandinsuranceVar.set(TaxandInsurance)
        self.rentVar.set(rent)
        self.closingcostVar.set(closing)
       
    def Compute(self):

        price = float(self.priceVar.get())
        down = float(self.downVar.get())
        down_payment = (down/100) * price
        mortgage = price - down_payment
        self.mortgageVar.set(mortgage)
        term = float(self.termVar.get())

        monthlypayment = self.getMonthlyMortgage(
                                            mortgage,
                                            float(self.rateVar.get())/1200,
                                            term
                                            )
       
        cashflow = self.getNet_cash_flow(
                                        float(self.rentVar.get()),
                                        float(self.taxandinsuranceVar.get()),
                                        float(self.hoaVar.get()),
                                        monthlypayment,
                                        float(self.vacancyVar.get()),
                                        float(self.managementVar.get()))
        
        annual_cashflow = cashflow * 12
        cashoncashReturn = self.getCashOnCash(
                                            float(self.closingcostVar.get()),
                                            annual_cashflow,
                                            down_payment
                                             )

        cap_rate = self.getCapRate(
                                cashflow,
                                monthlypayment,
                                price
        )


        self.monthlyVar.set(format(monthlypayment,'10.2f'))
        self.netcashflowVar.set(cashflow)
        self.cocVar.set(cashoncashReturn)
        self.capVar.set(cap_rate)


    def getMonthlyMortgage(self, mortgage, monthlyInterestRate,numberOfYears):
            # compute the monthly payment.
         
            monthlyPayment = mortgage * monthlyInterestRate / (1
            - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
            return monthlyPayment 
       

    def getNet_cash_flow(self,rent,taxandinsurance, hoa,monthly_mortgage,vacancy, property_management):
        Expenses = monthly_mortgage + (taxandinsurance/12) + hoa + (vacancy *rent) + (property_management *rent)
        ncf = rent - Expenses
        return  (round(ncf,2))

    def getCashOnCash(self, closing, annualcashflow, down_payment):
        cash_invested = (down_payment + closing)
        coc = (annualcashflow/cash_invested) *100
        return (round(coc,2) )

    def getCapRate(self, cashflow,monthly_mortgage, market_value):
        Cap_rate = (12*(cashflow + monthly_mortgage) / market_value) *100 
        return (round(Cap_rate,2))



    

zillowAnalysis()