def time_date(str_new):
    new_date, new_time = str_new.split('T')
    print("new date:", new_date)
    print("new time:", new_time)
    yy, mm, dd = new_date.split('-')
    print(f"yy: {yy}, mm: {mm}, dd: {dd}")
    hh, min, sec = new_time.split(':')
    print(f"hh: {hh}, min: {min}, sec: {sec}")
    sec, msec = sec.split('.')
    print(f"sec: {sec}, msec: {msec}")
    msecs = msec.strip('Z')

    output = (yy, mm, dd, hh, min, sec, msecs)
    print(output)
    return output

def Extract_time(str_created_time, str_current_time):
    a1, b1, c1, d1, e1, f1, g1 = time_date(str_created_time)
    print()
    a2, b2, c2, d2, e2, f2, g2 = time_date(str_current_time)

    #z1 = int(c1) - int(c2)
    #z2 = ((12 - int(b1))-(12 - int(b2))) * 30
    #z3 = (int(a2) - int(a1)) * 365
    #result = z1 + z2 + z3
    #z4 = (24 - int(d1)) - (24 - int(d2))
    #z5 = (60 - int(e1)) - (60 - int(e2))
    #z6 = (60 - int(f1)) - (60 - int(f2))
    #print(result, ":days", z4, ":hrs", z5, ":min", z6, ":sec")
    count1 = (int(a1) * 365 + int(b1) * 30 + int(c1))
    count2 = (int(a2) * 365 + int(b2) * 30 + int(c2))
    count3 = ((24 - int(d1)) + int(d1))
    count4 = ((60 - int(e1)) + int(e2))
    count5 = ((60 - int(f1)) + int(f2))
    result = (count2 - count1, "days")
    print("hrs", count3, end=" : ")
    print("min", count4, end=" : ")
    print("sec", count5)
    return result
