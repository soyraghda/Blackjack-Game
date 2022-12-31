import random
from replit import clear
user_lost=False
pc_lost=False
def deal_card(user):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    num = random.choice(cards)
    return num

    
def check_total(cards):
    total=0
    total=sum(cards)
    if total==21 and len(cards)==2:
        return 0
    elif 11 in cards and total>21:
        cards.remove(11)
        cards.append(1)
    return total
    
def compare(user1,user2):
    if(sum(user1)>21):
        print("Computer won, you lost!")
    elif(sum(user1)==0):
        print("You won, Computer lost!")
    elif(sum(user2)==0):
        print("Computer won, you lost!")
    elif(sum(user2)>21):
        print("you won, computer lost!")
    elif(sum(user2)>sum(user1)):
        print("Computer won, you lost!")
    elif sum(user2)<sum(user1):
        print("You won, Computer lost!")
    elif(sum(user1)==sum(user2)):
        print("its a draw!")
    

def play_game():
    is_game_over=False
    user_cards=[]
    pc_cards=[]
    user_sum=0
    pc_sum=0
    answer=input("Type 'y' to get cards, type 'n' to pass \n")
    for _ in range(0,2):
        user_cards.append(deal_card(user_cards))
        pc_cards.append(deal_card(pc_cards))
    while not is_game_over:
        user_sum = check_total(user_cards)
        pc_sum = check_total(pc_cards)
        if user_sum >21 or user_sum==0 or pc_sum==0:
            is_game_over=True
        else:
            print(f"Your cards are: {user_cards}, score is {check_total(user_cards)}")
            print(f"Computer's first card is [{pc_cards[0]}]")
            
            answer=input("Type 'y' to get another card, type 'n' to pass \n")
            if(answer.lower()=="y"):
                user_cards.append(deal_card(user_cards))
            else:
                is_game_over=True
    while pc_sum<17 and pc_sum!=0:
            pc_cards.append(deal_card(pc_cards))
            pc_sum = check_total(pc_cards)
    
    compare(user_cards,pc_cards)    
    print(f"Computer cards are: {pc_cards}, score is {check_total(pc_cards)}")
    print(f"Your cards are: {user_cards}, score is {check_total(user_cards)}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y":
    clear()
    play_game()