Xfrom Crypto.PublicKey import RSA
try:
 with open('private.pem'): pass
except IOError:

key = RSA.generate(1024)
public_key = Key.publickey()
enc_data = public_key.encrypt(bonjour tresor,13)
with open('~/Documents/tp-de-GSLW/private.pem','w') as kf:
	kf.write(k.decode())
	kf.close()

with open('~/Documents/tp-de-GSLW/public.pem','w') as pf:
	pf.write(p.decode())
	pf.close()
with open('~/Documents/tp-de-GSLW/private.pem','r') as fk:
	priv = fk.read()
	fk.close()

with open('~/Documents/tp-de-GSLW/public.pem','r') as fp:
	pub = fp.read()
	fp.close()

privat = RSA.importKey(priv)
public = RSA.importKey(pub)


