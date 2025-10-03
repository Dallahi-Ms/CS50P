import datetime, sys
import inflect

p = inflect.engine()
def main():
    brd = input("Date of Birth: ")
    print(transfer(brd))



def transfer(s):
    try:
        date = datetime.datetime.strptime(s, "%Y-%m-%d").date()
        now = datetime.date.today()
        difference = now - date
        minutes = difference.total_seconds() / 60
        minutes = (p.number_to_words(round(minutes), andword="")).capitalize()

        return f"{minutes} minutes"

    except Exception:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
