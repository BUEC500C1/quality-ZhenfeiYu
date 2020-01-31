from arabic2roman import quality
def test_quality():
	assert quality(1)=="I"
	assert quality(4)=="IV"
	assert quality(9)=="IX"
	assert quality(16)=="XVI"
	assert quality(25)=="XXV"
	assert quality(36)=="XXXVI"


