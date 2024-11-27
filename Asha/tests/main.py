import sys
import os
import time
from Asha.twitter_automation import TwitterAutomation


def initialization_effect():
    effects = [
        "[Start-up] Initializing 'Asha The Dream Catcher'...",
        "[Start-up] Loading whimsical tales...",
        "[Start-up] Spinning the web of dreams...",
        "[Start-up] Finalizing the dream realm...",
        "[Start-up] 'Asha The Dream Catcher' is now ready to capture and share dreams!"
    ]
    for effect in effects:
        print("\n" * 3, end="")
        print(effect)
        time.sleep(1)


def main():
    initialization_effect()

    twitter_bot = TwitterAutomation()
    tweet_counter = 1
    used_stories = set()

    while True:
        try:
            # Generate a non-repeating story about a dream
            story_components = twitter_bot.generate_unique_dream_story(used_stories)
            twitter_bot.post_tweet(tweet_counter, story_components)

            tweet_counter += 1
            time.sleep(2)  # Pause for 2 seconds before generating the next tweet

        except Exception as e:
            print(f'❌ [Error] {e}')
            time.sleep(1.5)  # Short delay before retrying on error


if __name__ == "__main__":
    main()
