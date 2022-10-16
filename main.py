#Author: Nicolas Son
#E-Mail: NicolasSon6@gmail.com
#Purpose: Take in the input weight of KG / LB and if it is a Feline or Canine, then return appropriate drug dosages.
#Future Challenge: Allow the user to pick specific category (to prescribe medicine, to inject anesthesia, to give medicine, etc.,
#in different classes to save memory.)

###working, returns first decimal place,
def lbToKgConvert(pounds):
    kg = pounds * .45359237
    kg = round(kg, 1)
    return kg


operating = True

#nested while loop, o(n^2) at the start while deciding pounds
while operating:
    #placeholders so that if you pick kg or lb, the other is not undefined
    lbWeight = 0
    kgWeight = 0

    operating = False
    speciesCheck = input("Is your client a Feline or a Canine? Type 'F' or 'C'.\n").lower()
    weightConfirm = True
    while weightConfirm:
        lbOrKg = input("Are you measuring in pounds (lb) or kilograms (kg)?").lower()
        if lbOrKg == "lb":
            lbWeight = float(input("How much does your client's animal weigh in pounds (lbs)?\n"))
            kgWeight = lbToKgConvert(lbWeight)
        elif lbOrKg == "kg":
            kgWeight = float(input("How much does your client's animal weigh in kilograms (kg)?\n"))
        else:
            print("Please restart and insert LB or KG next time.")
            exit()
            # redundant, see above lines if lbOrKg == "lb":
        if lbWeight >= 18.0 or kgWeight >= 8.1 and speciesCheck == "F":
            weightCheck = input("You listed that the feline is equal to or over 18lbs / 8.1 kgs.. If this is correct, type 'Y' to continue.\n").lower()
            if weightCheck == "y":
                break
            else:
                print("Please restart and insert the correct weight.")
                exit()

        elif lbWeight >= 100.0 or kgWeight >= 45.3 and speciesCheck == "C":
            weightCheck = input("You listed that the canine is equal to or over 100lb / 45.3 kg. If this is correct, type 'Y' to continue.\n").lower()
            if weightCheck == "y":
                break
            else:
                print("Please restart and insert the correct weight.")
                exit()
        else:
            weightConfirm = False

    #this would override kgWeight if you picked kgWeight, and lb = 0. kgWeight = lbToKgConvert(lbWeight)

    if speciesCheck == "f":
        felineDex = round(kgWeight * .04, 3)
        felineMidaz = round(kgWeight * .04, 3)
        felineTorb = round(kgWeight * .02, 3)

        print(f"\n\nMeasurements for a {lbWeight}lb or {kgWeight}kg Feline. Every dosage is rounded to the 3rd decimal place."
              f"\nSQ = Subcutaneous, IV = Intravenous, IM = Intramuscular."
              f"\nKitty Magic (Sedatives)"
              f"\nCombine Dex, Midaz, and Torb all into one syringe to sedate. Inject by IV or IM."
              f"\nDexamethasone Dosage for Feline: {felineDex} mL"
              f"\nMidazolam Dosage for Feline: {felineMidaz} mL"
              f"\nButorphanol Dosage for Feline: {felineTorb} mL"
              f"\nAntisedan Dosage for Feline: {felineDex} mL, injected by IM."
              )


        print("\n\nPre-Med")
        felineHydro = round(kgWeight * 0.05, 3)
        felineCerenia = round(kgWeight / 10, 3)
        print(f"\nHydromorphine Dosage for Feline to be injected IM: {felineHydro} mL"
              f"\nCerenia Dosage for Feline to be injected SQ: {felineCerenia} mL"
              )

        print("\nInduction")
        felineProp = round(kgWeight * .4, 3)
        print(f"\nAll of these are to be injected by IV."
              f"\nMidazolam Dosage for Feline: {felineMidaz} mL"
              f"\nPropofol Dosage for Feline: {felineProp} mL"
              )

        print("\nPost-Op")
        felineOnsior = round(kgWeight * .1, 3)
        felineBupe = round(kgWeight * .04, 3)
        felineBupeSR = round(kgWeight * .03, 3)
        print(f"\nAll of these are to be injected by SQ. However, pick only ONE to inject."
        f"\nOnsior Dosage for Feline: {felineOnsior} mL"
        f"\nBupe Dosage for Feline: {felineBupe} mL"
        f"\nBupe SR Dosage for Feline: {felineBupeSR} mL"
              )

    elif speciesCheck == "c":
        canineHydro = round(kgWeight * .05, 3)  #IM
        canineCerenia = round(kgWeight * .1, 3)  #SQ
        print(f"\n\nMeasurements for a {lbWeight}lb or {kgWeight}kg Canine. Every dosage is rounded to the 3rd decimal place."
              f"\nSQ = Subcutaneous, IV = Intravenous, IM = Intramuscular."
              f"\n\nPre-Med"
              f"\nHydromorphone Dosage for Canine: {canineHydro} mL, injected by IM"
              f"\nCerenia Dosage for Canine: {canineCerenia} mL, injected by SQ"
              )

        canineMidaz = round(kgWeight * .04, 3)
        canineProp = round(kgWeight * .4, 3)
        print(f"\nInduction"
              f"\nMidazolam Dosage for Canine: {canineMidaz} mL, injected by IV"
              f"\nPropofol Dosage for Canine: {canineProp} mL, injected by IV"
              )

#if == 15, rimadyl
        canineMelox = round(kgWeight * .04, 3)  #SQ
        canineRima = round(kgWeight * .088, 3)  #SQ
        canineBupe = round(kgWeight * .04, 3) #SQ

        if lbWeight < 15:
            print(f"\nPost-Op"
                  f"\nMeloxicam Dosage for Canine Under 15 Pounds: {canineMelox} mL, injected by SQ"
                  f"\nBuprenorphine Dosage for Canine: {canineBupe} mL, injected by SQ"
                  )
        else:
            print(f"\nPost-Op"
                  f"\nRimadyl Dosage for Canine 15 Pounds and Above: {canineRima} mL, injected by SQ"
                  f"\nBuprenorphine Dosage for Canine: {canineBupe} mL, injected by SQ")

    else:
        operating = True
        print("Incorrect input. Please type 'C' if it is a Canine, or 'F' if it is a Feline.")
