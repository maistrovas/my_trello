from .trello_command_abc import TrelloCommand
import urllib.request
from PIL import Image
import timeit
import time

class NextCheatMeal(TrelloCommand):
    """
    Command check out my cheat day and show what new restaurant I plan to visit this week. Additionally it
    open the picture of meal I plan to try.
    """
    command_name = 'cheat_meal'
    CHEAT_DAY = 'Saturday'

    def execute(self):
        cheat_day_list = self.trello_client.get_weekly_tasks_list(self.CHEAT_DAY)
        cheat_meal_card = NextCheatMeal.find_card(cheat_day_list)
        if cheat_meal_card is None:
            print("Unfortunately you forget to plan new food adventure this {}.".format(self.CHEAT_DAY))
        else:
            photo = cheat_meal_card.get_attachments()[0]
            cheat_meal_file_name = "cheat_meal.png"
            NextCheatMeal.store_image_locally(photo, cheat_meal_file_name)
            print("This {} you are going to try: \n{}. \nHere is additional info about the place: \n{}".format(
                self.CHEAT_DAY, cheat_meal_card.name, cheat_meal_card.description))
            NextCheatMeal.open_photo_in_viewer(cheat_meal_file_name)

    @staticmethod
    def find_card(cheat_day_list):
        cheat_meal_card = None
        start_time = time.time()
        cards = cheat_day_list.list_cards()
        for card in cards:
            if "Place:" in card.name:
                cheat_meal_card = card
                break
        print("--- %s seconds ---" % (time.time() - start_time))
        return cheat_meal_card

    @staticmethod
    def store_image_locally(image, cheat_meal_file_name):
        urllib.request.urlretrieve(image.url, cheat_meal_file_name)

    @staticmethod
    def open_photo_in_viewer(cheat_meal_file_name):
        with Image.open(cheat_meal_file_name) as img:
            img.show()
