import random


class TwitterAutomation:
    def __init__(self):
        self.tweets = []

    def generate_dream_story(self):
        """Generates a fantasy dream story."""
        adjectives = ["wonderful", "magical", "mysterious", "fantastic"]
        creatures = ["unicorn", "dragon", "fairy", "wizard"]
        places = ["enchanted forest", "mystic mountain", "dreamy valley", "starry night"]
        actions = ["flew over", "danced with", "explored", "found a hidden treasure in"]

        story = f"Last night, in a {random.choice(adjectives)} dream, I {random.choice(actions)} a {random.choice(creatures)} in the {random.choice(places)}."
        self.tweets.append(story)
        return story

    def post_tweet(self, tweet_counter, story):
        """Simulates posting a tweet."""
        print(f"Tweet {tweet_counter}: {story}")