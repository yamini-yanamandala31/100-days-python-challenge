import pyshorteners

url = input("Enter your long URL: ")

s = pyshorteners.Shortener()

short_url = s.tinyurl.short(url)

print("Short URL:", short_url)
