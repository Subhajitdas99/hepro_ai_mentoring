def compute_sri(aps, wws, ptms, crs):
    sri = (
        0.30 * aps +
        0.25 * wws +
        0.20 * ptms +
        0.25 * crs
    )
    return round(sri, 2)

