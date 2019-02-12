print ('Welcome to the Diet Planner')
#create calories per serving for chicken, spinach, sweet potato
one = 1
chkn_cal = 423
spnch_cal = 41
swt_cal = 180
chkn_prtn = 37
spnch_prtn = 5
swt_prtn = 4
chkn_fbr = 0
spnch_fbr = 4.3
swt_fbr = 6.6
# Have user enter number of servings for chicken, spinach, and sweet potato
chkn = int(input('Enter serving of chicken:'))
spnch = int(input('Enter serving of spinach:'))
swtpt = int(input('Enter serving of sweet potato:'))
# the below if statements will calculate
# the amount of calories for the users serving entries
if chkn > one:
    chkn_ttl = chkn * chkn_cal

if spnch > one:
    spnch_ttl = spnch * spnch_cal

if swtpt > one:
    swt_ttl = swtpt * swt_cal

cal_ttl = (chkn_ttl + spnch_ttl + swt_ttl)
#print ('Total Amount of Calories:', cal_ttl) -- taking this out
# the below lines of code will total the amount of protein taken
# from chicken, spinach, and sweet potato separately
if chkn > one:
    chkn_pttl = chkn * chkn_prtn

if spnch > one:
    spnch_pttl = spnch * spnch_prtn
    
if swtpt > one:
    swt_pttl = swtpt * swt_prtn
cal_pttl = (chkn_pttl + spnch_pttl + swt_pttl)
#print ('Total Amount of Protein:', cal_pttl) -- taking this out 
# the lines below will calculate the fiber from
# servings for chicken, sweet potato, and spinach
    
if chkn > one:
    chkn_fttl = chkn * chkn_fbr
    
if spnch > one:
    spnch_fttl = spnch * spnch_fbr
    
if swtpt > one:
    swt_fttl = swtpt * swt_fbr
cal_fttl = (chkn_fttl + spnch_fttl + swt_fttl)
#print ('Total Amoount of Fiber:', cal_fttl) -- taking this out
# the total from above should be taken from the three
# foods all combined
str(cal_ttl) + "\t" + ("+" if (cal_ttl > 1500) else "-")
print ('Calories/Protein/Fiber:', cal_ttl, cal_pttl, cal_fttl)
