import pyupbit

access = "fpb449xT6IRvOp4HuqlM7dZbxBhiDHgrKZJhQxFB"          # 본인 값으로 변경
secret = "TNXPaOqaI8UkEBh7EMGrM2n4DxZQ19khwGuIaAx8"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회