brands=['intel','bMw','eBay','hauwei','bYd','Tesla']
n=len(brands)
for i in range(n):
    if brands[i].lower()=="bmw" or brands[i].lower()=="tesla":
        brands[i]=brands[i].upper()
    elif brands[i].lower()=="byd":
        brands[i]="BYD-新能源"
    elif brands[i].lower()=="ebay":
        brands[i]=brands[i].lower()
    else: brands[i]=brands[i].title()
print(brands)