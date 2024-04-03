def driver_mapper_in_dict_dnf(driver_list_course_dict, driver_list_course_dnf_dict):
    # Créer un nouveau dictionnaire avec les mêmes valeurs que dict2 mais avec les clés de dict1
    driver_list_course_dnf_dict = {key: driver_list_course_dnf_dict.get(value) for key, value in driver_list_course_dict.items() if value in driver_list_course_dnf_dict.values()}
    return driver_list_course_dnf_dict
