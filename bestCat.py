def catGenerator():
    list =[]
    colors = ['Orange', 'Black', 'White','Calico','Brown','Siamese','Russian Blue']
    fluff = ['Short','Medium','Long','Curly','Naked']
    eyes = ['Green','Blue','Yellow','Two Colors']
    tail = ['Long tail','Short tail']
    gender = ['Girl','Boy']
    fattie = ['Chubby','Medium','Skinny']
    name = '' 

    ##GENDER STEP
    ans1 = ''
    while True:
        ans1 = input(f'Lets start with the gender! Select one:{gender}  ').lower()
        ans1 = ans1.capitalize()
        if ans1 in gender:
            list.append(ans1)
            break
        else:
            print('Please insert a valid answer meow!')
            continue
    print(f'This is what your current cat looks like! {list}')

    ##FATIE STEP
    ans2 = ''
    while True:
        ans2 = input(f'Its a chonker or a skinny? Select one: {fattie}').lower()
        ans2 = ans2.capitalize()
        if ans2 in fattie:
            list.append(ans2)
            break
        else:
            print('Please insert a valid answer meow!')
            continue
    print(f'This is what your current cat looks like! {list}')

    ##FLUFF STEP
    ans3 =''
    while True:
        ans3 = input(f'What kind of fluff it will have? Select one: {fluff}').lower()
        ans3 = ans3.capitalize()
        if ans3 in fluff:
            list.append(ans3)
            break
        else:
            print('Please insert a valid answer meow!')
            continue
    print(f'This is what you current cat looks like! {list}')

    ##COLOR STEP
    ans4 =''
    while True:
        ans4 = input(f'What color it will be? Select one: {colors}').lower()
        ans4 = ans4.capitalize()
        if ans4 in colors:
            list.append(ans4)
            break
        else:
            print('Please insert a valid answer meow!')
            continue
    print(f'This is what your current cat looks like! {list}')

    ##EYES STEP
    ans5 =''
    while True:
        ans5 = input(f'What eye color it will have? Select one: {eyes}').lower()
        ans5 = ans5.capitalize()
        if ans5 in eyes:
            list.append(ans5)
            break
        else:
            print('Please insert a valid answer meow!')
            continue
    print(f'This is what your current cat looks like! {list}')

    ##TAIL STEP
    ans6 =''
    while True:
        ans6 = input(f'What kind of tail it will have? Select one: {tail}').lower()
        ans6 = ans6.capitalize()
        if ans6 in tail:
            list.append(ans6)
            break
        else:
            print('Please insert a valid answer meow!')
            continue
    print(f'This is what your current cat looks like! {list}')

    ##NAME STEP 
    name = input('Finally, give it a name!').lower()
    name = name.capitalize()
    list.append(name)

    ##FINAL
    print(f'{name} is finished meow! How cute! This is how it looks like: {list[0:6]}')
            
            



inp = '' 
while True:
    inp = input('Are you ready to meet your new cat meow?  ').lower()
    if inp == "Yes" or inp == "yes":
        print('Cool, lets go meow!')
        catGenerator()
        break
    elif inp == "No" or inp == "no":
        print('Okay, see you next time meow!')
        break
    else:
        print('Sorry, say again meow?')
        continue





