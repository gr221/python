
import xmlrpc.client as xc

#myc = xc.ServerProxy("http://pc1011106671.ur.de:8001", verbose=False)
myc = xc.ServerProxy("http://phy305.ur.de:8001", verbose=False)

print('--------')
print( 'addiere 7 und 17', myc.add(7,17) )
print('--------')
a = myc.arr(8)
print('........')
print( 'array',  a)
print('--------')
print( 'com.',   myc.com() )
print('--------')

