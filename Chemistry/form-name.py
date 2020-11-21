###### code 1: going from formula to name
###Bibliography is at the bottom
print "Given the formula for a compound, this code will teach you how to write the name of that compound."
a = 0
### 1 = nonmetal, 2 = metal, 3 = hydrogen
while a < 0.5:
    first = raw_input("\nIs the first element in the compound's formula a nonmetal, a metal, or hydrogen?")
    if first == "nonmetal" or first == "Nonmetal" or first == "a nonmetal":
        a = 1
    elif first == "metal" or first == "Metal" or first == "a metal":
        a = 2
    elif first == "hydrogen" or first == "Hydrogen":
        a = 3
    else:
        a = 0
        print "Error. Please enter either 'nonmetal', 'metal', or 'hydrogen'"
        
prefix = {
    1 : "mono",
    2 : "di",
    3 : "tri",
    4 : "tetra",
    5 : "penta",
    6 : "hexa",
    7 : "hepta",
    8 : "octa"
    }
raw = "hello"
is1 = ""
is2 = ""
nm1 = 0
nm2 = 0
acidpoly = " "

###nonmetals
if a == 1:
    print "\nThis compound is a covalent compound, meaning that it is a bond between two nonmetals."
    while str(nm1) != "8" and str(nm1) != "7" and str(nm1) != "6" and str(nm1) != "5" and str(nm1) != "4" and str(nm1) != "3" and str(nm1) != "2" and str(nm1) != "1":
      nm1 = raw_input("What is the subscript under the first element? (If there is no subscript, enter 1). Please enter a numerical value, i.e. ‘4’, and not ‘four’. It must be 8 or less")
    while  str(nm2) != "8" and str(nm2) != "7" and str(nm2) != "6" and str(nm2) != "5" and str(nm2) != "4" and str(nm2) != "3" and str(nm2) != "2" and str(nm2) != "1":
      nm2 = raw_input("\nLikewise, what is the subscript under the second element in the formula?")
    if int(nm1) == 1:
      is1 = "is"
    else:
      is1 = "are"
    if int(nm2) == 1:
      is2 = "is"
    else:
      is2 = "are"
    print "\nYour first element has subscript %s, meaning that there %s %s of this element in the compound. The prefix for this is '%s-'" % (str(nm1), is1, str(nm1), prefix[int(nm1)]) 
    print "\nYour second element has subscript %s, meaning that there %s %s of this element in the compound. The prefix for this is '%s-'" % (str(nm2), is2, str(nm2), prefix[int(nm2)])
    while raw != "":
      raw = raw_input("Press enter to continue")
    if int(nm1) == 1:
        print "\nTo name the compound, simply add the prefixes of each element to its respective element, and replace the ending of the second element with the suffix 'ide'. However, when there is only one of the first element, the 'mono' is dropped. So, your compound's name is: \n'(first element name) + " + prefix[int(nm2)] + "-(second element name)ide'"
    else: 
      print "\nTo name the compound, simply add the prefixes of each element to its respective element, and replace the ending of the second element with the suffix 'ide'. So your compound's name is\n'%s-(first element name) + %s-(second element name)ide'" % (prefix[int(nm1)], prefix[int(nm2)])
    print "\nAlso, when adding a prefix (this does not include di- and tri-) to an element name that begins with a vowel (like oxygen), the prefix's ending vowel is dropped. While O3 would be trioxide, O4 would become tetroxide."
    raw = "g"
    while raw != "":
      raw = raw_input("Press enter to continue")
    print "\nHere are some examples of covalent compound names:\nSBr5 is 'Sulfur pentabromide'\nNO2 is 'Nitrogen dioxide'\nP2O5 is 'Diphosphorus pentoxide'" 


