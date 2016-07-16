text = "X-DSPAM-Confidence:    0.8475";
pos_colon = text.find(':')
s1 = text[pos_colon + 1:]
s2 = s1.strip()
print float(s2)

	
