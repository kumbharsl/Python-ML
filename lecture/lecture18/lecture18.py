#nested list
lang = ["Cpp","Java","Python",["Go","Rust","Dart"]]

print(lang[1])
print(lang[3][1])

#shallow cp and deep cp
newList = lang.copy()
print(lang)
print(newList)
print(id(lang) == id(newList))
lang[3][1] = "JavaScript"
print(lang)
print(newList)

