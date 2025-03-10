#Understanding
#Given a strin in D's and I's
#Return numberd of n+1 length, where I means after > prev
#and D means prev > after

#PLAN
#Make an empty stack
#Loop through the string, append a num to the stack depending on whether it is D or I
#Make a string of n+1 but order starts from 1. Using for loop

def arrange_guest_arrival_order(arrival_pattern):
  temp_guest_order = [1,2,3,4,5,6,7,8,9]
  stack = []
  guest_order = []

  for i, ch in enumerate(arrival_pattern):
    if ch == 'I':
      guest_order.append(str(temp_guest_order[i]))
      while stack:
        value = stack.pop()
        guest_order.append(str(value))
    elif ch == 'D':
      stack.append(str(temp_guest_order[i]))
    
  while stack:
    value = stack.pop()
    guest_order.append(str(value)) 
    
    return ''.join(guest_order)
  
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  
