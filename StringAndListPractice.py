words = "It's thanksgiving day. It's my birthday,too!"
position = words.find("day")
print position

newWords = words.replace( "day", "month" )
print newWords

x = ["hello",2,54,-2,7,12,98,"world"]
xFirstAndLast = [x[0],x[len(x)-1]]
print( xFirstAndLast )

x = [19,2,54,-2,7,12,98,32,10,-3,6]
xSorted = sorted(x)
print xSorted
xSorted1 = xSorted[0:len(x)/2]
print xSorted1
xSorted2 = xSorted[len(x)/2+1:]
print xSorted2
# xCombined = xSorted1
xCombined = []
xCombined.append(xSorted1)
xCombined += xSorted2
# xCombined[0] = xSorted1
print xCombined

