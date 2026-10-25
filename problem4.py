#Manufacturing Orders
#A factory receives the following orders. Each order takes one time slot to process, and profit is earned only if the order is completed by its deadline.


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
    ("M1", 4, 200),
    ("M2", 1, 80),
    ("M3", 2, 150),
    ("M4", 2, 100),
    ("M5", 3, 120),
    ("M6", 1, 60),
    ("M7", 4, 90)
]

schedule, profit = job_sequencing(jobs)
print("Schedule:", schedule)
print("Maximum Profit:", profit)
