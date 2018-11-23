

def getProductWeight(dataset):

    result = dict()

    for email in list( dataset.keys() ):
        orders = dataset[email]["orders"]

        for date in list( orders.keys() ):
            products = orders[date]["products"]


            for product in list (products.keys()):

                if product in result:
                    result[product] +=products[product]["weight"]
                else:
                    result[product] = products[product]["weight"]


    return result


def getUserExpenses(dataset, email):
    orders = dataset[email]["orders"]

    total=0;
    for date in list(orders.keys()):
        products = orders[date]["products"]

        for product in list(products.keys()):
            total+= products[product]["weight"]*products[product]["price_per_kilo"]

    return total


def getAllUsersExpenses(dataset):
    result = dict()

    for email in list(dataset.keys()):
        result[email] = getUserExpenses(dataset, email)

    return result;