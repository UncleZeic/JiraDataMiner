class SprintData:
    def __init__(self, sprint_id, name, velocity, bugs_throughtput, throughput, weeks=None, start_date=None,
                 end_date=None):
        self.id = sprint_id
        self.name = name
        self.velocity = velocity
        self.bugs_throughtput = bugs_throughtput
        self.throughput = throughput
        self.weeks = weeks
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return "Sprint {name}: velocity={velocity} per {weeks} weeks, throughput = {throughput}, {bugs_throughtput} " \
               "= bugs_throughtput ".format(name=self.name, velocity=self.velocity, weeks=self.weeks,
                                            throughput=self.throughput, bugs_throughtput=self.bugs_throughtput)
