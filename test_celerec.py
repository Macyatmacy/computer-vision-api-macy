import os

def test_celerec():
    assert 0 == os.system("python celerec.py --file queen.jpg")
    