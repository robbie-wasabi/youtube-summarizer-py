import sys
from text import summarize_text
from config import Config
import logging
from youtext import fetch_transcript


cfg = Config()


def configure_logging():
    logging.basicConfig(filename='log.txt',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    return logging.getLogger('AutoGPT')


def check_openai_api_key():
    """Check if the OpenAI API key is set in config.py or as an environment variable."""
    if not cfg.openai_api_key:
        print(
            Fore.RED +
            "Please set your OpenAI API key in config.py or as an environment variable."
        )
        print("You can get your key from https://beta.openai.com/account/api-keys")
        exit(1)


# def print_to_console(
#         title,
#         title_color,
#         content,
#         min_typing_speed=0.05,
#         max_typing_speed=0.01):
#     """Prints text to the console with a typing effect"""
#     global cfg
#     print(title_color + title + " " + Style.RESET_ALL, end="")
#     if content:
#         if isinstance(content, list):
#             content = " ".join(content)
#         words = content.split()
#         for i, word in enumerate(words):
#             print(word, end="", flush=True)
#             if i < len(words) - 1:
#                 print(" ", end="", flush=True)
#             typing_speed = random.uniform(min_typing_speed, max_typing_speed)
#             time.sleep(typing_speed)
#             # type faster after each word
#             min_typing_speed = min_typing_speed * 0.95
#             max_typing_speed = max_typing_speed * 0.95
#     print()


# def prompt_user():
#     """Prompt the user for input"""
#     print_to_console(
#         "Which topic would you like to know more about?",
#         Fore.GREEN,
#         "Select a number",
#     )


check_openai_api_key()
cfg = Config()
logger = configure_logging()

video_id = sys.argv[1]

text = fetch_transcript(video_id)
bullet_list = summarize_text(
    text, "create a numbered list of the main points in the following transcript")
print(bullet_list)

# selection = input("What would you like to know more about?")
