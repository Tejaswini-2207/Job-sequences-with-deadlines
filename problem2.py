#Software Company Tasks
#A software company has five tasks. Each task requires one time slot, and the company earns the listed profit only if the task finishes before its deadline.


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
    ("T1", 2, 80),
    ("T2", 1, 60),
    ("T3", 3, 100),
    ("T4", 2, 40),
    ("T5", 1, 30)
]

schedule, profit = job_sequencing(jobs)
print("Schedule:", schedule)
print("Maximum Profit:", profit)
