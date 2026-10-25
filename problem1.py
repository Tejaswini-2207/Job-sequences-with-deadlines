#A college gives students rewards for completing assignments. Each assignment takes exactly one hour, and only one assignment can be completed per hour. An assignment earns its reward only if completed by its deadline.


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

    schedule = [
        (slot, slots[slot])
        for slot in range(1, len(slots))
        if slots[slot] is not None
    ]

    return schedule, total_profit


jobs = [
    ("A", 2, 100),
    ("B", 1, 50),
    ("C", 2, 30),
    ("D", 1, 20),
    ("E", 3, 10)
]

schedule, profit = job_sequencing(jobs)
print("Schedule:", schedule)
print("Maximum Profit:", profit)
