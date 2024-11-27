import random
import time


class TwitterAutomation:
    def __init__(self):
        self.adjectives = [
            "mysterious", "enchanting", "surreal", "unforgettable", "magical",
            "captivating", "ethereal", "spellbinding", "dreamy", "phantasmagorical",
            "wondrous", "bewitching", "otherworldly", "mystical", "radiant",
            "luminous", "celestial", "mythical", "transcendent", "mesmerizing",
            "serene", "glorious", "arcane", "harmonious", "ghostly"
        ]
        self.themes = [
            "under a sparkling night sky", "in a land of dreams", "amidst twinkling stars",
            "in a fantastical realm", "within a mystical forest", "on a distant moon",
            "in a floating castle", "beneath the shimmering sea", "among the whispering winds",
            "above the clouds", "in an enchanted desert", "through a portal to another dimension",
            "in a land of talking animals", "within a crystal cave", "on a magical island",
            "in a fairy-tale village", "in a dragon's lair", "within a spellbound library",
            "in a garden of glowing flowers", "within a labyrinth of mirrors", "in a forgotten temple"
        ]
        self.char_traits = [
            "brave", "curious", "whimsical", "wise", "naive", "adventurous",
            "meticulous", "kind-hearted", "mischievous", "valiant"
        ]
        self.char_roles = [
            "hero", "guardian", "wanderer", "explorer", "seeker",
            "sage", "warrior", "dreamer", "mage", "prince"
        ]
        self.actions = [
            "discovered hidden secrets", "fought valiant battles", "explored uncharted territories",
            "befriended magical creatures", "solved ancient puzzles", "uncovered lost treasures",
            "embarked on epic quests", "revealed timeless mysteries", "shared stories of valor",
            "witnessed divine wonders", "crafted powerful spells", "brought harmony to realms"
        ]
        self.emojis = ["🌙", "🌟", "✨", "💫", "🌠", "🌌", "🌈", "🌊", "🌲", "🌸", "🦄", "🐉", "🧙", "🧚", "🔮", "🍄", "🦋", "🌿"]

    def generate_unique_dream_story(self, used_stories):
        attempts = 0
        while attempts < 100:  # Attempt to find a unique story up to 100 times
            story_components = self._create_dream_story()
            story_hash = tuple(story_components)  # Use a tuple to make an immutable hashable type
            if story_hash not in used_stories:
                used_stories.add(story_hash)
                return story_components
            attempts += 1

        return ["Asha is resting now, more dreams to come soon!"]

    def _create_dream_story(self):
        theme = random.choice(self.themes)
        adjective = random.choice(self.adjectives)
        char_trait = random.choice(self.char_traits)
        char_role = random.choice(self.char_roles)
        action = random.choice(self.actions)
        emojis = random.sample(self.emojis, 3)  # Ensure unique emojis in each story

        story_components = [
            "\n🌟 **Dream Story by Asha** 🌟",
            f"✨ **Captured Scene** ✨: {theme}",
            f"🏰 **Character** 🏰: A {char_trait} {char_role}",
            f"🌀 **Adventure** 🌀: The {char_role} {action}.",
            f"🌠 **Journey** 🌠: They ventured through {adjective} realms adorned with {emojis[0]}, {emojis[1]}, and {emojis[2]}.",
            "Asha watched in awe as the dreamer journeyed through this fantastical tale."
        ]
        return story_components

    def post_tweet(self, tweet_counter, story_components):
        for component in story_components:
            print(component)
            time.sleep(2)
        print("\n")
