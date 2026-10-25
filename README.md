# Job Sequencing with Deadlines — Greedy Algorithm

## 📌 Overview

This repository contains Python implementations of the **Job Sequencing with Deadlines problem** using the Greedy Algorithm.

The objective is to select and schedule jobs to maximize total profit while satisfying their deadlines.

Each job has:
- A unique job ID.
- A deadline.
- A profit earned if the job is completed by its deadline.

In the standard version, each job takes exactly one unit of time, and only one job can be executed in a time slot.

## 🎯 Objectives

- Understand the Job Sequencing with Deadlines problem.
- Identify greedy algorithm scenarios.
- Schedule jobs to maximize total profit.
- Implement the algorithm using Python.
- Analyze time and space complexity.
- Practise scenario-based Advanced Algorithm Design questions.

## 🔍 How to Recognize This Problem

Look for these clues in a problem statement:

1. Every job has a deadline.
2. Every job has a profit or reward.
3. Each job requires one unit of time.
4. Only one job can be performed at a time.
5. The goal is to maximize total profit while meeting deadlines.

**Example:** A software company has several tasks with deadlines and rewards. It must choose which tasks to complete to earn the maximum possible profit.

## 🧠 Greedy Strategy

The algorithm follows these steps:

1. Sort all jobs by profit in descending order.
2. Find the maximum deadline.
3. Create time slots from 1 to the maximum deadline.
4. Consider each job in descending order of profit.
5. Place the job in the latest available slot at or before its deadline.
6. Skip the job if no valid slot is available.
7. Calculate the total profit of scheduled jobs.

Placing a job as late as possible preserves earlier slots for jobs with tighter deadlines.

## 📝 General Pseudocode

```text
JOB-SEQUENCING(jobs):

    sort jobs by profit in descending order

    max_deadline = maximum deadline
    create empty time slots from 1 to max_deadline
    total_profit = 0

    for each job in jobs:
        for slot from min(job.deadline, max_deadline) down to 1:
            if slot is empty:
                schedule job in slot
                total_profit += job.profit
                break

    return schedule, total_profit
```

## 💻 Python Implementation

```python
def job_sequencing(jobs):
    # Each job: (job_id, deadline, profit)

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
    ("E", 3
