import datetime

try:
    login_str = input("Please put your entered time (format: HH:MM): ")
    login_time = datetime.datetime.strptime(login_str, "%H:%M")
    login_hour = login_time.hour

    if login_hour >=9 and login_hour== 9:
        print("Good morning")
    elif login_hour >=4 and login_hour== 4:
        print("Good afternoon")
    else:
        print("You are late")
except ValueError:
    print("Invalid time format. Please enter time in the format HH:MM.")
