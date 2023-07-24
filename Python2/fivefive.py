class TorKham:
    def __init__(self, input_list) -> None:
        self.input_list = input_list
        self.running_list = self.input_list
        self.used_list = []
        self.current_list = []
        self.run = False

    def start(self) -> None:
        self.run = True
        while self.run:
            for index, data in enumerate(self.running_list):
                if data[0] == 'X':
                    self.run = False

                elif data[0] == 'R':
                    self.restart(index)
                    break

                elif data[0] == 'P':
                    self.check_word(data[2:])

                else:
                    self.run = False
                    print(f'\'{data}\' is Invalid Input !!!')
                    break

                if index == len(self.running_list)-1:
                    self.run = False
                    break
                    
    def check_word(self, new_word):
        if new_word.lower() == 'nectarine':
            print('\'nectarine\' -> game over')
            return

        for word in self.used_list:
            if (new_word.lower() in word.lower()) or (word.lower() in new_word.lower()):
                print(f'\'{new_word}\' -> game over')
                return
        
        self.current_list.append(new_word)
        self.used_list.append(new_word)
        print(f'\'{new_word}\' -> {self.current_list}')

    def restart(self, list_start=0):
        self.running_list = self.running_list[list_start+1:]
        self.current_list = []
        print('game restarted')

print('*** TorKham HanSaa ***')
game = TorKham(input('Enter Input : ').split(','))
game.start()