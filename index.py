# coding=utf-8

import ccxt
import os
import time
from datetime import datetime


braziliex = ccxt.braziliex()
mercado = ccxt.mercado()
foxbit = ccxt.foxbit()

#print(binance_book['bids'][0])
#print(hit.load_markets())
while True:
	
	brb = ('brasiliex', braziliex.fetch_order_book('BTC/BRL')['bids'][0]);
	mbb = ('Mercado', mercado.fetch_order_book('BTC/BRL')['bids'][0]);
	fbb = ('Foxbit', foxbit.fetch_order_book('BTC/BRL')['bids'][0]);
	bra = ('brasiliex', braziliex.fetch_order_book('BTC/BRL')['asks'][0]);
	mba = ('Mercado', mercado.fetch_order_book('BTC/BRL')['asks'][0]);
	fba = ('Foxbit', foxbit.fetch_order_book('BTC/BRL')['asks'][0]);
	
	asks = (bra, mba, fba)
	bids = (brb, mbb, fbb)
	now = datetime.now()
	os.system('clear')
	print(now.strftime("%d/%m/%Y %H:%M:%S"))
	#print('asks', asks)
	#print('bids', bids)
	quant = 0.01
	for ask in asks:
		if (ask[1][0] < max(brb[1][0], mbb[1][0], fbb[1][0])):
			print("\n ##################################")
			print ("Comprar", ask[0], ask[1])
			for bid in bids:
				if(bid[1][0] == max(brb[1][0], mbb[1][0], fbb[1][0])):
					print("Vender", bid[0], bid[1])
			print("Diferença: R$ %.2f = %.2f%%" % (bid[1][0]- ask[1][0], (bid[1][0]- ask[1][0])*100/ask[1][0]))
			print("Valor negociado: %.5f BTC = R$ %.2f" % (quant, ask[1][0]*quant))
			print("Lucro: R$ %.2f" % (quant*(bid[1][0]- ask[1][0])))


"""
hitbtc_markets = hitbtc.load_markets()

print(hitbtc.id, hitbtc_markets)
print(bitmex.id, bitmex.load_markets())
print(huobi.id, huobi.load_markets())

print(hitbtc.fetch_order_book(hitbtc.symbols[0]))
print(bitmex.fetch_ticker('BTC/USD'))
print(huobi.fetch_trades('LTC/CNY'))

print(exmo.fetch_balance())

# sell one ฿ for market price and receive $ right now
print(exmo.id, exmo.create_market_sell_order('BTC/USD', 1))

# limit buy BTC/EUR, you pay €2500 and receive ฿1  when the order is closed
print(exmo.id, exmo.create_limit_buy_order('BTC/EUR', 1, 2500.00))

# pass/redefine custom exchange-specific order params: type, amount, price, flags, etc...
kraken.create_market_buy_order('BTC/USD', 1, {'trading_agreement': 'agree'})
"""