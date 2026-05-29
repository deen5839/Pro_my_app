# 這個 while 迴圈會一直執行，直到使用者輸入「正確格式」的資料才會跳出
while True:
    # 讓使用者輸入一串數字，格式例如：10,20,30
    numbers = input("請輸入數字（用逗號分隔）：")

    # 先處理完全空白的情況，避免後面 split 後沒有任何數字
    if numbers.strip() == "":
        print("請輸入至少一個數字。")
        continue

    # 先把字串依照逗號切開，再把每一段前後空白移除
    parts = [x.strip() for x in numbers.split(",")]

    # 如果有連續逗號（例如 1,,2）或末尾逗號（例如 1,2,），會產生空字串
    if any(part == "" for part in parts):
        print("格式錯誤：請不要輸入空白項目（例如連續逗號）。")
        continue

    # 嘗試把每一個輸入值轉成浮點數
    # 若其中一個不是數字（例如 abc），會進入 except 並提示重輸
    try:
        nums = [float(part) for part in parts]
    except ValueError:
        print("格式錯誤：請確認每一項都是數字，例如 10, 20.5, 30")
        continue

    # 再次確認至少有一個數字（避免除以 0）
    if len(nums) == 0:
        print("請輸入至少一個數字。")
        continue

    # 能走到這裡代表資料都有效，可以離開迴圈
    break

# 計算平均值：總和除以元素數量（此時 len(nums) 一定大於 0）
average = sum(nums) / len(nums)

# 使用 f-string 讓結果更好讀
print(f"平均值為：{average}")