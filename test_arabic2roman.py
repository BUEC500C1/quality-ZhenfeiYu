import arabic2roman as ar
def test_ar():
	assert ar.arbic2roman(1)=="I"
	assert ar.arabic2roman(4)=="IV"
	assert ar.arabic2roman(9)=="IX"
	assert ar.arabic2roman(16)=="XVI"
	assert ar.arabic2roman(25)=="XXV"
	assert ar.arabic2roman(36)=="XXXVI"
    assert ar.arabic2roman(49)=="XLIX"
    assert ar.arabic2roman(64)=="LXIV"
    assert ar.arabic2roman(81)=="LXXXI"
    assert ar.arabic2roman(100)=="C"

