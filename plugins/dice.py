class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_filter(self.dice)

    def dice(self, sender, message):
        # TODO(spark): Answer pong to VK API
        print(message)