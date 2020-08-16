def find_password2(range_start, range_stop):
    final_potential_password = list()
    for maybe_password in range(range_start, range_stop+1):
        password_list = [int(i) for i in str(maybe_password)]
        code_ok = None
        if len(set(password_list)) < 6:
          code_ok = True
          previous_i = password_list[0]
          n = 1
          for i in password_list[1:]:
            if i < previous_i:
              code_ok = False
            else:
                if i == previous_i:
                    n = n + 1
                    if n % 2 == 1:
                        code_ok = False
                    else:
                        code_ok = True
                else:
                    n = 1
            previous_i = i
          if code_ok == True:
            #print('new potential password:' + str(maybe_password))
            final_potential_password.append(maybe_password)
    print('# of potential passwords: ' + str(len(final_potential_password)))

find_password2(125730, 12800)

for i in range(111111,111112):
    print(i)

4 % 2
