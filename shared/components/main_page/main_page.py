from shared.components.mongo.mongo import get_plan_data


def main_page_data():
    data = {
        "card_name": "План",
        "card_data": get_plan_data()
    }

    return data