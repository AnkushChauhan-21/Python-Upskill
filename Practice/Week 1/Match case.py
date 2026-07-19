# Match case(switch case) is a control flow statement that allows a value to  be tested for equality against the list of values.

command = input("enter the command for ex: ('start','stop','resume','print'): ").lower()

match command:
    case"start":
        print("the code is starting now :----- ")
    case"stop":
        print("the code is stopped now : -----")
    case"resume":
        print("the stopped code is resuming again: -----")
    case"print":
        print("printig the written code now as per instruction:-0----")
    case _:
        print("Nothing is written here please choose one of the command here :___-")


def is_weekend(day):
    match day.lower():
        case "sunday" | "saturday" :
            return True
        case "monday" | "tuesday" | "wednesday" | "thrusday" | "friday":
            return False
        case _:
            print("Please use a valid weekday or weekend to check it : <-_->")
        


print(is_weekend("sunday"))
print(is_weekend("whoop"))
print(is_weekend("friday"))

    
