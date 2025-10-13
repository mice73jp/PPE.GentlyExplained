# # My solution
# def getHoursMinutesSeconds(totalSeconds):
#     M1 = 60
#     H1 = M1 * M1
#     D1 = H1 * 24
#     timeStr = ''

#     if totalSeconds // D1 > 0:
#         days = totalSeconds // D1
#         timeStr += str(days) + 'd '
#         totalSeconds -= ( days * D1 )

#     if totalSeconds // H1 > 0:
#         hours = totalSeconds // H1
#         timeStr += str(hours) + 'h '
#         totalSeconds -= ( hours * H1 )

#     if totalSeconds // M1 > 0:
#         minutes = totalSeconds // M1
#         timeStr += str(minutes) + 'm '
#         totalSeconds -= ( minutes * M1 )

#     if totalSeconds > 0 or len(timeStr) == 0:
#         timeStr += str(totalSeconds) + 's '

#     return timeStr.strip()


# # My solution2
# def getHoursMinutesSeconds(totalSeconds):
#     M1 = 60
#     H1 = M1 * M1
#     D1 = H1 * 24

#     times = []

#     if totalSeconds // D1 > 0:
#         days = totalSeconds // D1
#         times.append(str(days) + 'd')
#         totalSeconds -= ( days * D1 )

#     if totalSeconds // H1 > 0:
#         hours = totalSeconds // H1
#         times.append(str(hours) + 'h')
#         totalSeconds -= ( hours * H1 )

#     if totalSeconds // M1 > 0:
#         minutes = totalSeconds // M1
#         times.append(str(minutes) + 'm')
#         totalSeconds -= ( minutes * M1 )

#     if totalSeconds > 0 or len(times) == 0:
#         times.append(str(totalSeconds) + 's')

#     return ' '.join(times)


# Book solution
def getHoursMinutesSeconds(totalSeconds):
    M1 = 60
    H1 = M1 * M1
    D1 = H1 * 24

    if totalSeconds == 0:
        return '0s'

    days = 0
    while totalSeconds >= D1:
        days += 1
        totalSeconds -= D1

    hours = 0
    while totalSeconds >= H1:
        hours += 1
        totalSeconds -= H1

    minutes = 0
    while totalSeconds >= M1:
        minutes += 1
        totalSeconds -= M1

    seconds = totalSeconds

    hms = []
    if days > 0:
        hms.append(str(hours)+'d')
    if hours > 0:
        hms.append(str(hours)+'h')
    if minutes > 0:
        hms.append(str(minutes)+'m')
    if seconds > 0:
        hms.append(str(seconds)+'s')

    return ' '.join(hms)


if __name__ == '__main__':
    print("== Start hours minutes seconds ==")
    assert getHoursMinutesSeconds(30) == '30s'
    assert getHoursMinutesSeconds(60) == '1m'
    assert getHoursMinutesSeconds(90) == '1m 30s'
    assert getHoursMinutesSeconds(3600) == '1h'
    assert getHoursMinutesSeconds(3601) == '1h 1s'
    assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
    # assert getHoursMinutesSeconds(90042) == '25h 42s'
    assert getHoursMinutesSeconds(90042) == '1d 1h 42s'
    assert getHoursMinutesSeconds(0) == '0s'
    print("== Finish hours minutes seconds ==")
