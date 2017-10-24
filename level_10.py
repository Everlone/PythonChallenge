
numstr = "11"
series_length = 30
series = ["1"]

for i in range(1,31):     # series is 30 long since 0 to 29
    count = 0
    chrstr = ""
    nextstr = ""
    series.insert(i,numstr)
    for j in range(0,len(numstr)):
        if chrstr == "":
            chrstr = numstr[j]
            count += 1
        elif chrstr == numstr[j]:
            count += 1
        else:
            nextstr = nextstr + str(count) + chrstr
            chrstr = numstr[j]
            count = 1
    nextstr = nextstr + str(count) + chrstr
    numstr = nextstr

print(series)
print("length of series is ",len(series))
print("\r")
print("Answer is len(a[30]) = ",len(series[30]))
