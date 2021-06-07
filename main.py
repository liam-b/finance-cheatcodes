def npv(rate = 0.1, initial = 0, cash_flows = [], inflation = 0):
  real_rate = ((1 + rate) / (1 + inflation)) - 1
  value = -initial
  for t, net_flow in enumerate(cash_flows):
    value += net_flow / (1 + real_rate) ** (t + 1)

  return value

# print(npv(0.11, 580000, [80000, 100000, 120000, 140000, 160000, 180000, 200000]))


def ret_on_equity(risk_free, market_premium, beta):
  print(f"return on equity = {risk_free} + {market_premium} * {beta}")
  return risk_free + market_premium * beta

# print(ret_on_equity(0.06, 0.08, 1.5))


def PV_bond(coupon, life, YTM, face_value):
  print(f"PV of bond = ({coupon} / {YTM}) * (1 - (1 + {YTM}) ** (-{life})) + {face_value} / (1 + {YTM}) ** {life}")
  PV = (coupon / YTM) * (1 - (1 + YTM) ** (-life)) + face_value / (1 + YTM) ** life
  return PV

# print(PV_bond(10, 4, 0.08, 100))

def WACC(no_of_shares, share_price, risk_free, market_premium, beta,\
   YTM, no_of_bonds, coupon, life, face_value, corp_tax):
  equity_value = no_of_shares * share_price
  print(f"equity_value = {no_of_shares} * {share_price}")
  equity_cost = ret_on_equity(risk_free, market_premium, beta)
  print(f"equity_cost = {equity_cost}")
  debt_value = no_of_bonds * (PV_bond(coupon, life, YTM, face_value))
  print(f"debt_value = {debt_value:.4f}")
  debt_cost = YTM * (1 - corp_tax)
  print(f"debt_cost = {YTM} * (1 - {corp_tax})")
  total_value = equity_value + debt_value
  print(f"total_value = {equity_value:.4f} + {debt_value:.4f}")
  wacc = (equity_cost * equity_value + debt_cost * debt_value) / total_value
  print(f"wacc = ({equity_cost:.4f} * {equity_value:.4f} + {debt_cost:.4f} * {debt_value:.4f}) / {total_value:.4f}")
  return wacc
  
print(WACC(20000000, 1.5, 0.06, 0.08, 1.5, 0.08, 100000, 10, 4, 100, 0.3))


# 20 mill ord shares
# 1.5 per share
# beta of shares 1.5
# market risk premium is 0.08
# risk free rate is 0.06

# 100,000 bonds
# coupon rate of 10%
# maturing in 4 years
# face value of 100
# YTM of 0.08
# company tax rate is 30%