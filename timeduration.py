def get_time_date(str):
    date, time = str.split('T')
    print("date:", date)
    print("time:", time)
    yy, mm, dd = date.split('-')
    print(f"yy: {yy}, mm: {mm}, dd: {dd}")
    hh, min, sec = time.split(':')
    print(f"hh: {hh}, min: {min}, sec: {sec}")
    sec, msec = sec.split('.')
    print(f"sec: {sec}, msec: {msec}")
    msecs = msec.strip('Z')

    output = (yy, mm, dd, hh, min, sec, msecs)
    print(output)
    return output

def Extract_time(str_created_time, str_current_time):
    y1, m1, d1, h1, mn1, s1, ms1 = get_time_date(str_created_time)
    print()
    y2, m2, d2, h2, mn2, s2, ms2 = get_time_date(str_current_time)

    date1 = (int(y1) * 365 + int(m1) * 30 + int(d1))
    date2 = (int(y2) * 365 + int(m2) * 30 + int(d2))
    hour = ((24 - int(h1)) + int(h1))
    min = ((60 - int(mn1)) + int(mn2))
    sec = ((60 - int(s1)) + int(s2))
    result = (date2 - date1, "days")
    print("hrs", hour, end=" : ")
    print("min", min, end=" : ")
    print("sec", sec)
    print(result)
    return result

def main():
    str_created_time = "2017-2-29T08:30:27.11904211Z"
    str_current_time = "2019-5-19T04:40:47.11904211Z"

    Extract_time(str_created_time, str_current_time)

if (__name__ == "__main__"):
    main()
