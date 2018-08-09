def buy(curr_data, history):
	if curr_data['7_ema'] > curr_data['44_ema']:
		 return True

def sell(curr_data, history):
	if curr_data['7_ema'] < curr_data['44_ema']:
		 return True