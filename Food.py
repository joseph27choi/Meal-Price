# Module for Food class


### START

class Food:
    def __init__(self, name):
        '''
        :param: the name of the food, inputted in any style
        '''
        self.name = name


    # methods

    # gets the titlecase version of user input
    def get_title(self) -> str:
        '''
        :param lower_inp: lowercase user input
        :type lower_inp: str
        :returns: a dictionary key that is titlecased
        :rtype: str
        '''
        # check word count
        word_list = self.name.split()

        # initialize empty dictionary key
        dict_key = ""

        # copy by value
        for i in range(0, len(word_list)):
            # best i could do in python :(
            word_list[i] = word_list[i][0].upper() + word_list[i][1:len(word_list[i])]
            # concatenate words
            if (i < len(word_list) - 1):
                dict_key += word_list[i] + ' '
            else:
                dict_key = dict_key + word_list[i]

        return dict_key

    # gets the price of the food
    def get_price(self):
        key = self.get_title()
        return MENU[key]

    # gets the name of the food
    def get_name(self):
        return self.name

    # gets all the attributes of the object and packs it up into a dictionary
    def get_members(self):
        member_dict = {
            "name": self.name,
            "price": self.get_price(),
            "title": self.get_title()
        }
        return member_dict

    # sets the name of the food to something else
    def set_name(self, new_name):
        self.name = new_name
        return

### END