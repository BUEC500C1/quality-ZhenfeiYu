from arabic2roman import quality
def test_quality():
	assert quality(1)=="I"
	assert quality(4)=="IV"
	assert quality(9)=="IX"
	assert quality(16)=="XVI"
	assert quality(25)=="XXV"
	assert quality(36)=="XXXVI"
	assert quality(5000)=="number should between 0 and 5000"
	assert quality(-20)=="number should between 0 and 5000"
	assert quality('one')=="Invalid Input"


