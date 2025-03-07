import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv(r"github\prepro\data\Gold Price (2013-2023).csv")
df2 = pd.read_csv(r"github\prepro\data\BrentOilPrices2.csv")

# Chuyển đổi cột "Date" sang kiểu datetime
df["Date"] = pd.to_datetime(df["Date"])
df2["Date"] = pd.to_datetime(df2["Date"])

# Đặt Date làm index
df.set_index("Date", inplace=True)
df2.set_index("Date", inplace=True)

# Tạo dãy ngày đầy đủ từ min đến max
full_date_range = pd.date_range(start=min(df.index.min(), df2.index.min()),
                                end=max(df.index.max(), df2.index.max()),
                                freq="D")

# Reindex để lấp đầy các ngày bị thiếu, dùng forward fill (ffill)
df = df.reindex(full_date_range, method="ffill")
df2 = df2.reindex(full_date_range, method="ffill")

# Đổi lại tên index thành 'Date'
df.index.name = "Date"
df2.index.name = "Date"

# Chuyển đổi cột "Price" từ chuỗi thành số (xử lý lỗi dữ liệu nếu có)
df["Price"] = df["Price"].astype(str).str.replace(",", "", regex=True).astype(float)
df2["Price"] = df2["Price"].astype(float)  # df2 thường đã ở dạng số nên không cần thay đổi nhiều

# Lọc dữ liệu năm 2022
gold_price_2022 = df.loc["2022-01-01":"2022-12-31", "Price"]
oil_price_2022 = df2.loc["2022-01-01":"2022-12-31", "Price"]

# Vẽ biểu đồ scatter
plt.figure(figsize=(10, 5))
plt.scatter(gold_price_2022, oil_price_2022, alpha=0.7, c='blue', edgecolors='k')
plt.xlabel("Gold Price (USD)")
plt.ylabel("Brent Oil Price (USD)")
plt.title("Gold Price vs Brent Oil Price (2022)")
plt.grid(True)
plt.show(block= True)

pd.concat(df, df2, axis = 1)