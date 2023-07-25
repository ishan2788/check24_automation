from features import Login

if __name__ == "__main__":
    Login().newuser()
    print("Testcase 1: User Onboarding Executed Successfully")
    Login().trip()
    print("Testcase 2: Trip feature Executed Successfully")
    Login().hotel()
    print("Testcase 3: Hotel search feature Executed Successfully")
    Login().rental_car()
    print("Testcase 4: Rental Car feature Executed Successfully")
    Login().flights()
    print("Testcase 4: Search Flights feature Executed Successfully")
    print("Congratulations..!!! ALL TEST CASES Executed Successfully")
