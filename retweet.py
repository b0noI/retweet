from chatgpt import Conversation


def test():
    conversation = Conversation()

    # Stream the message as it arrives.
    for chunk in conversation.stream("We are going to start a conversation. I will speak English and you will speak Portuguese."):
        print(chunk, end="")
        sys.stdout.flush()


if __name__ == "__main__":
    test()
