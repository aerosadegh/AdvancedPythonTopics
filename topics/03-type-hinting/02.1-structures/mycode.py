from pkg import process



pr = process(5)
reveal_type(pr)

pr2 = process(bytes("123", encoding="utf8"))
reveal_type(pr2)