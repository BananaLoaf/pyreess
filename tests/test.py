from pyreess.generator import Generator


def test_source():
    gen = Generator(source=b"test", salt=b"")
    gen.set_rules(digits=True,
                  lowercase=True,
                  uppercase=True,
                  symbols=True)
    assert gen.generate(100) == "\\G?O_{UL+SGDUu@_+?h.~g!9jGM4VD&m$h5M5jKv)'D_&pZ)bLX}8vqkE8<BW~-g]\"(JX;R_~V$@`Ny=DH8t|?\"MKDmk,0_`37Vy"


def test_source_salt():
    gen = Generator(source=b"test", salt=b"test")
    gen.set_rules(digits=True,
                  lowercase=True,
                  uppercase=True,
                  symbols=True)
    assert gen.generate(100) == "XISa05CC<2MvTtZp[`==n3$N!:EweX(0mo0YJk`HQWNb=~%'PNi;YZvp)S&L7:h%!}Fi/_sk$n^.3$Z+v}6P;iUCG.y3W}*1I!r+"
