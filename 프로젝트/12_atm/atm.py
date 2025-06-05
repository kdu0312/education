#잔액 초기화
balance = 1000
x=0

while True:

    #모드 선택창
    mode = input("기능을 선택해주세요: (1.입금, 2.출금, 3.영수증 보기, 4.종료): ") ## 참거짓은 힘들것 같고 if로 조져야 할것같은데데

    #종료 메세지
    if mode == "4":
        print("종료 되었습니다.")
        break

    #입금 메세지
    if mode == "1":
    
        deposit = int(input("입금 할 금액을 입력해주세요: "))

        balance += deposit
        print("잔고금액 : ", balance)

        return balance

    #출금 메세지
    if mode == "2":
    
        deposit = int(input("출금금 할 금액을 입력해주세요: "))
    
        if deposit <= deposit:
            balance -= deposit
            print("잔고금액 : ", balance) 
    
        else:
            print("잔액이 부족합니다.")

