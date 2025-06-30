def game():
    while True:
        import random
        target=random.randint(1,10)
        count=1
        print("\n\t\t----------START GAME----------")
        while count<=10:
            try:
                guess=int(input("\n👉Guess the number between 1 to 10 : "))
                if(guess==target):
                    print(f"\n||🎉 Congratulations! You guessed the number in {count} attempt(s). 🎉||")
                    break
                elif guess <1 or guess >10:
                    print("\n!!🙄 Number out of Range. Please guess between 1 to 10 🙄!!")
                    continue
                else:
                    print(f"\n!!😢 You guess wrong number.Please try again. (You have {10-count} attempt left) 😢!!")      
            except ValueError as val:
                print("!! Please Enter Valid Number !!")
                continue
            count+=1
        play_again=input("\nEnter y to play again, or press other key to exit 🔁 : ").lower()
        if play_again!="y":
            print("\n\t\t----------👋Thank You👋----------")
            break
game()
