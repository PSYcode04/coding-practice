prize = int(input())
stock = list(map(int, input().split()))

jun_stock = 0
jun_prize = prize
sung_stock = 0
sung_prize = prize

up_time = 0 # 연속 상승 일수
down_time = 0 # 연속 하락 일수
last_stock = 0
count = 0

for _stock in stock:
    count += 1
    # 준현 - 매매가능하면 매매 (매도 안함)
    if jun_prize // _stock > 0:
        jun_stock += jun_prize // _stock    # 살 수 있는 양 만큼 주식개수 추가
        jun_prize -= _stock * (jun_prize // _stock) # 현재 구매한 만큼 자산에서 차감

    # 성민
    # 연속 상승, 하락 체크
    if last_stock > _stock:
        down_time += 1
        up_time = 0
    elif last_stock < _stock:
        up_time += 1
        down_time = 0

    # 3연속 하락이고 주식을 살 수 있는 자산이 있으면
    if down_time >= 3 and sung_prize // _stock > 0:  # 전량매수
        sung_stock += sung_prize // _stock
        sung_prize -= _stock * (sung_prize // _stock)

    # 3연속 상승이고 가진 주식이 있으면
    elif up_time >= 3 and sung_stock > 0:  # 전량매도
        sung_prize += _stock * sung_stock
        sung_stock = 0

    last_stock = _stock # 오늘거 정리

jun_prize += jun_stock * stock[13]
sung_prize += sung_stock * stock[13]

if jun_prize > sung_prize:
    print("BNP")
elif jun_prize < sung_prize:
    print("TIMING")
else:
    print("SAMESAME")