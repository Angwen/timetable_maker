lit_class = int(input("Magyarórák száma a héten:"))
mat_class = int(input("Matematikaórák száma a héten:"))
phys_class = int(input("Fizikaórák száma a héten:"))

print("A héten a magyarórák száma %s, a matematikaórák száma %s, \
a fizikaórák száma pedig %s. Ez összesen %s óra." \
% (lit_class, mat_class, phys_class, (lit_class+mat_class+phys_class)))
