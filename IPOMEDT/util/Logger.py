class Logger:
    def __init__(self):
        self.log_file = "/home/pi/log.txt"

    def append(self, string: str):
        with open(self.log_file, "a") as log:
            log.write("{}\n".format(string))

    def empty_file(self):
        log = open(self.log_file, 'w')
        log.close()

    def read_file(self):
        with open(self.log_file) as log:
            return log.read()
