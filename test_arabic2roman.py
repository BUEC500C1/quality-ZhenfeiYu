from arabic2roman import quality
def test_quality():
	assert quality(1)=="I"
	assert quality(4)=="IV"
	assert quality(9)=="IX"
	assert quality(16)=="XVI"
	assert quality(25)=="XXV"
	assert quality(36)=="XXXVI"
    assert quality(49)=="XLIX"
    assert quality(64)=="LXIV"
    assert quality(81)=="LXXXI"
    assert quality(100)=="C"

