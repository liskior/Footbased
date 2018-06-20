class IntegrationFilter(object):
    PARAM = 10

    def init(self, initial_values):
        assert(len(initial_values) == self.PARAM)
        self.mean = float(sum(initial_values)) / self.PARAM

    def feed(self, number):
        weight = 1. / self.PARAM
        self.mean = self.mean * (1 - weight) + number * weight

    def get_mean(self):
        return self.mean
