def suggest_maintenance_action(engine_id: int, rul: int) -> dict:
    """
    Suggests a maintenance action based on the engine's Remaining Useful Life (RUL).

    Args:
        engine_id (int): The ID of the engine.
        rul (int): Remaining Useful Life of the engine in cycles.

    Returns:
        dict: A dictionary containing the engine ID, recommended action, and priority level.
              - 'STOP' if RUL <= 20 (critical priority)
              - 'REPAIR' if RUL <= 60 (high priority)
              - 'MONITOR' otherwise (low priority)
    """
    if rul <= 20:
        return {"engine_id": engine_id, "action": "STOP", "priority": "critical"}
    elif rul <= 60:
        return {"engine_id": engine_id, "action": "REPAIR", "priority": "high"}
    else:
        return {"engine_id": engine_id, "action": "MONITOR", "priority": "low"}

def schedule_maintenance_task(engine_id: int, action: str, priority: str, rul: int) -> dict:
    """
    Schedules a maintenance task based on action type, priority, and Remaining Useful Life (RUL).

    Each engine is assumed to complete 5 cycles per day. The RUL is converted to days to determine
    an appropriate scheduling window.

    Args:
        engine_id (int): The ID of the engine.
        action (str): The recommended maintenance action ('STOP', 'REPAIR', 'MONITOR').
        priority (str): The urgency level ('critical', 'high', 'low').
        rul (int): Remaining Useful Life of the engine in cycles.

    Returns:
        dict: Contains scheduling information including:
            - engine_id
            - scheduled_action
            - scheduled_time (recommended time window)
            - priority
            - days_remaining (derived from RUL)
    """
    cycles_per_day = 20
    days_remaining = rul // cycles_per_day

    if priority == "critical" or rul <= 20:
        time_slot = "IMMEDIATE (0–1 days)"
    elif days_remaining <= 3:
        time_slot = "Schedule within 3 days"
    elif days_remaining <= 7:
        time_slot = "Schedule within 7 days"
    else:
        time_slot = "Monitor – maintenance not needed this week"

    return {
        "engine_id": engine_id,
        "scheduled_action": action,
        "scheduled_time": time_slot,
        "priority": priority,
        "days_remaining": days_remaining
    }

def estimate_maintenance_cost(action: str, priority: str) -> dict:
    """
    Estimates the cost and labor time required to perform a maintenance action.

    Cost is based on base action cost multiplied by a priority factor.
    Labor hours are predefined per action.

    Args:
        action (str): The maintenance action ('STOP', 'REPAIR', or 'MONITOR').
        priority (str): The urgency level ('critical', 'high', or 'low').

    Returns:
        dict: Contains:
            - action
            - priority
            - estimated_cost_usd (float)
            - labor_hours (int)
    """
    base_costs = {
        "STOP": 10000,
        "REPAIR": 5000,
        "MONITOR": 0
    }

    multiplier = {
        "critical": 1.5,
        "high": 1.2,
        "low": 1.0
    }

    labor_hours = {
        "STOP": 8,
        "REPAIR": 4,
        "MONITOR": 0
    }

    cost = base_costs.get(action, 1000) * multiplier.get(priority, 1.0)

    return {
        "action": action,
        "priority": priority,
        "estimated_cost_usd": round(cost, 2),
        "labor_hours": labor_hours.get(action, 2)
    }

def assign_maintenance_staff(labor_hours: int, priority: str) -> dict:
    """
    Assigns staff based on the number of labor hours and maintenance priority.

    Uses fixed staff pools per priority level.

    Args:
        labor_hours (int): Total estimated labor hours for the task.
        priority (str): Priority level ('critical', 'high', or 'low').

    Returns:
        dict: Contains:
            - assigned_staff (list of str)
    """
    staff_pool = {
        "critical": ["tech_lead", "senior_mechanic"],
        "high": ["mechanic", "junior_mechanic"],
        "low": ["junior_mechanic"]
    }

    staff = staff_pool.get(priority, ["mechanic"])

    return {
        "assigned_staff": staff
    }