###metals
elif a == 2:
    print "\nThis compound is an ionic compound: a metal and a nonmetal bonded together."   
    trans = raw_input("Is this metal a transition metal (is it in column 3-12 on the periodic table?)")
    while trans != "Yes" and trans!= "yes" and trans != "no" and trans != "No":
      trans = raw_input("Error. Please enter yes or no.")
    ###transition
    if trans == "yes" or trans == "Yes":
      trans = raw_input("Is the metal either Zinc, Cadmium, or Silver? (answer yes or no)")
      while trans != "Yes" and trans!= "yes" and trans != "no" and trans != "No":
        trans = raw_input("Error. Please enter yes or no.")
      ###zinc cadmium silver
      if trans == "yes" or trans == "Yes":
        print "Normally, when naming compounds containing transition metals, Roman Numerals are used in the names. Although Zinc, Cadmium, and Silver are transition metals, they have fixed charges, meaning they always want to lose a given amount of electrons, and are exempt from this rule."
        raw = "u"
        while raw != "":
          raw = raw_input("Press enter to continue")
        polyma = raw_input("\nDoes the second part of the formula (the part containing a nonmetal) contain a polyatomic ion?  A polyatomic ion consists of two or more atoms bonded to each other, forming an ion with a fixed charge. If there is just a single nonmetal in the formula following the metal, there is not a polyatomic. Here is a list of common polyatomic ions:\nhttps://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png")
        while polyma != "Yes" and polyma!= "yes" and polyma != "no" and polyma != "No":
          polyma = raw_input("Error. Please enter yes or no.")
        if polyma == "Yes" or polyma == "yes":
          print "\nTo name the compound, simply add the name of the metal and the name of the polyatomic ion. For example, Zn(NO3)2 is named Zinc Nitrate, as NO3 is the polyatomic 'nitrate'"
        if polyma == "No" or polyma == "no":
          print "\nTo name the compound, simply add the two element names together, and replace the ending of the second element with '-ide'. Easy. Here are some examples:\nZn3N2 is 'Zinc Nitride'\nAg3P is 'Silver Phosphide'\nCdCl2 is 'Cadmium Chloride'"
      ###trans metal no zinc silver cadmium
      elif trans == "no" or trans == "No":
        print "\n\nTransition metals, like all metals, want to lose electrons when bonding. However, all transition metals besides Zinc, Cadmium, and Silver don't always want to lose a set amount of electrons. For this reason, when naming these compounds, Roman numerals are used to indicate the amount of electrons that the metal has lost. This is the same as the metal's charge (if it loses 3 electrons, its charge will be 3+)."
        poly_qwa = raw_input("\nDoes the compound contain a polyatomic ion? (answer yes or no) A polyatomic ion consists of two or more atoms bonded to each other, forming an ion with a fixed charge. If there is just a single element following hydrogen, there is not a polyatomic. Here is a list of common polyatomic ions:\nhttps://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png")
        while poly_qwa != "yes" and poly_qwa != "no":
          poly_qwa = raw_input("Error. Enter yes or no.")
        if poly_qwa == "no":
          clum = raw_input("Locate the second element in your formula (the nonmetal) on the periodic table. How many columns away from column 18 is it? Enter a numerical value.")
          while clum != "1" and clum != "2" and clum != "3":
            clum = raw_input("Error. Try again.")
          clum_x = int(clum)
          xxx = raw_input("\nHow many atoms of this nonmetal are in the formula (what is the subscript under the nonmetal? No subscript means 1). Please enter a numerical value. ")
          while int(xxx) < 1 or int(xxx) > 10:
            xxx = raw_input("Error. Try again")
          electrons = clum_x * int(xxx)
          print "\n\nYour nonmetal is in column %s. Elements in this column want to gain %s electrons, and in the formula are %i atoms of the nonmetal. So, the nonmetal(s) want to gain a total of %i electrons." % (str(18 - clum_x), str(clum_x), int(xxx), electrons)
          print "\nDivide this number--the total amount of electrons gained by the nonmetal atom(s)--by the amount of metal atoms in the formula (the subscript under metal atom). For example, if the nonmetal(s) want to gain 6 electrons, and their are 3 metal atoms, each metal atom will have to give (6/3) = 2 electrons to each nonmetal atom."
          raw = "u"
          while raw != "":
            raw = raw_input("Press enter to continue")
          print "\n\nThis number, representing the number of electrons each metal atom gives to each nonmetal atom, is the Roman numeral used when naming the compound. This is how to name it:\n'first element name' + (calculated Roman numeral) + 'second element name'-ide\nThe suffix -ide replaces the ending of the second element name."
          print "Here are some examples:\nAuBr is 'Gold (I) Bromide'\nCu3P2 is 'Copper (II) Phosphide'"
        elif poly_qwa == "yes":
          charge = int(raw_input("Find the polyatomic ion on the list of polyatomics. What is the charge of the polyatomic ion, listed above the name? Please enter it as, for example, '-1', and not '1-', with the minus sign coming first."))
          polynum = raw_input("How many of the polyatomic ion are there in the formula (enter a numerical value)? For there to be multiple, the formula would look like 'metal atom (NO3)2', in which case there are 2 of the polyatomic NO3.")
          are = "hello"
          if polynum == "1": 
            are = "is"
          else:
            are = "are"
          print "As there %s %i of the polyatomic in the formula, and its charge is %i, the polyatomic(s) want a total of %i electrons" % (are, int(polynum), int(charge), abs(int(polynum)*int(charge)))
          raw = "u"
          while raw != "":
            raw = raw_input("Press enter to continue")
          print "\n\nTake this number--the total amount of electrons that the polyatomic wants--and divide it by the number of metal atoms in the compound (the subscript under the metal element). This new number represents the number of electrons that each metal atom will give to each polyatomic ion, and this is the Roman numeral in the compound's name."
          print "\n To name the compound, add the first element name, the calculated Roman numeral number, and finally the name of the polyatomic. Here are some examples:\nMgSO3 is 'Mercury (II) Sulfate'\nCu(OH)2 is 'Copper (II) Hydroxide'"
    ###non-transition
    else:
      polyma = raw_input("\nDoes the second part of the formula (the part containing a nonmetal) contain a polyatomic ion?  A polyatomic ion consists of two or more atoms bonded to each other, forming an ion with a fixed charge. If there is just a single nonmetal in the formula following the metal, there is not a polyatomic. Here is a list of common polyatomic ions:\nhttps://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png")
      while polyma != "Yes" and polyma!= "yes" and polyma != "no" and polyma != "No":
        polyma = raw_input("Error. Please enter yes or no.")
      if polyma == "Yes" or polyma == "yes":
        print "\nTo name the compound, simply add the name of the metal and the name of the polyatomic ion. For example, Mg(NO3)2 is named Magnesium Nitrate, as NO3 is the polyatomic 'nitrate'"
      if polyma == "No" or polyma == "no":
        print "\nTo name the compound, simply add the two element names together, and replace the ending of the second element with '-ide'. Easy. Here are some examples:\nCaCl2 is 'Calcium chloride'\nK3N is 'Potassium Nitride'\nAlP is 'Aluminium Phosphide'"

