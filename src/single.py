import validate_workflow


def validatesingle(
    key1="",
    key2="",
    ownvat="",
    foreignvat="",
    company="",
    street="",
    zip="",
    town="",
    type="vies",
    lang="en",
):
    data = {
        "key1": key1,
        "key2": key2,
        "ownvat": ownvat,
        "foreignvat": foreignvat,
        "company": company,
        "street": street,
        "zip": zip,
        "town": town,
        "type": type,
        "lang": lang,
    }
    r = validate_workflow.start_validation(data)

    return r
