from tkinter import *

class PropertyAnalysis:
    def __init__(self) -> None:
        window = Tk() #create window
        window.title("Property Analysis: assumption of 20% down, 30 year loan term, 10% vacancy and 10% for property management") #set title
        window.geometry("750x300")

        # image = PhotoImage(file="photo.png")
        # label = Label(window, image = image)
        # label.pack()
        
        Label(window,text = "Mortgage").grid(row = 3, column = 1, sticky = W)
        Label(window,text = "Interest Rate").grid(row = 4, column = 1, sticky = W)
        Label(window,text = "Tax and insurance").grid(row = 5, column = 1, sticky = W)
        Label(window,text = "HOA").grid(row = 6, column = 1, sticky = W)
        Label(window,text = "Rent").grid(row = 7, column = 1, sticky = W)
        Label(window,text = "Closing Cost").grid(row = 8, column = 1, sticky = W)

        Label(window,text="Monthly Mortgage").grid(row = 16,column = 1, sticky = W)
        Label(window, text = "Net Cash Flow").grid (row = 17, column = 1, sticky = W)
        Label(window, text = "CashOnCash").grid(row = 18, column = 1, sticky = W)
        Label(window, text = "Cap Rate").grid(row = 19, column = 1, sticky = W)

        #for taking inputs
        self.mortgageVar = StringVar()
        Entry(window,textvariable = self.mortgageVar,justify = RIGHT).grid(row =3 , column = 2)
        self.interestrateVar = StringVar()
        Entry(window,textvariable = self.interestrateVar,justify = RIGHT).grid(row =4 , column = 2)
        self.taxandinsuranceVar = StringVar()
        Entry(window,textvariable = self.taxandinsuranceVar,justify = RIGHT).grid(row =5 , column = 2)
        self.hoaVar = StringVar()
        Entry(window,textvariable = self.hoaVar,justify = RIGHT).grid(row =6 , column = 2)
        self.rentVar = StringVar()
        Entry(window, textvariable = self.rentVar, justify = RIGHT).grid(row = 7, column = 2)
        self.closingcostVar = StringVar()
        Entry(window,textvariable = self.closingcostVar,justify = RIGHT).grid(row =8 , column = 2)

        self.monthlymortgageVar = StringVar()
        lblmonthlypayment = Label(window,textvariable = self.monthlymortgageVar).grid(row=16, column = 2, sticky = E)
        self.netcashflowVar = StringVar()
        lblcashflow = Label(window,textvariable = self.netcashflowVar).grid(row = 17, column = 2, sticky = E)
        self.cocVar = StringVar()
        lblcoc = Label(window, textvariable=self.cocVar).grid(row = 18, column = 2, sticky = E)
        self.caprateVar = StringVar()
        lblcaprate = Label(window, textvariable=self.caprateVar).grid(row = 19, column = 2 , sticky = E)

        #create button
        button = Button(window,text = "Compute Analysis", command = self.ComputePayment).grid(row =10,column=2,sticky = E )


        window.mainloop()

    def ComputePayment(self):
        monthlypayment = self.getMonthlyMortgage(
                                            float(self.mortgageVar.get()),
                                            float(self.interestrateVar.get())/1200
                                            )
       
        cashflow = self.getNet_cash_flow(
                                        float(self.rentVar.get()),
                                        float(self.taxandinsuranceVar.get()),
                                        float(self.hoaVar.get()),
                                        monthlypayment)
        annual_cashflow = cashflow * 12
        mortgage = float(self.mortgageVar.get())

        cashoncashReturn = self.getCashOnCash(
                                            float(self.closingcostVar.get()),
                                            annual_cashflow,
                                            mortgage
                                             )

        cap_rate = self.getCapRate(
                                cashflow,
                                monthlypayment,
                                mortgage
        )

        self.monthlymortgageVar.set(format(monthlypayment,'10.2f'))
        self.netcashflowVar.set(cashflow)
        self.cocVar.set(cashoncashReturn)
        self.caprateVar.set(cap_rate)

       

    def getMonthlyMortgage(self, mortgage, monthlyInterestRate):
            # compute the monthly payment.
            numberOfYears = 30
            monthlyPayment = mortgage * monthlyInterestRate / (1
            - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
            return monthlyPayment 
       

    def getNet_cash_flow(self,rent,taxandinsurance, hoa,monthly_mortgage):
        vacancy = 0.10
        property_management = 0.10
        Expenses = monthly_mortgage + (taxandinsurance/12) + hoa + (vacancy *rent) + (property_management *rent)
        ncf = rent - Expenses
        return  (round(ncf,2))

    def getCashOnCash(self, closing, annualcashflow, mortgage):
        down_payment = 0.20 * mortgage
        cash_invested = (down_payment + closing)
        coc = (annualcashflow/cash_invested)*100
        return (round(coc,2) )

    def getCapRate(self, cashflow,monthly_mortgage, mortgage):
        Cap_rate = (12*(cashflow + monthly_mortgage) / mortgage) *100 
        return (round(Cap_rate,2))







PropertyAnalysis()





