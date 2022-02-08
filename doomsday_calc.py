CENTURY_ANCHOR_DAY_CYCLE = [2, 0, 5, 3]

DOOMSDAYS = {
    1:3,
    2:28,
    3:14,
    4:4,
    5:9,
    6:6,
    7:11,
    8:8,
    9:5,
    10:10,
    11:7,
    12:12
}

LEAP_DOOMSDAYS = {
    1:4,
    2:29,
    3:14,
    4:4,
    5:9,
    6:6,
    7:11,
    8:8,
    9:5,
    10:10,
    11:7,
    12:12
}

DAY_NAMES = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}


def oddPlusEleven(n):
    if not isDivisibleBy(n, 2):
        n += 11
    n = n // 2
    if not isDivisibleBy(n, 2):
        n += 11
    return (7 - (n%7))%7


def getCenturyAnchor(century):
    firstTwoCenturyDigits = century // 100
    century_mod_4 = firstTwoCenturyDigits % 4
    return CENTURY_ANCHOR_DAY_CYCLE[century_mod_4]


def getNearestDoomsday(month, isLeapYear):
    if isLeapYear:
        return LEAP_DOOMSDAYS[month]
    return DOOMSDAYS[month]

def isDivisibleBy(A,B):
    return not bool(A%B)

def getIsLeapYear(year):
    if (isDivisibleBy(year, 4)  \
        and not isDivisibleBy(year,100)) \
        or isDivisibleBy(year, 400):
        return True
    return False


def CalculateDayOfWeek(month,day,year):
    isLeapYear = getIsLeapYear(year)

    century = (year // 100) * 100

    lastTwoYearDigits = year % 100

    doomsdayDayOfWeek = (oddPlusEleven(lastTwoYearDigits) + getCenturyAnchor(century)) % 7

    nearestDoomsday = getNearestDoomsday(month, isLeapYear)

    dayOfWeek = (((day - nearestDoomsday) % 7) + doomsdayDayOfWeek) % 7

    return DAY_NAMES[dayOfWeek]

