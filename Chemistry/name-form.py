print "Given the name of a compound, this code will help you write the formula for that compound."
a = "0"
acid = raw_input("\nDoes the compound's name contain the word 'acid'?")
while acid != "yes" and acid != "no":
  acid = raw_input("Error. Please enter yes or no.")
are = ""
prefixx = "pre"
if acid == "yes":
  a = "1"


else:
  non = raw_input("Is the first element name in the compound a metal or a nonmetal?")
  while non != "metal" and non != "nonmetal":
    non = raw_input("Error. Enter either metal or nonmetal")
  if non == "metal":
    a = "3"
  elif non == "nonmetal":
    a = "2"
  
prefix = {
    "mono" : 1,
    "no prefix" : 1,
    "di" : 2,
    "tri" : 3,
    "tetra" : 4,
    "penta" : 5,
    "hexa" : 6,
    "hepta" : 7,
    "octa" : 8
    }

  
###acid
if a == "1":
  
  polyacid = raw_input("This means this compund is an acid, and contains hydrogen. Does the compound name start with 'hydro-'?")
  while polyacid != "no" and polyacid != "yes":
    polyacid = raw_input("Error. Enter yes or no.")
  if polyacid == "no":
    print "Acids usually contain the prefix 'hydro-' in their name, but, as this one does not, then this compound must contain a polyatomic ion (which is when the 'hydro' is dropped."
    us = raw_input("Does the first word in the name end in 'ous' or 'ic'?")
    while us != "ous" and us != "ic":
      polyacid = raw_input("Error. Enter ous or ic.")
    if us == "ous":
      print "\nBecause it ends in 'ous', replace the ous with 'ite'. Now, the word you are left with is the polyatomic ion in the formula."
      print "\nHere is a list of polyatomic ions: https://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png\nFind the polyatomic in your compound using this list. For example, nitrite is NO2."
      form = raw_input("What is the formula for this polyatomic? Please enter uppercase letters and numbers, like NO2")
      acidcharge = raw_input("What is the charge of this polyatomic? Please enter it as, for example, '-1', and not '1-', with the minus sign coming first.")
      acidnum = abs(int(acidcharge))
      print "\nA charge of %s means that this polyatomic wants %i electron(s)." % (acidcharge, acidnum)
      print "Because each hydrogen atom can give away 1 electron, there will need to be " + str(acidnum) + " hydrogen atom(s) to satisfy this polyatomic when bonding."
      if acidnum == 1:
        acidnum = ""
      print "\nSo, the chemical formula for this compound is \n'H%s%s'" % (acidnum, form)
      
    elif us == "ic":
      print "\nBecause it ends in 'ic', replace the ic with 'ate'. Now, the word you are left with is the polyatomic ion in the formula."
      print "\nHere is a list of polyatomic ions: https://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png\nFind the polyatomic in your compound using this list. For example, nitrate is NO3."
      form = raw_input("What is the formula for this polyatomic? Please enter uppercase letters and numbers, like NO3")
      acidcharge = raw_input("What is the charge of this polyatomic? Please enter it as, for example, '-1', and not '1-', with the minus sign coming first.")
      acidnum = abs(int(acidcharge))
      print "\nA charge of %s means that this polyatomic wants %i electron(s)." % (acidcharge, acidnum)
      print "Because each hydrogen atom can give away 1 electron, there will need to be " + str(acidnum) + " hydrogen atom(s) to satisfy this polyatomic when bonding."
      if acidnum == 1:
        acidnum = ""
      print "\nSo, the chemical formula for this compound is \n'H%s%s'" % (acidnum, form)
  elif polyacid == "yes":
    print "This compound does not contain a polyatomic ion. So, this compound's name looks like 'hydro-(something)-ic acid'. Remove the 'hydro' and 'ic' from the 'something' to find what element it is. For example, hydrochloric is chlor, which is obviously the element chlorine."         
    acidsym = raw_input("\nWhat is the symbol for this element?")
    col = raw_input("What column is this element in? Please enter a numerical value.")
    c = 18 - int(col)
    print "This nonmetal wants to gain %i electrons to be stable. As each hydrogen atom always wants to give 1 electron, there will have to be %i hydrogen atoms(s) that bond with the nonmetal.\nSo, the compound's formula is H%i%s" % (c, c, c, acidsym)


