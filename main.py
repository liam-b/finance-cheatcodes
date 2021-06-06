def npv(rate = 0.1, initial = 0, cash_flows = []):
  value = -initial
  for t, net_flow in enumerate(cash_flows):
    value += net_flow / (1 + rate) ** (t + 1)

  return value

print(npv(0.11, 580_000, [80_000, 100_000, 120_000, 140_000, 160_000, 180_000, 200_000]))
