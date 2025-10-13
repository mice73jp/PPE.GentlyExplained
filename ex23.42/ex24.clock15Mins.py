def showTime():
    for meridien in ["am", "pm"]:
        for hour in ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            for mins in ["00", "15", "30", "45"]:
                print(f"{hour}:{mins} {meridien}")


if __name__ == '__main__':
    print("== Start showing time table ==")
    showTime()
    print("== Finsih showing time table ==")
