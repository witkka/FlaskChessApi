from flaskr.chess.CONSTANTS import FILE_NAMES, RANK_NAMES, SQUARE_NAMES

class Knight:
    def __init__(self, field):
        self.field = field

    def get_numbers(self):
        pattern_number = [-2, -1, 1, 2, 2, 1, -1, -2]
        number_indx = RANK_NAMES.index(self.field[1])
        temp = []
        for elem in pattern_number:
            if number_indx + elem >= 0 and number_indx + elem <= 7:
                temp.append(RANK_NAMES[number_indx + elem])
            else:
                temp.append(None)
        return temp

    def get_letters(self):
        pattern_letter = [-1, -2, -2, -1, 1, 2, 2, 1]
        letter_indx = FILE_NAMES.index(self.field[0])
        temp = []
        for elem in pattern_letter:
            if letter_indx + elem >= 0 and letter_indx + elem <= 7:
                temp.append(FILE_NAMES[letter_indx + elem])
            else:
                temp.append(None)
        return temp


    def get_available_moves(self):
        letters = self.get_letters()
        numbers = self.get_numbers()
        return [(l+n) for l, n in zip(letters, numbers) if l!=None and n!=None]

