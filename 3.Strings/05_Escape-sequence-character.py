# ========== PYTHON ESCAPE SEQUENCES ==========
#
# \n   -> New line
# \t   -> Horizontal tab
# \b   -> Backspace
# \r   -> Carriage return
# \f   -> Form feed
# \v   -> Vertical tab
# \\   -> Backslash (\)
# \'   -> Single quote (')
# \"   -> Double quote (")
# \a   -> Alert/Bell sound
#
# \ooo -> Character with octal value
# \xhh -> Character with hexadecimal value
# \N{name} -> Unicode character by name
# \uXXXX -> Unicode (16-bit)
# \UXXXXXXXX -> Unicode (32-bit)
#
# ============================================

a = " Shubh \n is \t expected \bto attend \v the \\school in \a noon \f and \r then \'head on \''to this lab for experiments"
print(a)