str = "A     B     C     D     E     F     G     H     I     J     K     L     M     N     O     P     Q     R     S     T     U     V     W     X     Y     Z"
str_remove_space = str.replace(" ", "")
str_text = str_remove_space[2:6] + " : " + str_remove_space[12:18] + " : " + str_remove_space[21:26]
print(str_text)