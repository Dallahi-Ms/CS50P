def convert(emoticons):
    emoticons = emoticons.replace(":)", "🙂")
    emoticons = emoticons.replace(":(", "🙁")
    print(emoticons)

def main():
    emoticons = input("Enter your message: ")
    convert(emoticons)
main()
