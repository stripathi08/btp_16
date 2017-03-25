import lcm
import time

from exlcm import example_t

lc = lcm.LCM()

msg = example_t()
msg.myname = "Akshay Kumar"

while True:
	lc.publish("EXAMPLE", msg.encode())
