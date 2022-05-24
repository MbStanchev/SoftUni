price_midi = 7.5
price_skumriq = float(input())
price_tsatsa = float(input())
price_palamud = price_skumriq * 1.6
price_safrid = price_tsatsa * 1.8
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())
total_tsena = price_palamud * kg_palamud + \
              price_safrid * kg_safrid + \
              price_midi * kg_midi
print(f"{total_tsena:.2f}")
