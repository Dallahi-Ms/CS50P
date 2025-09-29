monthes = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

while True :
    try:
        date = input('Date: ').title().strip()
        if '/' in date:
            month, day, year = date.split('/')

        elif ',' in date:
            a, year = date.split(',')
            month, day = a.split(' ')
            month = monthes.index(month ) + 1

        month = int(month)
        day = int(day)
        if month > 12 or month < 1:
            continue
        if day < 1 or day > 31:
            continue

        print(f"{year}-{month:02}-{day:02}")
        break

    except:
        pass
