import codecs
import sys
def decode64():
	x = raw_input("Enter word for decode:")
	x =  codecs.decode(x,'base64')
	print 'Your Decoded word is : ' +x
def encode64():
	x = raw_input("Enter word for encode:")
	x= codecs.encode(x,'base64')
	print 'Your Encoded word is : ' +x
def encodeRot13():
	x = raw_input("Enter word for encode:")
	x= codecs.encode(x,'rot13')
	print 'Your Encoded word is : '+x
def decodeRot13():
	x = raw_input("Enter word for decode:")
	x= codecs.decode(x,'rot13')
	print 'Your Decoded word is : '+x

def main():
	print '             ####################################################'
	print '             #welcome to daly script encode/decode: ROT13,Base64# '
	print '             #################################################### '
	print ''
	print '  1-Encode with base64'
	print '  2-Decode with base64'
	print '  3-Encode with Rot13'
	print '  4-Decode with Rot13'
	print ''
	a = raw_input("Enter Your Choise :")
	if a=='1':
		encode64()
	elif a=='2':
		decode64()
	elif a=='3':
		encodeRot13()
	elif a=='4':
		decodeRot13()
	else :
		print "Incorrect choise , Plz Don't Put BullShit !! , Be smart ...."
		sys.exit(1)
if __name__ == "__main__":
	main()
