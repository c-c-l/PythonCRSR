# PYTHON3 FILE

def computepay(h,r):
    # 40 is hardcoded bc whatevs but we can
    # define a variable if necessary
    h = hrs - 40
    # 1.5 is the rate for overtime (harcoded again)
    r = rate * 1.5
    return h * r

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)

if hrs > 40 :
  p = computepay(hrs, rate)
  # Update the value of hrs
  hsup = hrs - 40
  hrs = hrs - hsup
else :
    p = 0
print(hrs * rate + p)
