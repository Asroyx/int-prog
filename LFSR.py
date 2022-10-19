state = 0b10011001
for i in range(5):
     print("{:08b}".format(state))
     newbit = (state ^ (state >> 1)) & 1 #[newbite] taking last index of [state]
     state = (state >> 1) | (newbit << 7) #[newbit] was 1 after (newbit<< 7) having new value newbit = 10000000, (state = 01001100 | 10000000) = 11001100
