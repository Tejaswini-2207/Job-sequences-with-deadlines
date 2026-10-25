#Cloud Computing Jobs

#A cloud service provider has jobs to execute. Each job takes one time unit, and each earns profit only if completed by its deadline.


def job_sequencing(jobs):
    jobs = sorted(jobs, key=lambda job: job[2], reverse=True)
    max_deadline = max((job[1] for job in jobs), default=0)
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    for job_id, deadline, profit in jobs:
        for slot in range(min(deadline, max_deadline), 0, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                break

    schedule = [(i, slots[i]) for i in range(1, len(slots))
                if slots[i] is not None]
    return schedule, total_profit


jobs = [
    ("J1", 2, 70),
    ("J2", 1, 110),
    ("J3", 3, 50),
    ("J4", 2, 90),
    ("J5", 3, 40),
    ("J6", 1, 30)
]

schedule, profit = job_sequencing(jobs)
print("Schedule:", schedule)
print("Maximum Profit:", profit)
