#General Job Scheduling
#You are given n jobs. Each job contains:
#A unique job ID
# A deadline
# A profit
#Every job takes one unit of time, and a job earns its profit only if it is scheduled by its deadline. Only one job can occupy a time slot.

#Write an algorithm that returns:
# The selected jobs in chronological order.
# The maximum total profit.
# The time complexity.
#Your implementation should handle an empty job list and jobs with deadlines greater than the number of jobs.


def job_sequencing(jobs):
    # Each job is (job_id, deadline, profit).
    # Assume non-negative deadlines and profits.
    if not jobs:
        return [], 0

    jobs = sorted(jobs, key=lambda job: job[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    for job_id, deadline, profit in jobs:
        latest_slot = min(deadline, len(jobs))

        for slot in range(latest_slot, 0, -1):
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
