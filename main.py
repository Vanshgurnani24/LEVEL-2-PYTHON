import re #re or regular expression library provides a set of powerful regular expression facilities
import long_responses as long


#function that checks the probability that the message is a corresponding message
def message_probability(user_message,reconginzed_words,single_response=False,required_words=[]):
    message_certainity=0
    has_required_words=True

    #counts how many words are present in each predefined message
    for word in user_message:
        if word in reconginzed_words:
            message_certainity+=1
    
    
    #Calculate the percent of recoginzed words in a user message
    percentage=float(message_certainity)/float(len(reconginzed_words))

    #Checks that required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break


    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0 #means nothing really matched so it will return the lowest response
    


def check_all_messages(message):
    highest_prob_list={} #an empty dictionary

    #This function simplifies adding items to our dictionary
    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list #referred as non local so we can use it inside function
        highest_prob_list[bot_response]=message_probability(message,list_of_words,single_response,required_words)


    #Responses--------------. Make sure response is in lower case as user input is converted to lower case too.
    response('Hello!',['hello','hi','ssup','heya','hey there'],single_response=True)
    response('I\'m doing fine. What about you?',['how', 'are', 'you','doing'],required_words=['how'])
    response('Thank You!!!!!',['i','like','future','vision'],required_words=['future','vision'])
    response(long.response_drinking,['do','you','like','to','drink'],required_words=['drink','you'])



    best_match=max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unkown() if highest_prob_list[best_match]<1 else best_match



def get_response(user_input):
    split_message=re.split(r'\s+|[,;?!.-]\s*',user_input.lower()) #split the message into array so we can analyze each word separately from user input. r'\s+|[,;?!.-]\s*' removes all the symbols from the messages to allow use to recognize clean words easily
    response=check_all_messages(split_message)
    return response


#Testing the response system
while True: #infinite while true loop so we can always get new responses
    print('Bot: '+get_response(input('You: ')))

