from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


Qlist = []
Alist = []






def login(loginid,loginpass):
    try:
        #リンガポルタのページへ行く
        driver.get('https://w5.linguaporta.jp/user/seibido/')
        wait. until(EC.presence_of_all_elements_located)#すべての要素が表示されるまで待機

        #IDを入力
        element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/table/tbody/tr[1]/td/input")#elementに入力欄のパスを代入
        element.clear()#入力欄の中を削除
        element.send_keys(loginid)#自分のログインID

        #passを入力
        element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/table/tbody/tr[2]/td/input")
        element.clear()
        element.send_keys(loginpass)#自分のパスワード

        #ログインボタンを押す
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/table/tbody/tr[3]/td/div/input")
        element.click()#ボタンを押す

    except:
        print("Cannot login")


def selectcoset():
    try:
        #本の選択画面へ移行
        wait. until(EC.presence_of_all_elements_located)
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/dl/dt[2]/form/a")
        element.click()

        #coset2600を選択
        wait. until(EC.presence_of_all_elements_located)
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/div/div[2]/div[3]/input")
        element.click()

    except:
        print("Cannot go coset page")



def selectUnit(unit_num):
    #ユニット選択
    wait. until(EC.presence_of_all_elements_located)
    unit_num = (unit_num)/25
    script = "select_unit('drill', '" + str(1810 + (unit_num)*4) + "', '');"
    try:
        driver.execute_script(script)
    except:
        print("Cannot select Unit")


def Answer():
    #回答
    wait.until(EC.presence_of_all_elements_located)
    try:
        question = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/div/div[2]")
        question = str(question.text)
        if(question in Qlist):
            print("question in Qlist")
            #Qlistから問題番号を取得
            i = Qlist.index(question)
            print(i)

            #Alistから答えを取得
            anser = Alist[i]
            anser = str(anser)
            anser = anser.replace(" ","")
            print(anser)

            #答えを入力
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/div/div[3]/div/input")
            element.clear
            element.send_keys(anser)

            #回答ボタンを押す
            wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")))
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")
            element.click()

            #次へ進を押す
            wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")))
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")
            element.click()

        else:
            #回答欄に適当な答えを入力
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/div/div[3]/div/input")
            element.clear
            element.send_keys("a")

            #回答ボタンを押す
            wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")))
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form/input[3]")
            element.click()

            #正解を見るを押す
            wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form[1]/input[2]")))
            wait.until(EC.presence_of_all_elements_located)
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form[1]/input[2]")
            element.click()

            #問題の答えを入手
            wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")))
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/form[1]/div/div[3]/input")
            anser = element.get_attribute("value")
            Alist.append(str(anser))
            Qlist.append(question)

            #次に進むを押す
            element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td/div/form/input[1]")
            element.click()

            print(Alist)
            print(Qlist)

        return(0)


    except:
        print("Cannot Anser")
        return(1)

def CheckUnitEnd():
    #ユニットが終わっているかの確認
    wait. until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/table/tbody/tr[2]/td/div[3]/form/input")))
    try:
        element = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/table/tbody/tr[4]/td")
        botti = str(element.text)
        botti = botti.replace(" ","")
        if(botti == "問題が有りません。"):
            return(1)
        else:
            return(0)
    except:
        return(1)

Unitnum = 400

print("自分のIDを入力してください")
loginid = str(input())
print("ログインパスワードを入力してください")
loginpass = str(input())

while(1):
    #Chromeを開く
    driver = webdriver.Chrome()
    #タイムアウトの時間を設定
    wait = WebDriverWait(driver, 20)
    login(loginid,loginpass)
    selectcoset()
    selectUnit(Unitnum)
    a = CheckUnitEnd()
    if(a == 1):
        Unitnum = Unitnum+25
        Qlist.clear()
        Alist.clear()
        driver.close()
        continue
    while(1):
        b = 0
        b = Answer()
        if(b == 1):
            break