class PersonalityTest:
    def __init__(self):
        self.questions = [
            "You prefer to spend your free time:",
            "When making decisions, you rely more on:",
            "You consider yourself to be more:",
            "In social situations, you tend to be:",
            "You are more comfortable with:",
            "You value:",
            "You prefer to work in a:",
            "You see yourself as:",
            "Your favorite type of weather is:",
            "Your ideal vacation destination is:",
            "Your preferred mode of transportation is:",
            "You feel most energized when:",
            "Your favorite type of music is:",
            "Your ideal way to relax is:",
            "You enjoy hobbies that involve:"
        ]
        self.options = [
            ["Reading a book", "Going for a hike", "Watching movies"],
            ["Logic and reason", "Intuition and gut feeling", "Seeking advice from others"],
            ["Introverted and reflective", "Outgoing and sociable", "Balanced and adaptable"],
            ["Observant and reserved", "Talkative and enthusiastic", "Diplomatic and empathetic"],
            ["Routine and structure", "Spontaneity and change", "Finding a middle ground"],
            ["Knowledge and intelligence", "Creativity and imagination", "Harmony and peace"],
            ["Quiet and organized environment", "Dynamic and collaborative workspace", "Flexible and adaptable setting"],
            ["Practical and analytical", "Dreamy and visionary", "Compassionate and understanding"],
            ["Sunny and warm", "Rainy and cozy", "Snowy and magical"],
            ["Historical cities and landmarks", "Tropical beaches and islands", "Countryside and nature retreats"],
            ["Car", "Bicycle", "Train"],
            ["Planning and organizing events", "Exploring new ideas and possibilities", "Helping others and making a difference"],
            ["Classical and instrumental", "Pop and upbeat", "Indie and alternative"],
            ["Meditating or practicing yoga", "Going for a run or exercise", "Spending time with friends and family"],
            ["Solving puzzles and brain teasers", "Creating art or crafting", "Cooking or baking"]
        ]

    def get_questions(self):
        return self.questions

    def get_options(self):
        return self.options

    def get_cake_type(self, answers):
        # Logic to determine the cake type based on user's answers...

      def get_cake_description(self, cake_type):
        descriptions = {
            "Vanilla Cake": "You are a Vanilla Cake! Just like this classic cake, you are simple yet elegant. You appreciate the little things in life and enjoy spending time with loved ones.",
            "Chocolate Cake": "You are a Chocolate Cake! Your rich and indulgent personality makes you irresistible to those around you. You have a deep passion for life and love to indulge in your favorite activities.",
            "Red Velvet Cake": "You are a Red Velvet Cake! Your vibrant personality and charm light up any room. You are bold and adventurous, always ready for new experiences.",
            "Carrot Cake": "You are a Carrot Cake! Just like this unique cake, you are full of surprises. Your warmth and kindness shine through, and you have a knack for bringing joy to others.",
            "Cheesecake": "You are a Cheesecake! Your smooth and creamy personality makes you a true delight to be around. You have a sophisticated taste and enjoy the finer things in life.",
            "Lemon Cake": "You are a Lemon Cake! Your zest for life and refreshing personality brighten everyone's day. You have a sunny disposition and always look on the bright side of things.",
            "Coconut Cake": "You are a Coconut Cake! Your exotic and tropical personality brings a taste of paradise wherever you go. You are laid-back and easygoing, enjoying life's simple pleasures.",
            "Black Forest Cake": "You are a Black Forest Cake! Your mysterious and complex personality keeps people guessing. You have a deep intensity and passion for the things you love.",
            "Funfetti Cake": "You are a Funfetti Cake! Your playful and colorful personality brings joy and laughter to those around you. You have a youthful spirit and love to embrace your inner child.",
            "Tiramisu": "You are a Tiramisu! Your sophisticated and refined personality makes you a true connoisseur of life's pleasures. You have a taste for the finer things and enjoy indulging in luxury.",
            "Angel Food Cake": "You are an Angel Food Cake! Your light and airy personality uplifts those around you. You have a gentle nature and a pure heart, always striving to spread love and positivity.",
            "Pineapple Upside-Down Cake": "You are a Pineapple Upside-Down Cake! Your unique and unconventional personality sets you apart from the crowd. You have a knack for turning things upside down and making them extraordinary.",
            "German Chocolate Cake": "You are a German Chocolate Cake! Your complex and layered personality is full of depth and richness. You have a strong sense of tradition and value your close relationships.",
            "Rainbow Cake": "You are a Rainbow Cake! Your vibrant and colorful personality shines brightly wherever you go. You embrace diversity and celebrate the beauty of individuality.",
            "Coffee Cake": "You are a Coffee Cake! Your comforting and warm personality makes you a reliable friend and confidant. You have a nurturing nature and enjoy creating a cozy atmosphere for others.",
        }
        return descriptions.get(cake_type, "Your personality is as unique as a custom-made cake! Unfortunately, we don't have a description for your result.")
