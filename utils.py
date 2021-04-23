
def auto_str(cls):
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls


def fillTextBoxAtStartup(combat_box, runes_box, converge_box):
    try:
        with open("iou.txt") as file:
            text = file.readlines()

            tmp = ''
            try:
                for i in range(9):
                    tmp += text[i]
            except IndexError:
                return False
            combat_box.insert('0.0', tmp[:-1])

            tmp = ''
            try:
                for i in range(9, 16):
                    tmp += text[i]
            except IndexError:
                return False
            runes_box.insert('0.0', tmp[:-1])

            tmp = ''
            try:
                for i in range(16, 17):
                    tmp += text[i]
            except IndexError:
                return False
            converge_box.insert('0', tmp)

        return True

    except FileNotFoundError:
        return False


def saveFromTextBoxToFile(combat_box, runes_box, converge_box):
    try:
        with open("iou.txt", 'w') as file:
            tmp = ''
            tmp += combat_box.get('0.0', 'end')
            tmp += runes_box.get('0.0', 'end')
            tmp += converge_box.get()
            file.write(tmp)
        return True
    except IndexError:
        return False