###nonmetal
elif a == "2":
  pre1 = raw_input("What is the prefix coming before the first nonmetal's name (no caps, please)? If there is no prefix, please enter 'no prefix'.")
  if pre1 == "no prefix":
    prefixx = ""
  else: 
    prefixx = " the prefix"
  while pre1 != "di" and pre1!= "tri" and pre1!= "tetra" and pre1!= "mono" and pre1!= "penta" and pre1!= "hexa" and pre1!= "hepta" and pre1!= "octa" and pre1 != "no prefix":
    pre1 = raw_input("Error. Please enter either 'no prefix' or 'mono', 'di', 'tri', 'tetra', 'penta', 'hexa', etc.")
  if pre1 == "no prefix" or pre1 == "mono":
    are = "is"
  else:
    are = "are"
  print "As the first element in your compound's name has%s %s, this means there %s %i of the nonmetal in the compound" % (prefixx, pre1, are, prefix[str(pre1)])
  
  pre2 = raw_input("What is the prefix coming before the second nonmetal's name (no caps, please)? If there is no prefix, please enter 'no prefix'.")
  if pre2 == "no prefix":
    prefixx = ""
  else: 
    prefixx = " the prefix"
  while pre2 != "di" and pre2!= "tri" and pre2!= "tetra" and pre2!= "mono" and pre2!= "penta" and pre2!= "hexa" and pre2!= "hepta" and pre2!= "octa" and pre2 != "no prefix":
    pre2 = raw_input("Error. Please enter either 'no prefix' or 'mono', 'di', 'tri', 'tetra', 'penta', 'hexa', etc.")
  if pre2 == "no prefix" or pre2 == "mono":
    are = "is"
  else:
    are = "are"
  print "As the second element in your compound's name has%s %s, this means there %s %i of the nonmetal in the compound" % (prefixx, pre2, are, prefix[str(pre2)])
  raw = "u"
  while raw != "":
    raw = raw_input("Press enter to continue")
  symn1 = raw_input("What is the symbol for the first element in the compound name (look on the periodic table)? For example, oxygen's symbol is O.")
  symn2 = raw_input("\nLikewise, what is the symbol for the second element in the compound name? (although the actual element name may not be in the compound name, and is instead 'oxide' or something, it is easy to figure out that this is the element oxygen.)")
  one = prefix[str(pre1)]
  two = prefix[str(pre2)]
  if pre1 == "no prefix" or pre1 == "mono":
    are = "is"
  else:
    are = "are"
  
  print "\n\nSo, as there %s %s of the first element ('%s') and %s of the second element ('%s'), the formula for this compound will look like..." % (are,str(one), symn1,str(two), symn2)
  if one == 1:
    one = ""
  else:
    one = one
  if two == 1:
    two = ""
  else:
    two = two
  print "%s%s%s%s" % (symn1,str(one),symn2,str(two))


