import arabic2roman as ar
def test():
	assert ar.intToRoman(1)=="I"
	assert ar.intToRoman(4)=="IV"
	assert ar.intToRoman(9)=="IX"
	assert ar.intToRoman(16)=="XVI"
	assert ar.intToRoman(25)=="XXV"
	assert ar.intToRoman(36)=="XXXVI"
    assert ar.intToRoman(49)=="XLIX"
    assert ar.intToRoman(64)=="LXIV"
    assert ar.intToRoman(81)=="LXXXI"
    assert ar.intToRoman(100)=="C"

