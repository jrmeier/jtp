def buy(curr_data, history):
	if curr_data['7_ema'] > curr_data['44_ema']:
		 return True
	if curr_data['14_rsi'] > curr_data['30']:
		 return True

def sell(curr_data, history):
	if curr_data['7_ema'] < curr_data['44_ema']:
		 return True