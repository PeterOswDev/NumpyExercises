import pandas as pd
print(pd.__version__)
import matplotlib.pyplot as plt

df = pd.read_csv("E:\Jezyki_programowania_ksiazki\Python\Pandas_Matplotlib\company_sales_data.csv")
print(df)
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
