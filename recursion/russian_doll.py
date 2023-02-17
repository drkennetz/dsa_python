def open_russian_doll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        open_russian_doll(doll-1)