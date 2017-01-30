class Logger:
    def __init__(self):
        print("init")
        self.log_file = "/home/pi/log.txt"

    def append(self, string: str):
        print("append")
        with open(self.log_file, "a") as log:
            log.write("{}\n".format(string))

    def empty_file(self):
        print("empty_file")
        log = open(self.log_file, 'w')
        log.close()

    def read_file(self):
        with open(self.log_file) as log:
            return log.read()
