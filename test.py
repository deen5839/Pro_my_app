# 定義一個名叫 compound_interest 的函式，用來算「複利」最後有多少錢
def compound_interest(principal, rate, times_per_year, years):
    # principal：本金（一開始存進去的錢）
    # rate：年利率，單位是「百分比」，例如 5 表示 5%
    # times_per_year：一年裡利息會結算幾次（複利幾次）
    # years：一共存幾年

    """
    計算複利結果。
    :param principal: 初始本金
    :param rate: 年利率（百分比，例如 5 代表5%）
    :param times_per_year: 每年複利次數
    :param years: 年數
    :return: 複利計算後的總金額
    """

    rate_decimal = rate / 100  # 把「5%」這種百分比，換成小數 0.05，公式才好用
    # 複利公式：本金 × (1 + 每期利率) 的 (每年複利次數 × 年數) 次方
    amount = principal * (1 + rate_decimal / times_per_year) ** (times_per_year * years)
    return amount  # 把算好的總金額「交還」給呼叫這個函式的地方

# 下面這段只在「直接執行這個檔案」時才會跑（被別的檔案 import 時通常不會跑）
if __name__ == "__main__":
    principal = float(input("請輸入本金："))  # 讀使用者輸入的本金，並轉成浮點數（可有小數）
    rate = float(input("請輸入年利率（%）："))  # 讀年利率（%），轉成浮點數
    times_per_year = int(input("請輸入每年複利次數："))  # 讀每年複利幾次，轉成整數
    years = float(input("請輸入存款年數："))  # 讀存幾年，轉成浮點數（例如 2.5 年也可以）
    # 呼叫上面的函式，把四個輸入值傳進去，得到最後總金額
    total = compound_interest(principal, rate, times_per_year, years)
    # 印出結果；:.2f 表示只顯示小數點後兩位（像金額常見寫法）
    print(f"{years}年後的總金額為：{total:.2f}")