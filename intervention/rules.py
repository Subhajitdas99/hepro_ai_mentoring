def intervention_plan(cluster_id, sri):
    if cluster_id == 1:
        return "Immediate mentor intervention: Productivity coaching"

    if cluster_id == 3:
        return "Career guidance + structured mentoring plan"

    if cluster_id == 0:
        return "Performance sustainability + wellness monitoring"

    if cluster_id == 2:
        return "Advanced mentoring & leadership track"

    return "General guidance"