###metal
elif a == "3":
  trans = raw_input("This compound is an ionic compound: a bond between a metal and a nonmetal. Does the name of the compound have a Roman numeral in it?")
  while trans != "yes" and trans != "no":
    trans = raw_input("Error. Enter yes or no.")
    
  ###transition metal
  if trans == "yes":
    print "\nThis means that the metal in this compound is a tranisition metal. Transition metals (besides zinc, cadmium, and silver) never lose a set amount of electrons when bonding, so Roman numerals are used to indicate how many electrons they have lost (the same as their charge)."
    rome = raw_input("What is this Roman numeral? (Enter it as an Arabic numeral, not a Roman numeral.")
    poly = raw_input("Does the second part of the compound name (after the Roman numeral) end in 'some element name'+ide? i.e. fluoride, phoshphide, etc. ***Hydroxide or cyanide would not fall under this category, as those are not element names + ide.")
    while poly != "yes" and poly != "no":
      poly = raw_input("Error. Enter yes or no.")
    if poly == "yes":
      print "This means there is no polyatomic in the compound."
      elec = raw_input("Figure out what element is in the second part of the formula by removing ide (floride becomes flor, which is clearly fluorine). Locate this element in the periodic table. What column is it in?")
      want = 18 - int(elec)
      print "\nAs it is in column %s, this nonmetal wants %i electrons." % (elec, want)
      if want == int(rome):
        print "\nBecause the Roman numeral is %s, meaning that the metal has given %s electrons to the nonmetal, and the nonmetal wants %s electrons, this works out perfectly, and there is one of each atom in the formula." % (rome, rome, str(want))
        print "\nSo, the formula for this compound is simply the symbol of the metal element (first part of compound name) plus the symbol of the nonmetal (second part of compound name)."
      elif want > int(rome):
        print "\nBecause the nonmetal wants more electrons than the metal is giving away, there must be more metal atoms than nonmetal atoms in the formula. Each metal atom can give %s electron(s) to each nonmetal, and each nonmetal wants %s electrons, so there will have to be a %s:%s ratio of metals to nonmetals." % (rome, str(want), str(want), rome)
        if int(rome) == 1:
          print "\nSo, the formula for this compound is the symbol of the metal element (first part of compound name) subscript 2, as there need to be 2 metal atoms, and then the symbol of the nonmetal (last part of compound name) no subscript, as there is only 1 of this atom."
        else:
          print "\nSo, the formula for this compound is the symbol of the metal element (first part of compound name) subscript 3, as there need to be 3 metal atoms, and then the symbol of the nonmetal (last part of compound name) subscript 2"
      elif int(rome) > want:
        print "\nBecause the metal is losing more electrons than the polyatomic wants to take, there must be more of the polyatomic in the formula than metal atoms. As the metal is giving %s electrons, and the polyatomic only wants %s electrons, there must be a %s:%s ratio of metals to nonmetals" % (rome, str(want), str(want), rome)
        if want == 1:
          print "\nSo, the formula for this compound is 'symbol of the metal atom' (first part of compound name) no subscript, as there is only one of this atom, and then the symbol of the nonmetal (second part of the compound name) subscript %s" % rome
        else:
          print "\nSo, the formula for this compound is 'symbol of the metal atom' (first part of compound name) subscript %s, as there are %s of these atoms in the compound, and then the symbol of the nonmetal (second part of the compound name) subscript %s" % (str(want), str(want), rome)
    if poly == "no":
      print "\nThis means there is a polyatomic in the compound. The polyatomic is in the compound's name--it comes right after the Roman numeral. Find this polyatomic using this list: https://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png" 
      wanp = raw_input("What is the charge of this polyatomic? Please enter it as, for example, -1, not 1-.") 
      while wanp != "-1" and wanp != "-2" and wanp != "-3":
        wanp = raw_input("Error. Try again")
      want = abs(int(wanp))
      print "\nThis means the polyatomic wants %s electrons" % want
      if want == int(rome):
        print "\nBecause the Roman numeral is %s, meaning that the metal has given %s electrons to the nonmetal, and the polyatomic wants %s electrons, this works out perfectly, and there is one of each atom in the formula." % (rome, rome, str(want))
        print "\nSo, the formula for this compound is simply the symbol of the metal element (first part of compound name) plus the formula of the polyatomc (second part of compound name), found on the polyatomics list."
      elif want > int(rome):
        print "\nBecause the polyatomic wants more electrons than the metal is giving away, there must be more metal atoms than the number of the polyatomic in the formula. Each metal atom can give %s electron(s) to one of the polyatomic ions, and each polyatomic wants %s electrons, so there will have to be a %s:%s ratio of metals to the polyatomic." % (rome, str(want), str(want), rome)
        if int(rome) == 1:
          print "\nSo, the formula for this compound is the symbol of the metal element (first part of compound name) subscript 2, as there need to be 2 metal atoms, and then the formula for the polyatomic (last part of compound name) no subscript, as there is only of this polyatomic in the compound."
        else:
          print "\nSo, the formula for this compound is the symbol of the metal element (first part of compound name) subscript 3, as there need to be 3 metal atoms, and then, in parentheses (the formula for the polyatomic) subscript 2, as there are two of this polyatomic in the compound."
      
      elif int(rome) > want:
        print "\nBecause the metal is losing more electrons than the polyatomic wants to take, there must be more of the polyatomic ion in the formula than metal atoms. As the metal is giving %s electrons, and the polyatomic only wants %s electrons, there must be a %s:%s ratio of metals to to the polyatomic" % (rome, str(want), str(want), rome)
        if want == 1:
          print "\nSo, the formula for this compound is 'symbol of the metal atom' (first part of compound name) no subscript, as there is only one of this atom, and then the formula for the polyatomic (last part of compound name, found in the list) subscript %s" % rome
        else:
          print "\nSo, the formula for this compound is 'symbol of the metal atom' (first part of compound name) subscript %s, as there are %s of these atoms in the compound, and then the formula for the polyatomic (second part of the compound name) subscript %s" % (str(want), str(want), rome)
  
  
  elif trans == "no":
    one = raw_input("Is the metal in column 1 on the periodic table, or is it silver? If it is one of these two, enter yes.")
    while one != "yes" and one != "no":
      one = raw_input("Error. Enter yes or no.")
    if one == "yes":
      print "Metals in this column, plus silver, want to give 1 electron."
      polymet = raw_input("Is the second part of the compound name a polyatomic? Here is a list of polyatomic ions: https://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png")
      while polymet != "yes" and polymet != "no":
        polymet = raw_input("Error. Enter yes or no.")
      if polymet == "no": 
        coll = raw_input("Find the nonmetal (second part in compound name) on the periodic table. What column is it in?")
        cox = 18 - int(coll)
        print "The formula for this compound is the symbol of the metal element, subcript %s, as there need to be %s of this metal to statisfy the nonmetal, which wants %s electrons. Then, the symbol for the nonmetal." % (cox, cox, cox)
      if polymet == "yes":
        col2 = raw_input("Find the polyatomic on the list. What is it's charge? Take the absolute value of the charge. This results in how many electrons the polyatomic wants. What is this number?")
        print "So, there need to be %s metal atoms, as one metal atom gives one electron, to satisfy the polyatomic, which wants %s." % (col2, col2) 
        print "\nThe formula for this compound is 'the symbol of the metal' + subscript %s, and then the formula of the polyatomic." % cox
    elif one == "no":
      two = raw_input("Is the metal in column 2, or is it zinc or cadmium? If it is any of these, enter yes.")
      while two != "yes" and two != "no":
        two = raw_input("Error. Enter yes or no.")
      if two == "yes":
        print "Zinc, cadmium, and metals in column 2 all want to give 2 electrons."
        print "\nIf there is a polyatomic following the metal (here is a list) then find the charge of that polyatomic. Take the absolute value of this to find how many electrons it needs. https://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png"
        print "\nOtherwise, if there is no polyatomic, find the column that the nonmetal is in, and find how many columns away this column is from column 18. This is how many electrons it wants."
        e = raw_input("Enter how many electrons the nonmetal / polyatomic wants.")
        print "\nSo, the metal atom wants to give 2 electrons, and the nonmetal / polyatomic wants %s electrons. Find the easiest way to get the nonmetal / polyatomic the electrons it wants. For example, if the nonmetal / polyatomic wanted 3, there would have to be 3 metal atoms and two of nonmetal atoms / polyatomics." % e
        print "\nThe formula for this would be the metal's symbol, subscript (however many of the metal atom there are), and then the symbol of the nonmetal / polyatomic, subcscript however many there need to be."
  
  
  
  
  
  
  
  
  
  