adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("Task 01")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
print("\nTask 02")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("\nTask 03")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("\nTask 04")
count = adwentures_of_tom_sawer.find("h")
print(f"There are {count} times the letter \"h\" in the sentence \"adwentures_of_tom_sawer\".")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("\nTask 05")
count = 0
for word in adwentures_of_tom_sawer.split():
    if word.istitle():
        count += 1
print(f"There are {count} times the word with title in the sentence \"adwentures_of_tom_sawer\".")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("\nTask 06")
count = 0
for index in range(len(adwentures_of_tom_sawer)):
    if adwentures_of_tom_sawer[index:index+3] == "Tom" and count != 1:
        count += 1
    elif adwentures_of_tom_sawer[index:index+3] == "Tom" and count == 1:
        print(f"The index is {index} where the word \"{adwentures_of_tom_sawer[index:index+3]}\" "
              f"finds second times in the sentence \"adwentures_of_tom_sawer\".")
        break

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("\nTask 07")
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("\nTask 08")
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("\nTask 09")
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print("The following sentence is started from \"By the time\":")
        print(sentence)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("\nTask 10")
print(f"The quantity is {len(adwentures_of_tom_sawer_sentences[len(adwentures_of_tom_sawer_sentences)-1].split())} "
      f"of the words in last sentences in list \"adwentures_of_tom_sawer_sentences\".")