"""
7/13class-method+GUI 作業

"""
# 使用 class 建立
# 一個class
# 儲存
# 產品的相關資料
# 請參考
#
# 65-class-properties.py
# 把第一題的Label 上的文字
# 改成讀取 class properties
print("===== GUI 練習 2====")
# 產品參考 snowpeak帳篷 https://www.snowpeak.com.tw/SalePage/Index/6106269

class snowClass(object):  # 繼承Python 最上層的object 類別
    snowName="拱型帳"                                       #定義產品名稱
    snowNumber="SDE-080RH"                                 #定義產品型號
    snowBagSize="60x23x23cm"                               #定義收納體積
    snowWeight=7.65                                        #定義產品重量
    snowPeople= 4                                          #定義容納人數
    def __init__(self, Name, Number, BagSize, Weight, People):  # 類別初始化的函數 initialize 一開始要做的函數
        self.snowName = Name
        self.snowNumber = Number
        self.snowBagSize = BagSize
        self.snowWeight = Weight
        self.snowPeople = People
    def info(self):  # 函數 Function
        print("產品名稱:", self.snowName)
        print("產品型號:", self.snowNumber)
        print("收納後體積:", self.snowBagSize)
        print("產品重量:", self.snowWeight)
        print("容納人數:", self.snowPeople,"人")

snow=snowClass(Name="拱型帳" , Number="SDE-080RH" , BagSize="60x23x23cm"  , Weight=7.65, People=4)
snow.info()

import tkinter as tk # 在Python 3.x 匯入該tkinter 函式庫

win = tk.Tk()                                             # 建立GUI 應用程式的主視窗
win.wm_title("拱型帳產品資料一覽")                            # 設定主視窗標題
win.resizable(width=False, height=False)                  # 設定主視窗不可以被調整大小
win.minsize(width=640, height=480)                        # 最小尺寸
win.maxsize(width=640, height=480)                        # 最大尺寸

label1 =tk.Label(win,text="產品名稱:"+snow.snowName)       # 建立文字
label1.place(x=20, y=60)                                 # 指定元件位置 x=20, y=60 的位置
label2 =tk.Label(win,text="產品型號:"+snow.snowNumber)     # 建立文字
label2.place(x=40, y=80)                                 # 指定元件位置 x=40, y=80 的位置
label3 =tk.Label(win,text="收納後體積:"+snow.snowBagSize)  # 建立文字
label3.place(x=60, y=100)                                # 指定元件位置 x=60, y=100 的位置
label4 =tk.Label(win,text="產品重量:"+str(snow.snowWeight))  # 建立文字
label4.place(x=80, y=120)                                # 指定元件位置 x=80, y=120 的位置
label5 =tk.Label(win,text="容納人數:"+str(snow.snowPeople))  # 建立文字
label5.place(x=100, y=140)                                # 指定元件位置 x=100, y=140 的位置
win.mainloop()                                            # 最後步驟：程式做無限循環