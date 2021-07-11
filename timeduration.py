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

def main():
    str_created_time = "2018-05-10T10:30:07.119045211Z"
    str_current_time = "2020-12-29T10:30:07.119045211Z"
    
    Extract_time(str_created_time, str_current_time)

if(__name__ == "__main__"):
    main()