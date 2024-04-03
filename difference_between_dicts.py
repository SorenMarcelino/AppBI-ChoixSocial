def difference_between_dicts(driver_list_reference_dict, driver_list_course_dict, driver_list_course_dnf_dict):
    to_add = []
    for driver_season_key, driver_season_value in driver_list_reference_dict.items():
        found = False
        for driver_course_key, driver_course_value in driver_list_course_dict.items():
            if driver_season_value == driver_course_value:
                found = True
                break
        if not found:
            print(f"{driver_season_value} est manquant")
            to_add.append(driver_season_value)

    # Ajout des pilotes dnf dans le dictionnaire dnf
    for i, driver in enumerate(to_add, start=len(driver_list_course_dnf_dict) + 1):
        driver_list_course_dnf_dict[i] = driver

    # Ajout des pilotes dnf à la fin du dictionnaire des participants
    for i, driver in enumerate(to_add, start=len(driver_list_course_dict) + 1):
        driver_list_course_dict[i] = driver

    print(f"liste des participants : {driver_list_course_dict}")
    # print(f"liste des dnf : {driver_list_course_dnf_dict}")

    return driver_list_course_dnf_dict