###acid
elif a == 3:
    print "\nThis compound is an acid."
    acidpoly = raw_input("\nDoes the compound contain a polyatomic ion? (answer yes or no) A polyatomic ion consists of two or more atoms bonded to each other, forming an ion with a fixed charge. If there is just a single element following hydrogen, there is not a polyatomic. Here is a list of common polyatomic ions:\nhttps://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png")
    while acidpoly != "yes" and acidpoly != "no" and acidpoly != "Yes" and acidpoly != "No":
      acidpoly = raw_input("Error. Please enter yes or no: does your compound contain a polyatomic ion?")
    if acidpoly == "no" or acidpoly == "No":
      print "To name this compound, add the prefix 'hydro-' to the second element in the formula, replace the last part of the element's name (probably 'ine') with '-ic', and add the word acid. However, with some elements, the suffix '-ic' does not replace the element's ending and is instead added on to it (like sulfur)."
      raw = "u"
      while raw != "":
        raw = raw_input("Press enter to continue")
      print "\nHere are some examples:\nHCl is 'Hydrochloric acid'\nH2S is 'Hydrosulfuric acid'\nHI is 'Hydroiodic acid'"
      print "\nNotice that while the other two examples have one hydrogen, H2S has two. This is because both elements want a total of 8 valence electrons. Chlorine and Iodine have 7, and hydrogen has 1, so in the other examples, one of each element is needed to get 8. Sulfur, however, has 6 valence electrons, and therefore needs to bond with 2 hydrogens to get 8."
    elif acidpoly == "Yes" or acidpoly == "yes":
      print "Because there is a polyatomic, the prefix 'hydro-' is not added."
      ateite = raw_input("Look at the list of polyatomics. Does the polyatomic in your compound end in '-ate' or '-ite'?")
      while ateite != "ate" and ateite != "-ate"  and ateite != "-ite" and ateite != "ite":
        ateite = raw_input("Error. Please enter ate or ite.")
      if ateite == "-ate" or ateite == "ate":
        print "\nTo name the compound, replace the ending of the polyatomic (-ate) with the suffix '-ic' and add the word acid.\n***In the case of sulfate, it becomes sulfuric acid, not sulfic acid."
        raw = "u"
        while raw != "":
          raw = raw_input("Press enter to continue")
        print "\nHere is an example: HClO3 has the polyatomic ClO3. Looking at the polyatomic ions list, I know that this is 'chlorate'. Because the polyatomic ends in '-ate', I will add the suffix '-ic'. So, I can name it as 'Chloric acid'."
      elif ateite == "-ite" or ateite == "ite":
        print "To name the compound, replace the ending of the polyatomic (-ite) with the suffix '-ous' and add the word acid.\n***In the case of sulfite, it becomes sulfurous acid, not sulfous acid."
        raw = "u"
        while raw != "":
          raw = raw_input("Press enter to continue")
        print "\nHere is an example: HNO2 has the polyatomic NO2. Looking at the polyatomic ions list, I know that this is 'nitrite'. Because the polyatomic ends in '-ite', I will add the suffix '-ous'. So, I can name it as 'Nitrous acid'."
    
### HERE IS THE BIBLIOGRAPHY

###
###http://dl.clackamas.edu/ch104/lesson8naming_covalentcompounds.html
###https://s-media-cache-ak0.pinimg.com/originals/56/79/51/5679511593c7cbedc960ec156274aa67.png


        
    